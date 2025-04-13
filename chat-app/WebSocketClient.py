import websocket
import threading
import time
import json
from PySide6.QtCore import QThread, Signal

def stomp_frame(command, headers=None, body=""):
    """Tworzy STOMP frame jako string."""
    if headers is None:
        headers = {}
    frame = command + "\n"
    for key, value in headers.items():
        frame += f"{key}:{value}\n"
    frame += "\n" + body + "\0"
    return frame

class WebSocketStompClient(QThread):
    received_message = Signal(str)

    def __init__(self, uri, username):
        super().__init__()
        self.uri = uri
        self.username = username
        self.ws = None
        self.connected = False
        self.running = True

    def run(self):
        while self.running:
            try:
                self.ws = websocket.WebSocketApp(
                    self.uri,
                    on_open=self.on_open,
                    on_message=self.on_message,
                    on_error=self.on_error,
                    on_close=self.on_close
                )
                self.ws.run_forever()
            except Exception as e:
                print(f"WebSocket thread error: {e}")
                time.sleep(5)  # Retry after delay

    def on_open(self, ws):
        print("WebSocket connection opened.")
        self.connected = True

        connect_frame = stomp_frame("CONNECT", headers={
            "accept-version": "1.1,1.2",
            "host": "linkup-rf0o.onrender.com"
        })
        ws.send(connect_frame)
        print("Sent CONNECT frame.")
        time.sleep(1)

        public_subscribe_frame = stomp_frame("SUBSCRIBE", headers={
            "id": "sub-0",
            "destination": "/topic/public"
        })
        ws.send(public_subscribe_frame)
        print("Subscribed to public chat.")

        private_subscribe_frame = stomp_frame("SUBSCRIBE", headers={
            "id": "sub-1",
            "destination": f"/user/{self.username}/private"
        })
        ws.send(private_subscribe_frame)
        print(f"Subscribed to private messages for {self.username}.")

    def on_message(self, ws, message):
        print("Received message:", message)
        if not message.startswith("CONNECTED"):
            self.received_message.emit(message)

    def on_error(self, ws, error):
        print("WebSocket error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed:", close_status_code, close_msg)
        self.connected = False

    def send_message(self, recipient, message_text):
        if self.ws and self.connected:
            try:
                message_body = json.dumps({
                    "sender": self.username,
                    "recipient": recipient,
                    "encryptedMessage": message_text["encryptedMessage"],
                    "iv": message_text["iv"],
                    "keyForRecipient": message_text["keyForRecipient"],
                    "keyForSender": message_text["keyForSender"]
                })

                send_frame = stomp_frame("SEND", headers={
                    "destination": "/app/chat.private",
                    "content-length": str(len(message_body))
                }, body=message_body)

                self.ws.send(send_frame)
                print(f"Sent private message to {recipient}: {message_text}")
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("Cannot send message: not connected.")

    def stop_client(self):
        self.running = False
        if self.ws and self.connected:
            try:
                disconnect_frame = stomp_frame("DISCONNECT")
                self.ws.send(disconnect_frame)
                print("Sent DISCONNECT frame.")
            except Exception as e:
                print(f"Error during disconnect: {e}")
        if self.ws:
            self.ws.close()

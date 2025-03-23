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
        self.ws = None
        self.connected = False
        self.username = username

    def run(self):
        self.ws = websocket.WebSocketApp(
            self.uri,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

        self.ws.run_forever()

    def on_open(self, ws):
        print("WebSocket connection opened.")
        self.connected = True

        # Wysyłamy STOMP CONNECT frame
        connect_frame = stomp_frame("CONNECT", headers={
            "accept-version": "1.1,1.2",
            "host": "linkup-rf0o.onrender.com"
        })
        ws.send(connect_frame)
        print("Sent CONNECT frame.")

        time.sleep(1)  # Poczekaj, aż serwer potwierdzi CONNECTED

        # Subskrypcja publicznych wiadomości
        public_subscribe_frame = stomp_frame("SUBSCRIBE", headers={
            "id": "sub-0",
            "destination": "/topic/public"
        })
        ws.send(public_subscribe_frame)
        print("Subscribed to public chat.")

        # Subskrypcja prywatnych wiadomości użytkownika
        private_subscribe_frame = stomp_frame("SUBSCRIBE", headers={
            "id": "sub-1",
            "destination": f"/user/{self.username}/private"
        })
        ws.send(private_subscribe_frame)
        print(f"Subscribed to private messages for {self.username}.")

    def on_message(self, ws, message):
        print("Received message:", message)

        if message.startswith("CONNECTED"):
            return

        self.received_message.emit(message)

    def on_error(self, ws, error):
        print("WebSocket error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed:", close_status_code, close_msg)
        self.connected = False

    def send_message(self, recipient, message_text):
        if self.ws and self.connected:
            message_body = json.dumps({
                "sender": self.username,
                "content": message_text,
                "recipient": recipient
            })

            # Wysyłamy do `/app/chat.private`, aby kontroler Spring obsłużył wiadomość
            send_frame = stomp_frame("SEND", headers={
                "destination": "/app/chat.private",
                "content-length": str(len(message_body))
            }, body=message_body)
            self.ws.send(send_frame)
            print(f"Sent private message to {recipient}: {message_text}")
        else:
            print("Not connected.")

    def stop_client(self):
        if self.ws:
            self.ws.close()

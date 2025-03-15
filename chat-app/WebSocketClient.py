import stomp
from PySide6.QtCore import QThread, Signal

class WebSocketClient(QThread):
    received_message = Signal(str)

    def __init__(self, uri):
        super().__init__()
        self.uri = uri
        self.connection = None

    def on_message(self, headers, message):
        self.received_message.emit(message)

    def on_error(self, headers, message):
        print(f"Error: {message}")

    def on_connecting(self, host_and_port):
        print(f"Connecting to {host_and_port}")

    def run(self):
        self.connection = stomp.Connection([("wss://linkup-rf0o.onrender.com/ws", 443)])
        self.connection.set_listener("", self)
        self.connection.connect(wait=True)

        # Subskrybuj temat
        self.connection.subscribe(destination="/topic/public", id=1, ack="auto")

        while True:
            pass  # Czekaj na wiadomości, wszystko będzie obsługiwane przez listenera

    def send_message(self, message):
        if self.connection:
            self.connection.send(destination='/topic/public', body=message)

    def stop(self):
        if self.connection:
            self.connection.disconnect()
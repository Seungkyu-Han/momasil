from typing import Dict, Set
from fastapi import WebSocket

class SocketManager:
    def __init__(self):
        self.active_connections: Dict[int, Set[WebSocket]] = {}

    async def connect(self, cart_id: int, websocket: WebSocket):
        await websocket.accept()
        if cart_id not in self.active_connections:
            self.active_connections[cart_id] = set()
        self.active_connections[cart_id].add(websocket)

    def disconnect(self, cart_id: int, websocket: WebSocket):
        if cart_id in self.active_connections:
            self.active_connections[cart_id].discard(websocket)
            if not self.active_connections[cart_id]:
                del self.active_connections[cart_id]

    async def broadcast(self, cart_id: int, message: dict):
        if cart_id not in self.active_connections:
            return

        dead_connections = []

        for websocket in self.active_connections[cart_id]:
            try:
                await websocket.send_json(message)
            except Exception:
                dead_connections.append(websocket)

        for websocket in dead_connections:
            self.disconnect(cart_id, websocket)

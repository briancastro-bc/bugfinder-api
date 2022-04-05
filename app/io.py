from app.namespaces import auth, game
from app.core import settings

import socketio

def create_async_sio() -> socketio.AsyncServer:
    sio = socketio.AsyncServer(
        logger=True,
        always_connect=False,
        async_mode="asgi",
        ping_interval=30000,
        ping_timeout=100000,
        cors_allowed_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        cors_credentials=True,
        engineio_logger=True
    )
    sio.register_namespace(
        auth.AuthNamespace(namespace="/auth")
    )
    sio.register_namespace(
        game.GameNamespace(namespace="/game")
    )
    return sio
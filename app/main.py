from .app import create_application
from .io import create_async_sio

import socketio

sio = create_async_sio()
app = create_application()
io_app = socketio.ASGIApp(
    socketio_server=sio,
    other_asgi_app=app
)

@app.on_event("startup")
async def on_startup():
    print('Application started')
    
@app.on_event("shutdown")
async def on_shutdown():
    print('Shutdown application')

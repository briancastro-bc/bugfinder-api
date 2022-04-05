from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import settings

def create_application() -> FastAPI: 
    app = FastAPI(
        debug=True,
        title="RESTful API of BUGFINDER",
        description="""
            Resource server for Bugfinder project
        """,
        version="0.1.0",
        contact={
            "brian": {
                "email": "yitocode@gmail.com",
            },
            "james": {
                "email": "example@gmail.com"
            },
            "alejo": {
                "email": "example@gmail.com"
            }
        }
    )
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        expose_headers=None
    )
    return app
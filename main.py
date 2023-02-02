from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.expectlist import expectlist_router
import uvicorn
from uvicorn.config import LOGGING_CONFIG

app = FastAPI()
api_router = APIRouter()

api_router.include_router(expectlist_router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api_router.get("/")
def root() -> dict:
    return {"msg": "Hello root"}


app.include_router(api_router)

if __name__ == "__main__":
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    uvicorn.run(app, host="127.0.0.1", port=8001)

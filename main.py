from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_route import router as UserRouter
from routes.mentor_route import router as MentorRouter
from routes.plan_route import router as PlanRouter
import uvicorn

app = FastAPI()

app.include_router(UserRouter)
app.include_router(MentorRouter)
app.include_router(PlanRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index() -> dict[str, str]:
    return {"data": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="debug",
        reload="True"
    )

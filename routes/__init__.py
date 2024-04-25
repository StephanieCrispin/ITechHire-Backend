from fastapi import APIRouter
from .talent import router as talent_router
from .company import router as company_router
from .employee import router as employee_router
from .vacancy import router as vacancy_router
from .task import router as task_router
api_router = APIRouter()

# NOTE: All routes prefix must be registered here

routes = [
    "/ping",
    "/create"
    "/login",
    "/delete"
]

api_router.include_router(
    talent_router,
    prefix="/talent",
    tags=["Talent Services"]
)

api_router.include_router(
    company_router,
    prefix="/company",
    tags=["Company Services"]
)

api_router.include_router(
    employee_router,
    prefix="/employee",
    tags=["Employee Services"]
)
api_router.include_router(
    vacancy_router,
    prefix="/vacancy",
    tags=["Vacancy Services"]
)

api_router.include_router(
    task_router,
    prefix="/task",
    tags=["Task Services"]
)

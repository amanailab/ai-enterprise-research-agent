from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.research import router as research_router
from app.api.users import router as users_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    description="Backend API for an AI-powered enterprise research agent.",
    version="1.0.0",
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ],
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(users_router)
app.include_router(research_router)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    return {
        "message":
        f"{settings.app_name} API is running"
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "environment":
        settings.environment
    }
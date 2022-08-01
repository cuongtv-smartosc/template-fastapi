from fastapi import FastAPI

app = FastAPI(
    title="Template FastApi",
    description="Template fast api",
)

app.include_router(api_router, prefix=settings.API_V1_STR)
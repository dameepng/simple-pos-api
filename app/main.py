from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.routes.products import router as products_router
from app.api.routes.orders import router as orders_router

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(title=settings.APP_NAME)

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    app.include_router(products_router)
    app.include_router(orders_router)
    return app

app = create_app()

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import Base, engine
from app.db_wait import wait_for_db
from app.core.error_handler import ErrorHandlerMiddleware

from app.modules.auth.auth_routes import router as auth_router
from app.modules.dashboard.dashboard_routes import router as dashboard_router
from app.modules.analytics.analytics_routes import router as analytics_router
from app.modules.leads.leads_routes import router as leads_router
from app.modules.sales.sales_routes import router as sales_router
from app.modules.contents.contents_routes import router as contents_router
from app.modules.settings.settings_routes import router as settings_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    wait_for_db()
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title = 'Backend Management', lifespan= lifespan)

# app.add_middleware(ErrorHandlerMiddleware)

app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)
app.include_router(leads_router)
app.include_router(sales_router)
app.include_router(contents_router)
app.include_router(settings_router)

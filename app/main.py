"""Main entry point for the Smart Summary App Backend.

This module initializes the FastAPI application and runs the server using Uvicorn.
"""

import logging
from collections.abc import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

from app.api import bars

logger = logging.getLogger("api")
logging.basicConfig(level=logging.INFO)


def add_cors_middleware(app: FastAPI) -> None:
    """Add CORS middleware to the FastAPI application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@asynccontextmanager
async def lifespan(_: Request) -> AsyncGenerator[None]:
    """Application lifespan events."""
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = FastAPI(title="Smart Summary App Backend", version="1.0.0", dependencies=[])
add_cors_middleware(app)


@app.get("/docs", include_in_schema=False)
def swagger_ui() -> HTMLResponse:
    """Serve the Swagger UI for the API.

    Returns
    -------
    HTMLResponse
        The HTML content for the Swagger UI.

    """
    return get_swagger_ui_html(openapi_url=app.openapi_url, title=app.title + " - Swagger UI")


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint.

    Returns
    -------
    dict
        A dictionary indicating the health status of the application.

    """
    return {"status": "healthy"}


app.include_router(bars.router, prefix="/api/v1", tags=["bars"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # noqa: S104
        port=8000,
        reload=True,
    )

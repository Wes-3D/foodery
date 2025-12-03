from fastapi import FastAPI, Request, Query, Depends, BackgroundTasks, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import logging

from app.core.log import setup_logging
from app.routers.products import router_products
from app.routers.recipes import router_recipes
from app.db.db import init_database
from config import settings

# Initialize logging early
setup_logging()
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="assets/templates")
app = FastAPI()
app.state.settings = settings
init_database(app)

app.mount("/static", StaticFiles(directory="assets/static"), name="static")
#app.include_router(router_scan)
app.include_router(router_products)
app.include_router(router_recipes)



@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

### Squirrelf AI Example ###
@app.get("/example", response_class=HTMLResponse)
def example(request: Request):
    return templates.TemplateResponse("squirrelf_example.html", {"request": request})


if __name__ == "__main__":
    ssl_keyfile = os.path.join("assets/certs", "key.pem")
    ssl_certfile = os.path.join("assets/certs", "cert.pem")
    #uvicorn.run(app, host="0.0.0.0", port=5000)
    #uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=5000, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)





"""
def create_app(settings=Settings) -> FastAPI:
    app = FastAPI(title="MyApp")

    # Load settings
    app.state.settings = settings()

    # Templates / Static
    app.mount("/static", StaticFiles(directory="assets/static"), name="static")
    templates = Jinja2Templates(directory="assets/templates")
    app.state.templates = templates

    # Security headers middleware (Flask after_request equivalent)
    @app.middleware("http")
    async def set_secure_headers(request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["X-Download-Options"] = "noopen"
        return response

    #init_logger(app)
    # Initialize components
    init_security(app)
    register_routers(app)          # replaces Flask blueprints
    #init_extensions(app)
    init_error_handlers(app)
    init_database(app)             # run migrations or connect engine

    return app
"""
from fastapi import FastAPI, Request, Query, Depends, BackgroundTasks, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn
import os
import logging

from core.log import setup_logging
from app.products.product_scan import router_scan
from app.products.routes import router_products
from app.recipes.routes import router_recipes

from data import schemas, crud, models
from data.db import get_db, SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Initialize logging early
setup_logging()
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="assets/templates")
app = FastAPI()
#app.mount("/json", StaticFiles(directory="json", html=True), name="root")
app.include_router(router_scan)
app.include_router(router_products)
app.include_router(router_recipes)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


### Squirrelf AI Example ###
@app.get("/example", response_class=HTMLResponse)
def example(request: Request):
    return templates.TemplateResponse("alt/example.html", {"request": request})


if __name__ == "__main__":
    ssl_keyfile = os.path.join("assets/certs", "key.pem")
    ssl_certfile = os.path.join("assets/certs", "cert.pem")
    #uvicorn.run(app, host="0.0.0.0", port=5000)
    #uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
    uvicorn.run(app, host="0.0.0.0", port=5000, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)

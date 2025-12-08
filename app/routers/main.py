from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router_main = APIRouter()

@router_main.get("/", response_class=HTMLResponse)
def index(request: Request):
    return request.app.state.templates.TemplateResponse("base.html", {"request": request})

### Squirrelf AI Example ###
@router_main.get("/example", response_class=HTMLResponse)
def example(request: Request):
    return request.app.state.templates.TemplateResponse("alt/squirrelf_example.html", {"request": request})
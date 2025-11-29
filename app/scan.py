#from flask import Blueprint, render_template, request
from fastapi import APIRouter, Request, Query, Depends, BackgroundTasks, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

import cv2
from pyzbar.pyzbar import decode
import numpy as np
from app.food import food_api

#bp_scan = Blueprint('scan', __name__, template_folder='templates', static_folder='static')

templates = Jinja2Templates(directory="app/templates")
router_scan = APIRouter()



@router_scan.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})



@router_scan.get("/add_product", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("scan.html", {"request": request})


@router_scan.post("/scan", response_class=HTMLResponse)
async def scan(
    request: Request,
    file: UploadFile = File(...),
):
    product = None
    try:
        # Read uploaded file
        contents = await file.read()

        # Decode image
        image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_UNCHANGED)
        barcodes = decode(image)

        if not barcodes:
            return templates.TemplateResponse(
                "scan.html",
                {"request": request, "error": "Barcode not detected or is blank/corrupted!"},
            )

        # Decode first barcode found
        code_string = barcodes[0].data.decode("utf-8")
        product = food_api.product.get(code_string)

        return templates.TemplateResponse(
            "scan.html",
            {"request": request, "code_string": code_string, "product": product},
        )

    except Exception as e:
        return templates.TemplateResponse(
            "scan.html",
            {"request": request, "error": f"Error: {str(e)}"},
        )


@router_scan.post("/lookup")
async def lookup_code(data: dict):
    code = data.get("code")
    if not code:
        return JSONResponse({"error": "No code provided"}, status_code=400)

    product = food_api.product.get(code)
    return {"code": code, "product": product}
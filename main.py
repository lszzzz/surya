# main.py
import json
import logging
import os
import traceback
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI

from dto.prediction_dto import StructurePredictionRequest, StructurePredictionResponse
from service.structure_predict_service import structure_predict


@asynccontextmanager
async def lifespan_context(app):
    print("✅ app initialized.")
    # 在这里 yield，让 FastAPI 应用运行
    yield
    # 当应用关闭时，会回到这里，退出 with 块会自动清理连接
    print("🔌 app cleaned up.")


app = FastAPI(title="ocr api", lifespan=lifespan_context)


@app.post("/structure-predict", response_model=StructurePredictionResponse)
async def structure_predict_endpoint(request: StructurePredictionRequest):
    result = await structure_predict(request.image_name, request.image_url)
    return StructurePredictionResponse(
        layout_prediction=result
    )


@app.get("/health")
async def health():
    return {"success": True}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8200)

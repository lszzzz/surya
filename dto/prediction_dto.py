from typing import Optional, List, Any
from pydantic import BaseModel


# 请求和响应模型
class StructurePredictionRequest(BaseModel):
    image_name: str
    image_url: str


class StructurePredictionResponse(BaseModel):
    layout_prediction: dict

from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    code: int
    name: str
    volumeUnit: str
    volumeQty: float
    weightGram: float | None = None
    #weightGram: float


class ProductCreate(ProductBase):
    pass

class ProductSchema(ProductBase):
    id: int
    class Config:
        from_attributes = True




class RecipeIngredientBase(BaseModel):
    #ingredient_id: int
    quantity: float
    name: str
    unit: Optional[str] = None
    method: Optional[str] = None

class RecipeStepBase(BaseModel):
    step_number: int
    description: str

class RecipeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    servings: int = 1
    time_prep: int = 5
    time_cook: int = 5
    ingredients: List[RecipeIngredientBase]
    steps: List[RecipeStepBase]

class RecipeSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    servings: int
    time_prep: int
    time_cook: int
    ingredients: List[RecipeIngredientBase]
    steps: List[RecipeStepBase]
    class Config:
        from_attributes = True

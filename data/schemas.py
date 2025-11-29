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

class Product(ProductBase):
    id: int
    class Config:
        from_attributes = True

class RecipeIngredientBase(BaseModel):
    ingredient_id: int
    quantity: float

class RecipeStepBase(BaseModel):
    step_number: int
    description: str

class RecipeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    servings: int = 1
    ingredients: List[RecipeIngredientBase]
    steps: List[RecipeStepBase]

class Recipe(BaseModel):
    id: int
    name: str
    description: Optional[str]
    servings: int
    ingredients: List[RecipeIngredientBase]
    steps: List[RecipeStepBase]
    class Config:
        from_attributes = True

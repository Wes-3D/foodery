#from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, Date
#from sqlalchemy.orm import relationship
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from typing import List, Optional
from datetime import date
import uuid


##############################
#####      Users      #####
##############################
# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)

class User(UserBase, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    #username: str
    hashed_password: str
    #recipes: list["Recipe"] = Relationship(back_populates="owner", cascade_delete=True)
    #mealplans: list["MealPlan"] = Relationship(back_populates="owner", cascade_delete=True)



##############################
#####      Products      #####
##############################
class ProductBase(SQLModel):
    code: int
    name: str
    #name: Optional[str] = None
    volumeUnit: str = "unit"
    volumeQty: float
    weightGram: float | None = None
    #weightGram: Optional[float] = None
    brand: Optional[str] = None
    category: Optional[str] = None


class ProductCreate(ProductBase):
    pass

class ProductSchema(ProductBase):
    id: int
    class Config:
        from_attributes = True


class Product(ProductBase, table=True):
    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)





##############################
#####      Recipes       #####
##############################


class RecipeIngredientBase(SQLModel):
    #ingredient_id: int
    quantity: float
    name: str
    unit: Optional[str] = None
    method: Optional[str] = None

class RecipeStepBase(SQLModel):
    step_number: int
    description: str

class RecipeBase(SQLModel):
    name: str
    description: Optional[str] = None
    servings: int = 1
    time_prep: int = 5
    time_cook: int = 5



class RecipeCreate(RecipeBase):
    ingredients: List[RecipeIngredientBase]
    steps: List[RecipeStepBase]
    pass

class RecipeSchema(RecipeBase):
    id: int
    class Config:
        from_attributes = True



class RecipeIngredient(RecipeIngredientBase, table=True):
    __tablename__ = "recipe_ingredients"

    id: Optional[int] = Field(default=None, primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.id")

    recipe: "Recipe" = Relationship(back_populates="ingredients")

class RecipeStep(RecipeStepBase, table=True):
    __tablename__ = "recipe_steps"

    id: Optional[int] = Field(default=None, primary_key=True)
    recipe_id: int = Field(foreign_key="recipes.id")

    recipe: "Recipe" = Relationship(back_populates="steps")

class Recipe(RecipeBase, table=True):
    __tablename__ = "recipes"

    id: Optional[int] = Field(default=None, primary_key=True)
    #owner_id: int = Field(foreign_key="users.id")

    ingredients: List["RecipeIngredient"] = Relationship(back_populates="recipe", cascade_delete=True)
    steps: List["RecipeStep"] = Relationship(back_populates="recipe", cascade_delete=True)
    #owner: "User" = Relationship(back_populates="recipes")



##############################
#####     Meal Plans     #####
##############################
"""
class MealPlan(Base):
    __tablename__ = "mealplans"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    recipe = relationship("Recipe")
    #user = relationship("User", back_populates="mealplans")
"""

"""
class MealPlanBase(SQLModel):
    date: str
    description: Optional[str] = None
    servings: int = 1
"""
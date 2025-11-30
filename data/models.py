from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, Date
from sqlalchemy.orm import relationship

from data.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    recipes = relationship("Recipe", back_populates="owner")
    mealplans = relationship("MealPlan", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    name = Column(String, nullable=True) #, unique=True, nullable=False
    volumeUnit = Column(String, default="unit")  # g, ml, pcs, etc.
    volumeQty = Column(Float, nullable=False)
    weightGram = Column(Float, nullable=True)
    brand = Column(String, nullable=True)
    category = Column(String, nullable=True)

    recipes = relationship("RecipeIngredient", back_populates="ingredient")

    def to_dict(self):
        return {
            'product_id': self.id,
            'code': self.code,
            'name': self.name,
            'volumeUnit': self.volumeUnit,
            'volumeQty': self.volumeQty,
            'weightGram': self.weightGram if self.weightGram else ""
        }

    """
    def __init__(self, name):
        self.name = name
    """

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False) #, index=True
    description = Column(String)
    servings = Column(Integer, default=1)
    owner_id = Column(Integer, ForeignKey("users.id"))

    #cook_method = Column(String, nullable=True)
    time_prep = Column(Integer, default=5, nullable=True)
    time_cook = Column(Integer, default=5, nullable=True)
    #time_total = Column(Integer, default=10, nullable=True)

    owner = relationship("User", back_populates="recipes")
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")
    steps = relationship("RecipeStep", back_populates="recipe", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "servings": self.servings,
            "time_prep": self.time_prep if self.time_prep else 5,
            "time_cook": self.time_cook if self.time_cook else 5,
            #"time_total": self.time_cook + self.time_prep,
        }

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    ingredient_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Float, nullable=False)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Product", back_populates="recipes")

class RecipeStep(Base):
    __tablename__ = "recipe_steps"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    step_number = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    ##time_perform = Column(Integer, default=1, nullable=True)

    recipe = relationship("Recipe", back_populates="steps")



class MealPlan(Base):
    __tablename__ = "mealplans"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    recipe = relationship("Recipe")
    user = relationship("User", back_populates="mealplans")
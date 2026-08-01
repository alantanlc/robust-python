import datetime
from dataclasses import dataclass
from enum import auto, Enum

class ImperialMeasure(Enum):
    TEASPOON = auto()
    TABLESPOON = auto()
    CUP = auto()

class Broth(Enum):
    VEGETABLE = auto()
    CHICKEN = auto()
    BEEF = auto()
    FISH = auto()

@dataclass(frozen=True)
# Ingredients added into the broth
class Ingredient:
    name: str
    amount: float = 1
    units: ImperialMeasure = ImperialMeasure.CUP

@dataclass(eq=True)
class Recipe:
    aromatics: set[Ingredient]
    broth: Broth
    vegetables: set[Ingredient]
    meats: set[Ingredient]
    starches: set[Ingredient]
    garnishes: set[Ingredient]
    time_to_cook: datetime.timedelta

    def make_vegetarian(self):
        self.meats.clear()
        self.broth = Broth.VEGETABLE

    def get_ingredient_names(self):
        ingredients = (self.aromatics | self.vegetables | self.meats | self.starches | self.garnishes)

        return ({i.name for i in ingredients} | {self.broth.name.capitalize() + " broth"})

pepper = Ingredient("Pepper", 1, ImperialMeasure.TABLESPOON)
garlic = Ingredient("Garlic", 2, ImperialMeasure.TEASPOON)
carrots = Ingredient("Carrots", .25, ImperialMeasure.CUP)
celery = Ingredient("Celery", .25, ImperialMeasure.CUP)
onions = Ingredient("Onions", .25, ImperialMeasure.CUP)
parsley = Ingredient("Parsley", 2, ImperialMeasure.TABLESPOON)
noodles = Ingredient("Noodles", 1.5, ImperialMeasure.CUP)
chicken = Ingredient("Chicken", 1.5, ImperialMeasure.CUP)

print(f'\n{pepper=}\n')

chicken_noodle_soup = Recipe(
    aromatics = {pepper, garlic},
    broth = Broth.CHICKEN,
    vegetables = {celery, onions, carrots},
    meats = {chicken},
    starches = {noodles},
    garnishes = {parsley},
    time_to_cook = datetime.timedelta(minutes=60)
)

chicken_noodle_soup.garnishes.add(pepper)
print(f'{chicken_noodle_soup=}\n')

from copy import deepcopy
# make a deep copy so that changing one soup does not change the original
noodle_soup = deepcopy(chicken_noodle_soup)
noodle_soup.make_vegetarian()
print(f'{noodle_soup.get_ingredient_names()=}\n')

print(f'{chicken_noodle_soup == noodle_soup=}\n')

print(f'{noodle_soup == deepcopy(noodle_soup)=}\n')

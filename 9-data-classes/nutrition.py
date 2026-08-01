from dataclasses import dataclass

# @dataclass(eq=True, order=True)
@dataclass(eq=True)
class NutritionInformation:
    calories: int
    fat: int
    carbohydrates: int

    def __lt__(self, rhs) -> bool:
        return ((self.fat, self.carbohydrates, self.calories) < (rhs.fat, rhs.carbohydrates, rhs.calories))

    def __le__(self, rhs) -> bool:
        return self < rhs or self == rhs

    def __gt__(self, rhs) -> bool:
        return self > rhs

    def __ge__(self, rhs) -> bool:
        return self >= rhs

nutritionals = [
    NutritionInformation(calories=100, fat=1, carbohydrates=3),
    NutritionInformation(calories=50, fat=6, carbohydrates=4),
    NutritionInformation(calories=120, fat=12, carbohydrates=3),
]

print(f'{sorted(nutritionals, reverse=True)=}')

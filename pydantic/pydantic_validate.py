from typing import Optional

from pydantic.dataclasses import dataclass
from pydantic import constr, PositiveInt

from typing import Literal, Optional, Union

import yaml

@dataclass
class AccountAndRoutingNumber:
    account_number: constr(min_length=9, max_length=9)
    routing_number: constr(min_length=8, max_length=12)

@dataclass
class BankDetails:
    bank_details: AccountAndRoutingNumber

AddressOrBankDetails = Union[dict, BankDetails]

Position = Literal['Chef', 'Sous Chef', 'Host', 'Server', 'Delivery Driver']

@dataclass
class Dish:
    name: constr(min_length=1, max_length=17)
    price_in_cents: PositiveInt
    description: constr(min_length=1, max_length=80)
    picture: Optional[str] = None

@dataclass
class Employee:
    name: str
    position: Position
    payment_details: AddressOrBankDetails

@dataclass
class Restaurant:
    name: constr(pattern=r'^[a-zA-Z0-9]*$', min_length=1, max_length=16)
    owner: constr(min_length=1)
    address: constr(min_length=1)
    employees: list[Employee]
    dishes: list[Dish]
    number_of_seats: PositiveInt
    to_go: bool
    delivery: bool

@dataclass
class Address:
    address: constr(min_length=1)

def load_restaurant(filename: str) -> Restaurant:
    with open(filename) as yaml_file:
        data = yaml.safe_load(yaml_file)
        return Restaurant(**data)

try:
    res = load_restaurant('restaurant.yaml')
    print(res)
except Exception as e:
    print(f'e = {e}')
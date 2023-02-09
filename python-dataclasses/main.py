from dataclasses import dataclass, astuple, asdict, field
from typing import Any
from math import asin, cos, radians, sin, sqrt
from pprint import pprint
import inspect


@dataclass(order=True)
class Person:
    first_name: Any = "Kingsley"
    last_name: Any = "Abru"
    age: int = 25
    job: str = ""
    full_name: str = field(init=False, repr=False)
    sort_index: int = field(init=False, repr=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        self.sort_index = self.age

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.age})"

    def __eq__(self, other: object) -> bool:
        if other.__class__ is not self.__class__:
            return NotImplemented

        return (self.first_name, self.last_name, self.age, self.job) == (
            other.first_name,
            other.last_name,
            other.age,
            other.job,
        )  # type: ignore


@dataclass(frozen=True)
class Animal:
    name: str
    age: int
    weight: float
    is_alive_and_hungry: bool = field(init=False, default=False)

    def __post_init__(self):
        object.__setattr__(self, "is_alive_and_hungry", self.weight > 10)


@dataclass()
class Position:
  name: str
  lon: float = 0
  lat: float = 0

  def distance_to(self, other: object) -> float:
    r = 6371  # Earth radius in kilometers
    lam_1, lam_2 = radians(self.lon), radians(other.lon)
    phi_1, phi_2 = radians(self.lat), radians(other.lat)
    h = (sin((phi_2 - phi_1) / 2)**2
          + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
    return 2 * r * asin(sqrt(h))

def main():
    person_one = Person("John", "Doe", 30, "Software Engineer")
    person_two = Person("John", "Doe", 30, "Software Engineer")

    print(f"person = {asdict(person_one)}")
    # person.age = 40  # This will not work
    print(f"person = {astuple(person_one)}")
    print(person_one == person_two)
    print(person_one.full_name)
    pprint(inspect.getmembers(Person, inspect.isfunction))

    oslo = Position("Oslo", 10.8, 59.9)
    vancouver = Position("Vancouver", -123.1, 49.2)
    print(oslo.distance_to(vancouver))


if __name__ == "__main__":
    main()

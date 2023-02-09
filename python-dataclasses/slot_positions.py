from dataclasses import dataclass
from pympler import asizeof
from timeit import timeit

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float
    

def main():
    simple = SimplePosition('London', -0.1, 51.5)
    slot = SlotPosition('Madrid', -3.7, 40.4)
    
    print(asizeof.asizesof(simple, slot))
    
    print(timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals()))
    print(timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals()))

if __name__ == '__main__':
    main()

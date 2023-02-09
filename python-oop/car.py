class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model

class Device:
    def __init__(self):
        self._voltage = 12

# Multiple Inheritance
class Car:
    def __init__(self, color:str, model:str, year:int) -> None:
        Vehicle.__init__(self, color, model)
        Device.__init__(self)
        self.year = year

    # Private variable decorator
    @property
    def voltage(self)-> int:
        return self._voltage
    
    @voltage.setter
    def voltage(self, volts:int) -> None:
        print("Warning: this can cause problems!")
        self._voltage = volts

    @voltage.deleter
    def voltage(self) -> None:
        print("Warning: the radio will stop working!")
        del self._voltage
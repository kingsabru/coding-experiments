from car import *

def main():
  my_car = Car("Red", "Toyota", 2017)

  print(f"My car uses {my_car.voltage} volts")

  my_car.voltage = 6

  print(f"My car now uses {my_car.voltage} volts")

  del my_car.voltage

  print(f"My car is now uses {my_car.voltage} volts")

if __name__ == '__main__':
  main()
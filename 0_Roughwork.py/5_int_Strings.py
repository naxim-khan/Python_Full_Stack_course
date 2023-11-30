



import math
import os
import random
import re
import sys


class Car:
    def __init__(self,max_speed,units):
        self.max_speed=max_speed
        self.units=units
    # pass
    def __str__(self):
        return f"Car with maximum speed of {self.max_speed} {self.units}"

class Boat:
    def __init__(self,max_speed_knots):
        self.max_speed_knots=max_speed_knots
    def __str__(self):
        return f"Boat with the maximum speed of {self.max_speed_knots} knots"
    # pass 

if __name__ == '__main__':
    q = int(input())
    queries = []

    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]

        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
            queries.append(str(vehicle))
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
            queries.append(str(vehicle))
        else:
            raise ValueError("invalid vehicle type")

    print('\n'.join(queries))





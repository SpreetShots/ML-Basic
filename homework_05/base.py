from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel
        
class Vehicle(ABC):
    def __init__(self, weight: float = 0.0, fuel: float = 0.0, fuel_consumption: float = 0.0):
        self.weight = float(weight)
        self.started = False
        self.fuel = float(fuel)
        self.fuel_consumption = float(fuel_consumption)

    def start(self):
        """
        Метод для запуска двигателя машины
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError(self.fuel)

    def move(self, distance: float):
        """
        Переместить машину на определенное расстояние. Расстояние в КМ

        Args:
            distance (float): Расстояние в км.
        """
        if distance < 0:
            raise ValueError("Значение не может быть отрицательным")

        required = distance / 100 * self.fuel_consumption

        if required <= self.fuel:
            self.fuel -= required
        else:
            raise NotEnoughFuel(self.fuel)

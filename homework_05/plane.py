from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, max_cargo):
        self.max_cargo = float(max_cargo)
        self.cargo = 0.0

    def load_cargo(self, amount):
        """
        Метод для загрузки машины

        Args:
            amount (float): Передаваемый вес.
        """
        amount = float(amount)
        if amount < 0:
            raise ValueError("Значение не может быть отрицательным")
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload(f"{self.cargo + amount} > {self.max_cargo}")
        self.cargo += amount

    def remove_all_cargo(self):
        """
        Функция для обнуления груза

        Returns:
            float: Предыдущее значение загрузки машины
        """
        previous = self.cargo
        self.cargo = 0.0
        return previous
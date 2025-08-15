class LowFuelError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Ошибка, низкое топливо. Текущее топливо: {self.value}"

class NotEnoughFuel(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Ошибка, отсутствует топливо. Текущее топливо: {self.value}"


class CargoOverload(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Ошибка, машина перегружена. Текущий вес: {self.value}"
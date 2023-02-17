""" Работа над ошибками:
1. Все переменные с маленькой буквы
2. Так возвращать не правильно return (print("Object in a solid state")),
поскольку возвращается none.
Исправленный код ниже
"""


class PropertiesChemicalElement:

    def __init__(self, melting_temperature, boiling_temperature):
        self.melting_temperature = melting_temperature
        self.boiling_temperature = boiling_temperature

    def check_status(self, temperature):
        if temperature < self.melting_temperature:
            return f"Object in a solid state"
        elif self.melting_temperature <= temperature < self.boiling_temperature:
            return f"Object in a liquid state"
        elif temperature > self.boiling_temperature:
            return f"Object in a gaseous state"


if __name__ == '__main__':
    pb = PropertiesChemicalElement(327.5, 1749)
    print(pb.check_status(500))
    print(pb.check_status(100))
    ti = PropertiesChemicalElement(1668, 3227)
    print(ti.check_status(1000))
    print(ti.check_status(2000))
    print(ti.check_status(5000))

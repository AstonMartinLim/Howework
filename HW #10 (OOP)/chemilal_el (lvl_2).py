
class PropertiesChemicalElement:

    def __init__(self, melting_temperature, boiling_temperature):
        self.melting_temperature = melting_temperature
        self.boiling_temperature = boiling_temperature

    def _convert_temperature(self, temperature, scale):
        if scale == 'F':
            return (temperature-32)*5/9
        if scale == 'K':
            return (temperature-273.15)

    def check_status(self, temperature, scale):
        if scale == 'F' or scale == 'K':
            conv_temperature = self._convert_temperature(temperature, scale)
        else:
            conv_temperature = temperature
       
        if conv_temperature < self.melting_temperature:
            return f"Object in a solid state"
        elif self.melting_temperature <= conv_temperature < self.boiling_temperature:
            return f"Object in a liquid state"
        elif conv_temperature > self.boiling_temperature:
            return f"Object in a gaseous state"


if __name__ == '__main__':
    pb = PropertiesChemicalElement(327.5, 1749)
    print(pb.check_status(500, 'F'))
    print(pb.check_status(500, 'K'))
    print(pb.check_status(500, 'C'))

    ti = PropertiesChemicalElement(1668, 3227)
    print(ti.check_status(1000, 'F'))
    print(ti.check_status(2000, 'K'))
    print(ti.check_status(5000, 'K'))
    print(ti.check_status(2000, 'C'))


class PropertiesChemicalElement:


    def __init__(self, MeltingTemperature, BoilingTemperature):
        self.MeltingTemperature = MeltingTemperature
        self.BoilingTemperature = BoilingTemperature


    def _convert_temperature(self, Temperature, Scale):
        if Scale == 'F':
            return (Temperature - 32)*5/9
        if Scale == 'K':
            return (Temperature - 273.15)        

 
    def chek_status (self, Temperature, Scale):
        if Scale == 'F' or Scale == 'K':
            Conv_Temperature = self._convert_temperature(Temperature, Scale)
        else:
            Conv_Temperature = Temperature
       
        if Conv_Temperature < self.MeltingTemperature:
            return (print("Object in a solid state"))
        elif Conv_Temperature >= self.MeltingTemperature and Conv_Temperature < self.BoilingTemperature:
            return (print("Object in a liquid state"))
        elif Conv_Temperature > self.BoilingTemperature:
            return (print("Object in a gaseous state"))

if __name__ == '__main__':
    pb = PropertiesChemicalElement(327.5, 1749)
    pb.chek_status(500, 'F')
    pb.chek_status(500, 'K')
    pb.chek_status(500, 'C')

    ti = PropertiesChemicalElement(1668, 3227)
    ti.chek_status (1000, 'F')
    ti.chek_status (2000, 'K')
    ti.chek_status (5000, 'K')
    ti.chek_status (2000, 'C')

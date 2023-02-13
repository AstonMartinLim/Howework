
class PropertiesChemicalElement:

    def __init__(self, MeltingTemperature, BoilingTemperature):
        self.MeltingTemperature = MeltingTemperature
        self.BoilingTemperature = BoilingTemperature
        
 
    def chek_status (self, Temperature):        
        if Temperature < self.MeltingTemperature:
            return (print("Object in a solid state"))
        elif Temperature >= self.MeltingTemperature and Temperature < self.BoilingTemperature:
            return (print("Object in a liquid state"))
        elif Temperature > self.BoilingTemperature:
            return (print("Object in a gaseous state"))

if __name__ == '__main__':
    pb = PropertiesChemicalElement(327.5, 1749)
    pb.chek_status(500)
    pb.chek_status(100)
    ti = PropertiesChemicalElement(1668, 3227)
    ti.chek_status (1000)
    ti.chek_status (2000)
    ti.chek_status (5000)  

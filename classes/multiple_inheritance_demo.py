class LandVehicle():

    def __init(self,list_of_parts)
        self.list_of_parts=list_of_parts
    
    def displayParts(self,list_of_parts):
        print("Land Vehicles have ",part_name) 


class WaterVehicle():
    
    def displayParts(self,part_name):
        print("Water Vehicles have ",part_name) 
   


class AmphibiousVehicle(LandVehicle,WaterVehicle):
    
    def displayParts(self,part_name):
        print("Amphibious Vehicles have both {} ",part_name) 


def main():

    a = AmphibiousVehicle():
        

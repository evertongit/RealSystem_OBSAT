from .sensors import Sensors
from .payload import Payload_SDR
from .telemetry import Telemetry

class CubesatParameter():

    def __init__(self):
        self.cube_sensors = Sensors()
        self.cube_telemetry = Telemetry()
        #self.cube_payload_sdr = Payload_SDR()

    def get_data_from_sensors(self):
    
        #self.cube_data = self.cube_sensors.get_sensors_data()    
        self.cube_data = self.cube_sensors.get_test_array()
        return self.cube_data
    

    def post_data(self, data_to_post):
   
        self.cube_telemetry.send_data(data_to_post)


    def get_data_from_payload(self):
        pass



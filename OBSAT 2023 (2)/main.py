#main file
#https://obsat.org.br/teste_post/index.php
'''
from Source.sensors import Sensors
from Source.payload import Payload_SDR
from Source.telemetry import Telemetry
'''

from Source.cubesat_paramater import CubesatParameter


if __name__ == "__main__":
   bacurau_i = CubesatParameter()
   bacura_i_data = bacurau_i.get_data_from_sensors()
   
   print(bacura_i_data)
   if bacurau_i.post_data(bacura_i_data) is not None:
      print("Upload successful!")


    
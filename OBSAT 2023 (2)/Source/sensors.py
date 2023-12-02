import smbus2
import bme280
from imusensor.MPU9250 import MPU9250
from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1
team_code = 8

class Sensors:
    MPU_ADDRESS = 0X68
    BME_ADDRESS = 0X77
    PORT = 1
    CALIBRATION_FILE_PATH = "/home/pi/MPU9250-rpi/data/calib.json"
    SHUNT_OHMS = 0.1 


    def __init__(self):
        self.bme_sensor = None
        self.imu = None

    def initialize_mpu(self):
        try:
            self.bus = smbus2.SMBus(Sensors.PORT)
            self.imu = MPU9250.MPU9250(self.bus, Sensors.MPU_ADDRESS)
            self.imu.begin()
            self.calibration_parameters = bme280.load_calibration_params(self.bus, Sensors.BME_ADDRESS)
        except Exception as e:
            print(f"Failed to initialize MPU: {e}")
            self.imu = None

    def initialize_bme_sensor(self):
        try:
            self.bme_sensor = bme280.sample(self.bus, Sensors.BME_ADDRESS, self.calibration_parameters)
        except Exception as e:
            print(f"Failed to initialize BME sensor: {e}")
            self.bme_sensor = None

    def initialize_ina_sensor(self):
        self.ina = INA219(Sensors.SHUNT_OHMS)
        self.ina.configure()

    def get_imu_data(self):
        try:
            if self.imu is None:
                self.initialize_mpu()  # Initialize MPU if not done already
            if self.imu:
                self.imu.loadCalibDataFromFile(Sensors.CALIBRATION_FILE_PATH)
                self.imu.readSensor()
                self.imu.computeOrientation()
                return (
                    self.imu.AccelVals[0],self.imu.AccelVals[1], self.imu.AccelVals[2],
                    self.imu.GyroVals[0], self.imu.GyroVals[1], self.imu.GyroVals[2]
                )
            else:
                print("IMU not initialized.")
                return None
        except Exception as e:
            print(f"Failed to retrieve IMU data: {e}")
            return None

    def get_bme_data(self):
        try:
            if self.bme_sensor:
                return self.bme_sensor.temperature, self.bme_sensor.pressure
            else:
                print("BME sensor not initialized.")
                return None
        except Exception as e:
            print(f"Failed to retrieve BME data: {e}")
            return None

    def get_ina_data(self):
        
        try:
            self.voltage = self.ina.voltage()
            self.current = self.ina.current()
            self.shunt_voltage = self.ina.shunt_voltage()
            return (self.voltage, self.current, self.shunt_voltage)
        except DeviceRangeError as e:
            # Current out of device range with specified shunt resistor
            print(e)
            return None

    def get_test_array(self):
        return {
            "equipe": team_code,
            "bateria": 99,
            "temperatura": 33,
            "pressao": 9,
            "giroscopio": [7, 4, 3],
            "acelerometro": [7, 7, 7],
            "payload": [7, 7, 7, 7, 7]
        }
    
    def get_sensors_data(self):
        imu_data = self.get_imu_data()
        bme_data = self.get_bme_data()
        ina_data = self.get_ina_data()
        test_array = self.get_test_array()
        
        if imu_data is not None and bme_data is not None and ina_data is not None:
            return {
                    "equipe": team_code,
                    "bateria": ina_data[0],
                    "temperatura": bme_data[0],
                    "pressao": bme_data[1],
                    "giroscopio": imu_data[3:6],
                    "aceletrometro": imu_data[:3],
                    "payload": [7,7,7]
            }
        else:
            return None
        

#sensors = Sensors()
#sensors.initialize_bme_sensor()
#data = sensors.get_test_array()

'''
if data:
    print("Accel (X, Y, Z):", data[:3])
    print("Gyroscope (X, Y, Z):", data[3:6])
    print("Temperature:", data[6])
    print("Pressure:", data[7])
    print("Battery level:", data[8])
else:
    print("Failed to retrieve sensor data.")
'''
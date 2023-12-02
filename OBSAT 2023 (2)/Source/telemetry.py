import requests
import json
# import sensors.py  

team_code = 7

class Telemetry:
    SERVER_URL = 'https://obsat.org.br/teste_post/envio.php'
    
    def __init__(self):
        self.example_data_vector = {
            "equipe": team_code,
            "bateria": 99,
            "temperatura": 33,
            "pressao": 9,
            "giroscopio": [7, 4, 3],
            "acelerometro": [7, 7, 7],
            "payload": [7, 7, 7, 7, 7]
        }        
    
    def send_data(self, data_vector):
        try:
            self.data_vector_json = json.dumps(data_vector)
            post_answer = requests.post(Telemetry.SERVER_URL, data = self.data_vector_json)
            post_answer.raise_for_status()#  cria excessao
            if post_answer.status_code == 200:
                print("Upload successful!")
                return 1
            else:
                print(f"Error sending data. Status code: {post_answer.status_code}")
        except requests.RequestException as e:
            print(f"Connection error: {e}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
             
    def send_data_debugger(self):
        example_data_vector_json = json.dumps(self.example_data_vector)
        try:
            post_answer = requests.post(Telemetry.SERVER_URL, data=example_data_vector_json)
            post_answer.raise_for_status()  # cria excessao
            if post_answer.status_code == 200:
                print("Upload successful!")
            else:
                print(f"Error sending data. Status code: {post_answer.status_code}")
        except requests.RequestException as e:
            print(f"Connection error: {e}")
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
    
    
        
'''
telemetry = Telemetry()

#telemetry.send_data_debugger()


sensors = Sensors()
#sensors.initialize_bme_sensor()
data_buffer = sensors.get_test_array()
#recebe os dados de acel, gyro, temperatura e pressao

real_data = {
    "equipe": team_code, 
    "bateria": data_buffer[8],
    "temperatura": data_buffer[6],
    "pressao": data_buffer[7],
    "acelerometro": data_buffer[:3],
    "giroscopio": data_buffer[3:6],
    "payload": [7,7,7,7,]
} 

telemetry.send_data(real_data)

'''

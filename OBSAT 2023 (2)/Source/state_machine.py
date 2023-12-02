from enum import Enum
import time
import json
import queue


class State(Enum):
    INIT = 0
    STANDBY = 1
    AGENDAMENTO = 2
    PAYLOAD = 3
    MONITORAR = 4
    SEND_MSG = 5

'''
class Event(Enum):
    NULO = 0
    LIGAR = 1
    AGENDAR = 2
'''

class FSM:
    data_values = []
    def __init__(self):
        pass
        #self.current_state = State.INIT

    def process_state(pFSM):
        print(f"Current state: {pFSM.current_state}")
    
        if pFSM.current_state == State.INIT:
            pass 
        elif pFSM.current_state == State.STANDBY:
            time.sleep(10)  
        elif pFSM.current_state == State.PAYLOAD:
            pass
        elif pFSM.current_state == State.MONITORAR:
            FSM.data_values = Sensors.get_sensors_data()
            if (FSM.data_values is None):
                FSM.data_values = Sensors.get_array_test()
                print('Teste')
        elif pFSM.current_state == State.SEND_MSG:
            time.sleep(1)  
           # Telemetry.send_data(0
    
    def next_state(pFSM, pEvents):
        event = pEvents.get() if not pEvents.empty() else Event.NULO
    
        if pFSM.current_state == State.INIT:
            if event == Event.LIGAR:
                pFSM.current_state = State.STANDBY
        elif pFSM.current_state == State.STANDBY:
            pFSM.current_state = State.AGENDAMENTO
        elif pFSM.current_state == State.AGENDAMENTO:
            if event == Event.AGENDAR:
                pFSM.current_state = State.PAYLOAD
            else:
                pFSM.current_state = State.MONITORAR
        elif pFSM.current_state == State.PAYLOAD:
            pFSM.current_state = State.MONITORAR
        elif pFSM.current_state == State.MONITORAR:
            pFSM.current_state = State.SEND_MSG
        elif pFSM.current_state == State.SEND_MSG:
            pFSM.current_state = State.STANDBY
            

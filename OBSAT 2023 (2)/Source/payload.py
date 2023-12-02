from rtlsdr import RtlSdr

list_of_freq = [70e6, 80e6] #etc...

class Payload_SDR():
    SAMPLE_RATE = 2.048e6
    CENTER_FREQ = list_of_freq[0]
    FREQ_CORRECTION = 60
    GAIN = 'auto'

    def __init__(self):
        sdr = RtlSdr()
        Payload_SDR.sdr.sample_rate = Payload_SDR.SAMPLE_RATE
        Payload_SDR.sdr.center_freq = Payload_SDR.sdr.freq_correction = Payload_SDR.FREQ_CORRECTION
        Payload_SDR.sdr.gain = Payload_SDR.GAIN

    def read_samples(self):
        samples = Payload_SDR.sdr.read_samples(512)
        return (samples)

    def close_payload(self):
        Payload_SDR.sdr.close()
        #apenas limitei o acesso ao metodo

    def save_samples(self):
        pass

# configure device

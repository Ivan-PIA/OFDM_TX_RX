from context import *
import time
from scipy.io import loadmat

N_fft = 128
GB_len = 55
CP = 32
N_pilot = 6

FILE = 1

if FILE == 1:
    path = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_tx\\tx_file.py"
if FILE == 2:   
    path = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_tx\\tx.jpg"
if FILE == 3:
    path = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_tx\\tx1.jpg"

bits = converted_file_to_bits(path)

len_packet = len(bits)
print("len_bit_tx: ", len_packet)

QAM = QPSK(bits)

ofdm = modulation(N_fft, CP,GB_len, QAM, N_pilot, amplitude_all= 2**14, amplitude_data=1, amplitude_pss = 1, amplitude_pilots = 1)

print("len_ofdm ",len(ofdm))

#resource_grid_3(ofdm, N_fft, CP)


sdr2 = standart_settings("ip:192.168.3.1", 1.920e6, 1.92e3*2)

tx_signal(sdr2,1900e6,0,ofdm)
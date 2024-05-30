from context import *
import numpy as np
import matplotlib.pyplot as plt


N_fft = 128
GB_len = 55
CP = 32
N_pilot = 6

FILE = 3

if FILE == 1:
    path = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_tx\\tx_file.py"
if FILE == 2:   
    path = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_tx\\imag_tx.jpg"
if FILE == 3:
    path = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_tx\\tx1.jpg"

bits = converted_file_to_bits(path)

len_packet = len(bits)
print("len_bit_tx: ", len_packet)

QAM = QPSK(bits)

ofdm = modulation(N_fft, CP,GB_len, QAM, N_pilot, amplitude_all= 2**14, amplitude_data=1, amplitude_pss = 1, amplitude_pilots = 1)
resource_grid_3(ofdm, N_fft, CP)

ofdm = ofdm[(N_fft + CP):]

data1 = ofdm[:(N_fft+CP) * 5 + CP]

print(len(data1))

count_slots = get_inform_slot_bit10(data1, N_fft, N_pilot, GB_len, 2, CP)

print("count slot= ", count_slots)

ofdm2 = ofdm[:((960*count_slots))]

ofdm2 = del_pss_in_frame(ofdm2, N_fft,CP)

slots, broken_slot = decode_slots_bit10(ofdm2, N_fft, CP, GB_len,count_slots,N_pilot)
print(broken_slot)
bits = slots

print("len_bit_rx: ", len(bits))

if FILE == 1:   
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\rx_file.py"
if FILE == 2:
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\imag_rx.jpg"
if FILE == 3:
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\rx.jpg"



converted_bits_to_file(bits, path_final_file)
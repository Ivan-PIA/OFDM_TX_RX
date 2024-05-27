from context import *
import time
from scipy.io import loadmat

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

print("len_ofdm ",len(ofdm))

#resource_grid_3(ofdm, N_fft, CP)

sdr  = standart_settings("ip:192.168.2.1", 1.920e6, len(ofdm)*3)
sdr2 = standart_settings("ip:192.168.3.1", 1.920e6, len(ofdm)*3)

tx_signal(sdr2,1900e6,0,ofdm)

start = time.time()
rx = rx_signal(sdr,1900e6,20,1)

#print("len_rx: ",len(rx), rx[:10])

#resource_grid(rx,10,6,N_fft, CP)

data = corr_pss_time(rx,N_fft)

#resource_grid(data,10,6,N_fft, CP)

data_cor = calculate_correlation(N_fft, data, 15000) #

#resource_grid(data_cor,10,6,N_fft, CP)

data1 = data_cor[:(N_fft+CP) * 5 + CP]

count_slots = get_inform_slot_bit10(data1, N_fft, N_pilot, GB_len, 2, CP)

print("count slot= ", count_slots)

ofdm2 = data_cor[:((960*count_slots))+800]

ofdm2 = del_pss_in_frame(ofdm2, N_fft,CP)

#resource_grid_3(ofdm2, N_fft,CP)

slots, broken_slot = decode_slots_bit10(ofdm2, N_fft, CP, GB_len,count_slots,N_pilot)
bits = slots[:len_packet]

print("len_bit_rx: ", len(bits))


if FILE == 1:   
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\rx_file.py"
if FILE == 2:
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\imag_rx.jpg"
if FILE == 3:
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\rx.jpg"


converted_bits_to_file(bits, path_final_file)
end = time.time() - start
print("Время передачи", end)
print("бит: ", len_packet)
print("Поврежденные слоты: ", broken_slot)
print("end")
plt.show()
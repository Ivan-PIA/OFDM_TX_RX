from context import *
import time


N_fft = 128
GB_len = 55
CP = 32
N_pilot = 6

FILE = 1



sdr  = standart_settings("ip:192.168.2.1", 1.920e6,  1.920e3*2)

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
bits = slots

if FILE == 1:   
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\rx_file.py"
if FILE == 2:
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\imag_rx.jpg"
if FILE == 3:
    path_final_file = "C:\\Users\\Ivan\\Desktop\\lerning\\OFDM\\OFDM_TX_RX\\test\\resurs_rx\\rx.jpg"


converted_bits_to_file(bits, path_final_file)
end = time.time() - start

print("Время передачи", end)
print("бит: ",  len(bits))
print("Поврежденные слоты: ", broken_slot)
print("end")
plt.show()
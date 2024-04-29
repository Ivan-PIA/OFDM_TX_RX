from context import *

from scipy.io import loadmat

N_fft = 128
GB_len = 55
CP = 32
N_pilot = 6

path = "OFDM_TX_RX\\test\\tx_file.py"

bits = converted_file_to_bits(path)
len_packet = len(bits)
QAM = QPSK(bits)


ofdm = modulation(N_fft, CP,GB_len, QAM, N_pilot, amplitude_all= 2**14, amplitude_data=1, amplitude_pss = 1, amplitude_pilots = 1)

resource_grid_3(ofdm, N_fft, CP)

sdr = standart_settings("ip:192.168.2.1", 1.920e6, 50e3)
sdr2 = standart_settings("ip:192.168.3.1", 1.920e6, 50e3)

tx_signal(sdr,1900e6,0,ofdm)
rx = rx_signal(sdr2,1900e6,20,2)

#resource_grid(rx,10,6,N_fft, CP)

data = corr_pss_time(rx,N_fft)

data_cor = calculate_correlation(N_fft, data, 15000) # 

resource_grid(data_cor,10,6,N_fft, CP)

data1 = data_cor[:(N_fft+CP) * 5 + CP]

count_slots = get_inform_slot(data1, N_fft, N_pilot, GB_len, 2, CP)

ofdm2 = data_cor[:((960*count_slots))+800]

ofdm2 = del_pss_in_frame(ofdm2, N_fft,CP)

resource_grid_3(ofdm2, N_fft,CP)

slots = decode_slots(ofdm2, N_fft, CP, GB_len,count_slots,N_pilot)
slots = slots[:len_packet]

path_final_file = "OFDM_TX_RX\\test\\rx.py"

converted_bits_to_file(slots, path_final_file)
print("end")
plt.show()
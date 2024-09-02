from context import *
import matplotlib.animation as animation



count_zero = 0
colm = 180 + count_zero
rows = 130
gain_rx = 30


def form_ofdm(data_mat):
    
    zeros = np.zeros(count_zero)
    data_ofdm = np.zeros(0)

    for i in range(len(data_mat)):
        data_and_zero = np.concatenate([zeros, data_mat[i], zeros])
        data_ifft = np.fft.ifft(data_and_zero)
        data_ofdm = np.concatenate([data_ofdm, data_ifft])

    return data_ofdm




data = np.array((   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],#18/13    ofdm = 32/11   SDR
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 5, 5, 5, 1, 5, 5, 5, 1, 1, 5, 5, 5, 1, 1, 1],
                    [1, 1, 5, 1, 1, 1, 1, 5, 1, 1, 5, 1, 5, 1, 1, 5, 1, 1],
                    [1, 1, 5, 1, 1, 1, 1, 5, 1, 1, 5, 1, 5, 1, 1, 5, 1, 1],
                    [1, 1, 1, 5, 5, 1, 1, 5, 1, 1, 5, 1, 5, 5, 5, 1, 1, 1],
                    [1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 5, 1, 5, 1, 5, 1, 1, 1],
                    [1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 5, 1, 5, 1, 1, 5, 1, 1],
                    [1, 1, 5, 5, 5, 1, 1, 5, 5, 5, 1, 1, 5, 1, 1, 5, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


# data = np.array((   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],#12/13    ofdm = 32/11 zont
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1],
#                     [1, 1, 1, 5, 5, 5, 5, 5, 5, 1, 1, 1],
#                     [1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 5, 1, 5, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))



# data = np.array((   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],#12/13    ofdm = 32/11 rocket
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 10, 10, 10, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 10, 10, 10, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 10, 10, 10, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 10, 10, 10, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 10, 10, 10, 1, 1, 1, 1],
#                     [1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 1, 1],
#                     [1, 1, 1, 10, 10, 10, 1,  10, 10, 10, 1, 1],
#                     [1, 1, 1, 10, 10, 10, 1,  10, 10, 10, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],))


data = data.repeat(10, axis=0).repeat(10, axis=1)

data[data == 1] = 0

data = data * 2**12

data_ofdm = form_ofdm(data)
# zeros = np.zeros(55)
print(len(data_ofdm))

# data = np.concatenate([zeros,data,zeros])


# data_ofdm = data_ofdm.reshape(rows,colm)

# data = np.fft.fft(data_ofdm)

#plt.imshow(abs(data), cmap='jet',interpolation='nearest', aspect='auto')



# data = data.flatten()
#data_ofdm = np.fft.ifft(data)


sdr  = standart_settings("ip:192.168.3.1", 1e6, len(data_ofdm) * 1)
sdr2 = standart_settings("ip:192.168.2.1", 1e6, len(data_ofdm) * 1)




tx_signal(sdr,1900e6,0,data_ofdm)
rx = rx_signal(sdr2,1900e6,gain_rx,1)

rx = rx[:rows*colm]
# plt.plot(abs(np.fft.fft(rx)))

rx = rx.reshape(rows,colm)

rx = np.fft.fft(rx)




fig, ax = plt.subplots()
heatmap = ax.imshow(abs(rx), cmap='jet',interpolation='nearest', aspect='auto')

def update(frame):
    rx = rx_signal(sdr2,1900e6,gain_rx,1)
    # rx = calculate_correlation(120, rx, 1e6/120) 
    rx = rx[:rows*colm]
    
    rx = rx.reshape(rows,colm)

    rx = np.fft.fft(rx)

    heatmap.set_array(abs(rx))
    return [heatmap]



ani = animation.FuncAnimation(fig, update, frames=100, interval=80)

plt.show()
# OFDM_TX_RX

## Проктокол передачи данных через SDR

- Программа написана под плату Adalm-Pluto SDR. Позволяет передать файл, текст, изображение по радиоканалу. Используется технология цифровой модуляции OFDM.


### Для начала работы


#### Windows:

Для работы с SDR: 

1. [**libiio**](https://github.com/analogdevicesinc/libiio/releases), кроссплатформенная библиотека взаимодействия с интерфейсами “железа”;

2. [**libad9361-iio**](https://github.com/analogdevicesinc/libad9361-iio/releases), AD9361 - RF-чип внутри PlutoSDR;

3. [**PlutoSDR-M2k-USB-Drivers.exe**](https://github.com/analogdevicesinc/plutosdr-m2k-drivers-win/releases)

4. **pyadi-iio**, библиотека Python API для взаимодействия с PlutoSDR. С ней мы и будет взаимодействовать напрямую при помощи Python. (pip install pyadi-iio)

Для корректной работы программы:

**pip install matplotlib**

**pip install numpy**

#### Linux:

```sh
sudo apt-get install build-essential git libxml2-dev bison flex libcdk5-dev cmake python3-pip libusb-1.0-0-dev libavahi-client-dev libavahi-common-dev libaio-dev
cd ~
git clone --branch v0.23 https://github.com/analogdevicesinc/libiio.git
cd libiio
mkdir build
cd build
cmake -DPYTHON_BINDINGS=ON ..
make -j$(nproc)
sudo make install
sudo ldconfig

cd ~
git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install

cd ~
git clone --branch v0.0.14 https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip3 install --upgrade pip
pip3 install -r requirements.txt
sudo python3 setup.py install
```

Далее для любой их ОС склонировать репозиторий 

```sh
git clone https://github.com/Ivan-PIA/OFDM_TX_RX.git
```

и запустить *ofdm_tx_rx.py* в папке test


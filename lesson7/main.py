import serial
import time

ser = serial.Serial()
ser.port = "COM5"  # 根據你的COM port進行調整
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = 0.5
ser.writeTimeout = 0.5
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False

try:
    ser.open()
except Exception as ex:
    print("open serial port error " + str(ex))
    exit()

if ser.isOpen():
    try:
        ser.flushInput()  # 清空輸入緩衝區
        ser.flushOutput()  # 清空輸出緩衝區
        # 寫入8個byte數據
        ser.write([78, 78, 78, 78, 78, 78, 78, 78])
        print("write 8 byte data: 78, 78, 78, 78, 78, 78, 78, 78")
        time.sleep(0.5)  # 等待0.5秒
        # 讀取8個byte數據
        response = ser.read(8)
        print("read 8 byte data:")
        print(response)
        ser.close()
    except Exception as e1:
        print("communicating error " + str(e1))
else:
    print("open serial port error")
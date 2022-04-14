import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

maxVoltage = 3.3
troyka = 17
comp = 4

dac = [26,19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(i):
    return [int(elem) for elem in bin(i)[2:].zfill(8)]

def bin2dac(i): #lights leds
    signal = decimal2binary(i)
    GPIO.output(dac, signal)    
    return signal

def adc(i, value):
    if i == -1:
        return value
    bin2dac(value + 2**i)
    time.sleep(0.01)
    compVAL = GPIO.input(comp)
    if compVAL == 0:
        return adc(i - 1, value)
    else:
        return adc(i - 1, value + 2**i)



#measured_data = [1, 2, 3, 4, 5, 10]
#plt.plot(measured_data)
#plt.show()


#measured_data_str = [str(item) for item in measured_data]
##print(measured_data, measured_data_str)
#
##with open("data.txt", "w") as outfile:
##    outfile.write("\n".join(measured_data_str))


try:
    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
    list = []
    start_of_time = time.clock()
    mode_of_measure = 1
    while True:
        tmp_bin_volt = adc(7, 0)
        list.append(tmp_bin_volt)
        print("цифровое значение =")
        print(tmp_bin_volt)
        print("напряжение")
        valToPr = tmp_bin_volt / 2**8 * 3.3
        print(valToPr)
        if tmp_bin_volt >= 0.95 * (2**8 - 1) and mode_of_measure == 1:
            GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
            mode_of_measure = 0

        if tmp_bin_volt <= 0.05 * (2**8 - 1) and mode_of_measure == 0:
            break
    
    end_of_time = time.clock()

    lab_time = end_of_time - start_of_time;
        

    plt.plot(list)
    plt.show()


    strdac = [str(item) for item in list]
    with open("data.txt", "w") as outfile:
            outfile.write("\n".join(strdac))

    with open("src.txt", "w") as f:
            f.write(str(lab_time))



finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)

#!/usr/bin/python

import time
import serial
import matplotlib.pyplot as plt
import pickle

update_interval = 1

ser = serial.Serial(
 port = '/dev/ttyUSB0',
 baudrate = 9600,
 )


time.sleep(1.5)
ser.flush()

r = 0
r_time = 0
analog_reads = [];
analog_times = [];
pickle.dump(analog_reads, open("../logfiles/analog_reads.log","wb"))
pickle.dump(analog_times, open("../logfiles/analog_times.log","wb"))
while len(analog_times) >= 0:
	time.sleep(5)
	val = ser.readline() #read 5 bytes
	val = val.replace("\n","")
	if len(val) == 5:
		r = val
		analog_reads = pickle.load(open("analog_reads.log","rb"))
		analog_reads.append(r)
		#print analog_reads
		pickle.dump(analog_reads, open("analog_reads.log","wb"))
		analog_times = pickle.load(open("analog_times.log","rb"))
		analog_times.append(r_time)
		pickle.dump(analog_times, open("analog_times.log","wb"))
		#print analog_times
		plt.plot(analog_times, analog_reads)
		#plt.show()
		plt.savefig('../logfiles/tempkurve.png')
		r_time = r_time + update_interval



# -*-coding:utf-8-*-
import socket
import time
import uuid 
import datetime

HOST = "37.50.200.7"
HOST = "MYHOST"
PORT = 5005
PORT = MYPORT
PROTOCOL = "UDP"
PROTOCOL = "MYPROTOCOL"
DELAY = 5
DELAY = MYDELAY
BytesRamdomLength = 200
BytesRamdomLength = MYRANDOMLENGTH

#first 4 bytes (here 0027) are the DELAY in hex encoded (0027 means 39 seconds)
#calculate from number "DELAY" a HEX value and fill it up to 4 digits (Stellen)
DELAY_hex = hex(DELAY)
DELAY_hex_4 = '%0*x' % (4,int(DELAY_hex, 16))

#generate a random hexstring in length of BytesRamdomLength
myrandom = uuid.uuid4().hex.upper()[0:BytesRamdomLength]

#concatenate the delay value in hex and the random string and transcode it into byte string
PAYLOAD = (str(DELAY_hex_4) + str(myrandom))
PAYLOAD = bytes(PAYLOAD, encoding='utf8')

if "UDP" in PROTOCOL:
    print("Doing UDP Test")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Delay in dezimal is: ' + str(DELAY))
    print('Delay in hex is: ' + str(DELAY_hex))
    print('Delay in hex 4 bytest is: ' + str(DELAY_hex_4))
    print('Random Length is: ' + str(BytesRamdomLength))
    print('Random string is: ' + str(myrandom))
    print('Payload is: ' + str(PAYLOAD))
    print('Client started')
    print('Client sending to IP: ' + str(HOST))
    print('Client sending to port: ' + str(PORT))
    dateTimeObj = int(time.time())*1000
    dateTimeObjHumanReadable = datetime.datetime.now()
    print("### Message send: " + str(dateTimeObj))
    print("### Message sendtime: " + str(dateTimeObjHumanReadable))
    s.sendto(PAYLOAD, (HOST, PORT))
    data = s.recvfrom(4096)
    dateTimeObj = int(time.time())*1000
    dateTimeObjHumanReadable = datetime.datetime.now()
    print("### Message received: " + str(dateTimeObj))
    print("### Message receivetime: " + str(dateTimeObjHumanReadable))
    s.close()

if "TCP" in PROTOCOL:
    print("Doing TCP Test")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Delay in dezimal is: ' + str(DELAY))
    print('Delay in hex is: ' + str(DELAY_hex))
    print('Delay in hex 4 bytest is: ' + str(DELAY_hex_4))
    print('Random Length is: ' + str(BytesRamdomLength))
    print('Random string is: ' + str(myrandom))
    print('Payload is: ' + str(PAYLOAD))
    print('Client started')
    print('Client sending to IP: ' + str(HOST))
    print('Client sending to port: ' + str(PORT))
    s.connect((HOST, PORT))
    dateTimeObj = int(time.time())*1000
    dateTimeObjHumanReadable = datetime.datetime.now()
    print("### Message send: " + str(dateTimeObj))
    print("### Message sendtime: " + str(dateTimeObjHumanReadable))
    s.sendall(PAYLOAD)
    data = s.recv(4096)
    dateTimeObj = int(time.time())*1000
    dateTimeObjHumanReadable = datetime.datetime.now()
    print("### Message received: " + str(dateTimeObj))
    print("### Message receivetime: " + str(dateTimeObjHumanReadable))
    s.close()

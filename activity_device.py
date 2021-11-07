#!/usr/bin/python3

# imports
from kafka import KafkaProducer , KafkaClient # pip install kafka-python
import numpy as np              # pip install numpy
from random import randint
from sys import argv, exit
from time import time, sleep
import json

# different device "profiles" with different 
# distributions of values to make things interesting
DEVICE_PROFILES = {
	"iwatch": {'device_id': (10000, 1000000), 'steps': (0, 100), 'workout': (0, 3), 'heartbeat': (50, 200) },
	"galaxy": {'device_id': (1000001, 2000000), 'steps': (0, 100), 'workout': (0, 3), 'heartbeat': (50, 200) },
	"fitbit": {'device_id': (2000001, 3000000), 'steps': (0, 100), 'workout': (0, 3), 'heartbeat': (50, 200) }
}

# check for arguments, exit if wrong
if len(argv) != 2 or argv[1] not in DEVICE_PROFILES.keys():
	print("please provide a valid device name:")
	for key in DEVICE_PROFILES.keys():
		print(f"  * {key}")
	print(f"\nformat: {argv[0]} DEVICE_NAME")
	exit(1)

profile_name = argv[1]
profile = DEVICE_PROFILES[profile_name]

# set up the producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

count = 1

# until control-C is pressed
while True:
	# get random values within a normal distribution of the value
	device_id = randint(profile['device_id'][0], profile['device_id'][1])
	steps = randint(profile['steps'][0], profile['steps'][1])
	workout = randint(profile['workout'][0], profile['workout'][1])
	heartbeat = randint(profile['heartbeat'][0], profile['heartbeat'][1])
	
	# create json structure
	msg = {"device_time":time(),"device_id":device_id,"profile_name":profile_name,"steps": steps,"workout": workout,"heartbeat":heartbeat}

	# send json data to Kafka
	print(msg)
	producer.send('fitness', json.dumps(msg).encode('utf-8'))
	print(f'sending data to kafka, #{count}')

	count += 1
	sleep(2)
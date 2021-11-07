#!/usr/bin/python3

# imports
from kafka import KafkaProducer # pip install kafka-python
import numpy as np              # pip install numpy
from random import randint
from sys import argv, exit
from time import time, sleep

# different device "profiles" with different 
# distributions of values to make things interesting
# tuple --> (mean, std.dev)
DEVICE_PROFILES = {
	"iwatch": {'steps': (0, 50000), 'workout': (0, 1440), 'heartbeat': (50, 200) },
	"galaxy": {'steps': (0, 50000), 'workout': (0, 1440), 'heartbeat': (50, 200) },
	"fitbit": {'steps': (0, 50000), 'workout': (0, 1440), 'heartbeat': (50, 200) }
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

# until ^C
while True:
	# get random values within a normal distribution of the value
	steps = randint(profile['steps'][0], profile['steps'][1])
	workout = randint(profile['workout'][0], profile['workout'][1])
	heartbeat = randint(profile['heartbeat'][0], profile['heartbeat'][1])
	
	# create CSV structure
	msg = f'{time()},{profile_name},{steps},{workout},{heartbeat}'

	# send to Kafka
	producer.send('fitness', bytes(msg, encoding='utf8'))
	print(f'sending data to kafka, #{count}')

	count += 1
	sleep(.5)
# pyspark-structured-streaming
Project to run structured streaming using kafka and pyspark. The producer generates random health and fitness data from three iot devices and sends it to kafka.
The application then receives the data in real time and aggregates the average heartbeat and total steps per device type and displays it on the console in real time. 

Prerequisites:
- Kafka

Preparation:
- Start kafka zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

- Start kafka broker
bin/kafka-server-start.sh config/server.properties

- Create the kafka topic
bin/kafka-topics.sh --create --topic fitness --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

- Run the pyspark application
PIPENV_VENV_IN_PROJECT=1 pipenv shell

- Build and start the application
make build
make run

- Run the KafkaProducer
python3 iot_devices.py <device_name>

# pyspark-structured-streaming
Project to run structured streaming using kafka and pyspark

Prerequisites:
- Kafka should be installed
- Pyspark should be installed


Preparation:
- Create the kafka topic
bin/kafka-topics.sh --create --topic fitness --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

- Run the consumer
bin/kafka-console-consumer.sh --topic fitness --from-beginning --bootstrap-server localhost:9092

- Run the KafkaProducer
python3 iot_devices.py <device_name>
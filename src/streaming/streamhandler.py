from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType
from pyspark.sql.functions import col,from_json, avg, sum

class StreamHandler():
    #Class for doing processing on kafka streaming data
    @staticmethod
    def process_stream(spark: SparkSession):

        print('Streaming data Processing')

        # read from Kafka
        inputDF = spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("subscribe", "fitness") \
            .load() \
        
        #inputDF.printSchema()
        sc=spark.sparkContext

        rawDF = inputDF.selectExpr("CAST(value AS STRING)")

        schema=StructType([
            StructField("device_time", StringType(), True),
            StructField("device_id", StringType(), True),
            StructField("profile_name", StringType(), True),
            StructField("steps", StringType(), True),
            StructField("workout", StringType(), True),
            StructField("heartbeat", StringType(), True)
        ])

        #explode the json data in value field to the above schema's structure
        newDF = rawDF.withColumn("jsonData",from_json(col("value"),schema)) \
                   .select("jsonData.*")

        rawjsonDF = newDF \
            .writeStream \
            .format("console") \
            .option("truncate","false") \
            .queryName("fitness_raw_data") \
            .trigger(processingTime='10 seconds') \
            .start()

        summaryDF = newDF.groupBy("profile_name") \
                .agg(avg("heartbeat").alias("average_heartbeat"), \
                sum("steps").alias("total_steps") \
                )

        outputDF = summaryDF \
            .writeStream \
            .format("console") \
            .outputMode("complete") \
            .option("checkpointLocation", "checkpoints") \
            .option("truncate","false") \
            .queryName("fitness_aggregation_data") \
            .trigger(processingTime='10 seconds') \
            .start()
        
        outputDF.awaitTermination()

import os
import sys
from streaming.streamhandler import StreamHandler
from pyspark.sql import SparkSession
print(f'Python version is {sys.version}')

if os.path.exists('src.zip'):
    sys.path.insert(0, 'src.zip')
else:
    sys.path.insert(0, './src')

if __name__=='__main__':
    spark = SparkSession \
    .builder \
    .appName("Pyspark Streaming example") \
    .getOrCreate()
    
    print('Calling function to process kafka stream')
    sh=StreamHandler()     #Passing Sparksession to the class
    sh.process_stream(spark)
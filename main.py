import os
import sys
import pyspark

print(f'Python version is {sys.version}')


if os.path.exists('src.zip'):
    sys.path.insert(0, 'src.zip')
else:
    sys.path.insert(0, './src')

if __name__=='__main__':
    from pyspark.sql import SparkSession
    spark = SparkSession \
    .builder \
    .appName("Pyspark Streaming example") \
    .getOrCreate()
    
    print('Inside main')
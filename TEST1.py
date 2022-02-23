from pyspark import SparkContext
from pyspark import SparkConf

# create Spark context with Spark configuration
conf = SparkConf().setAppName("read text file in pyspark")
sc = SparkContext(conf=conf)

# Read file into RDD
lines = sc.textFile("file:///home/ds503/shared_folder/data.txt")
print('reached')
lines.collect()
print('abcd')
# execute:  bash run.sh

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("hello_spark_adolfo")\
        .getOrCreate()

    print("Hello spark world, welcome Adolfo ... ")

    spark.stop()

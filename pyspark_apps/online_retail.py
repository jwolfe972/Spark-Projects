import pyspark
from ucimlrepo import fetch_ucirepo 
from pyspark.sql import SparkSession
import os


if __name__ == "__main__":
    # fetch dataset  https://archive.ics.uci.edu/dataset/352/online+retail
    online_retail = fetch_ucirepo(id=352) 
    
    # data (as pandas dataframes) 
    X = online_retail.data.features 
    y = online_retail.data.targets 
    
    # metadata 
    print(online_retail.metadata) 
    
    # variable information 
    print(online_retail.variables)

    # conf = spark.SparkConf().setAppName('MyApp').setMaster('spark://127.0.0.1:7077')
    # sc = spark.SparkContext(conf=conf)

    spark = (SparkSession.builder.appName("online_retail")
                .master('spark://127.0.0.1:7077')
             .getOrCreate())

    spark_df = spark.createDataFrame(X)

    spark_df.show()

    spark.stop()







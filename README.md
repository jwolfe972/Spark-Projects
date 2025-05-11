# Spark-Projects

## This will be a repo of a set of Spark Projects I work on to get more familiar using Spark. I will be using both Pyspark and RSpark



## How to get Started
#### To get started run the following commands:
#### Create a virtual environment
```
python -m venv spark-venv
```
#### Activate the virtual environment and install the libraries
```
source spark-venv/bin/activate
pip install -r requirements.txt

```
#### Start the Spark Containers w/ Sample Iceberg Spark Containers from here [Databricks Spark Iceberg Repository](https://github.com/databricks/docker-spark-iceberg)

```
docker compose up -d
```

#### Start the Jupyter Notebook Server with this command
```
jupyter notebook
```

#### Code to connect to the Spark Cluster
```python


from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Jupyter").getOrCreate()

spark
```
""""
This module is going to write data back to mysql database
"""
from pyspark.sql import SparkSession

#MySQL Connection details
MYSQL_JDBC_DRIVER = "com.mysql.cj.jdbc.Driver"
MYSQL_SERVER = "127.0.0.1"
MYSQL_DBNAME = ""
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = ""

URL = f"jdbc:mysql://{MYSQL_SERVER}/{MYSQL_DBNAME}"

#Table details
TABLE_EMPLOYEE = "employee"

def write_to_mysql(_df):

    """ 
    This method is to write data back to mysql
    """

    _df.write \
        .format("jdbc") \
        .option("driver", MYSQL_JDBC_DRIVER) \
        .option("url", URL) \
        .option("dbtable", "Employees") \
        .option("user", MYSQL_USERNAME) \
        .option("password", MYSQL_PASSWORD) \
        .save()

def read_from_mysql(_spark):
    """
    This method is going to read data from mysql database
    """
    return _spark.read \
        .format("jdbc") \
        .option("driver", MYSQL_JDBC_DRIVER) \
        .option("url", URL) \
        .option("dbtable", TABLE_EMPLOYEE) \
        .option("user", MYSQL_USERNAME) \
        .option("password", MYSQL_PASSWORD) \
        .load()

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("mysql demo") \
        .getOrCreate()
    
    df_employees = spark.read \
        .json(r"C:\spark-3.5.1-bin-hadoop3\examples\src\main\resources\employees.json")
    df_employees.show()

    df_emps = read_from_mysql(spark)
    df_emps.show()
    df_emps.printSchema()



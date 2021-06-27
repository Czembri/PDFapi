from Application.config import db_config
import mysql.connector



mydb = mysql.connector.connect(user=db_config["login"], password=db_config["password"],
                              host=db_config["url"], database=db_config["database"])

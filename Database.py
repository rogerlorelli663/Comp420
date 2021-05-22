import logging
import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = database
        self.__database = None
        self.__cursor = None
        self.__connect()

    def __connect(self):
        self.__database = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            passwd=self.__password,
            database=self.__db
        )
        self.__cursor = self.__database.cursor()

    def execute(self, sql_command):
        try:
            self.__cursor.execute(sql_command)
            self.__database.commit()
            return self.__cursor.fetchall()
        except:
            self.__database.rollback()
            logging.error(f"Could not resolve sql command {sql_command}")
            return None

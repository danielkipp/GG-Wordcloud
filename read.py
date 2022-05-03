import datetime
import psycopg2
import requests
from config import config


def getWords(competitorID):

    words = ""

    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # Read PostgreSQL purchase timestamp value into Python datetime
        sql = "SELECT title FROM ft_newsletter WHERE ft_newsletter.competitor_id ='" + competitorID + "'"
        cursor.execute(sql)
        sqlResult = cursor.fetchall()

        #print("Print each row and it's columns values")
        for row in sqlResult:
            words = words + " " + row[0]


        return words

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        # TODO: define specific exception
        raise Exception("Could not pull competitors from DB.")

    finally:
        if connection:
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")




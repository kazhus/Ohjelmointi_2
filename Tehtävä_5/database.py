import mysql.connector
def y():
    conncetor= mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        database="flight_game",
        user="root",
        password="paaswOrd",
        autocommit=True
    )
    return conncetor
def haeICAO (koodi):
    conncection = y()

icao = input("Anna Icao: ")
haeICAO(icao)
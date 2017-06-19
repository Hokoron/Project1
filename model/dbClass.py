class dbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "password",
            "db": "enmdatabase"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def saveinfo(self, username, password, weelradios):
        sqlQuery = "INSERT INTO registreren (username, password, weelradius) VALUES ('{param1}','{param2}','{param3}')"
        sqlCommand = sqlQuery.format(param1=username, param2=password, param3=weelradios)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getinfo(self, username):
        query = "SELECT password FROM registreren where username = '" + username + "'"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getuser(self, username):
        query = "SELECT username FROM registreren where username = '" + username + "'"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def changepass(self, username, password):
        sqlQuery = "update registreren set password = '{param1}' where username = '{param2}'"
        sqlCommand = sqlQuery.format(param1= password, param2= username)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def changename(self, username, username_new):
        sqlQuery = "update registreren set username = '{param1}' where username = '{param2}'"
        sqlCommand = sqlQuery.format(param1= username_new, param2= username)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def changeweel(self, username, weel):
        sqlQuery = "update registreren set weelradius = '{param1}' where username = '{param2}'"
        sqlCommand = sqlQuery.format(param1=weel, param2=username)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def getdate(self):
        query = "SELECT datum FROM kilometerTeller"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getafstand(self):
        query = "SELECT afstand FROM kilometerTeller"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getdodetijd(self):
        query = "SELECT gepauzeerdetijd FROM kilometerTeller"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getgeredetijd(self):
        query = "SELECT geredentijd FROM kilometerTeller"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getcollection(self, gegevenDatum):
        query = "SELECT * FROM kilometerTeller WHERE datum ='" + gegevenDatum + "'"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result

    def make_new_day(self, datum, afstand, geredentijd, gepauzeerdetijd, gemideldesnelheid):
        sqlQuery = "INSERT INTO kilometerTeller (datum, afstand, geredentijd, gepauzeerdetijd, gemideldesnelheid) VALUES ('{param1}','{param2}','{param3}','{param4}','{param5}')"
        sqlCommand = sqlQuery.format(param1= datum, param2=afstand, param3=geredentijd, param4=gepauzeerdetijd, param5=gemideldesnelheid)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()

    def updatekilometer(self, date ,afstand, geredentijd, gepauzeerdetijd, gemideldesnelheid):
        sqlQuery = "update kilometerTeller set afstand = '{param2}', geredentijd = '{param3}',gepauzeerdetijd = '{param4}',gemideldesnelheid = '{param5}'  where datum = '{param1}'"
        sqlCommand = sqlQuery.format(param1=date, param2=afstand, param3=geredentijd, param4=gepauzeerdetijd, param5=gemideldesnelheid)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()

    def getweel(self, parameter):
        query = "SELECT weelradius FROM registreren WHERE id = '{param1}'"
        sqlCommand = query.format(param1 = parameter)
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result
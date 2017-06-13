class DbClass:
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

    def getcollection(self, gegevenDatum):
        query = "SELECT * FROM kilometerTeller WHERE datum ='" + gegevenDatum + "'"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        self.__cursor.close()
        return result


    def make_new_day(self,datum,afstand,geredentijd,gepauzeerdetijd,gemideldesnelheid):
        query = "insert into kilometerTeller(persoonID, datum, afstand ,geredentijd,gepauzeerdetijd,gemideldesnelheid) VALUES('" + str(0) + ',' + datum + ',' + str(afstand) + ',' + str(geredentijd) + ',' + str(gepauzeerdetijd) + ',' + gemideldesnelheid + "')"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()

        self.__cursor.close()
        return result


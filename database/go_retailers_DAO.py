from database import DB_connect
from model import product
from model.retailers import Retailers


class Retailers_DAO:
    def get_retailers(self):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM go_retailers"""

        cursor.execute(query)
        tabella = []
        for i in cursor:
            tabella.append(Retailers(i[0], i[1], i[2], i[3]))
        cursor.close()
        cnx.close()
        return tabella
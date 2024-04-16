from database import DB_connect
from model import product
from model.method import Method



class Method_DAO:
    def get_methods(self):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM go_methods"""

        cursor.execute(query)
        tabella = []
        for i in cursor:
            tabella.append(Method(i[0], i[1]))
        cursor.close()
        cnx.close()
        return tabella
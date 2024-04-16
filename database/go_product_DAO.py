from database import DB_connect
from model import product
from model.product import Product


class Product_DAO:
    def get_product(self):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM go_products"""

        cursor.execute(query)
        tabella = []
        for i in cursor:
            tabella.append(Product(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        cursor.close()
        cnx.close()
        return tabella


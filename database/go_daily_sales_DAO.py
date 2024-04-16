from database import DB_connect, go_retailers_DAO, go_method_DAO, go_product_DAO
import model
from model.daily_sales import Daily_sales


class Daily_sales_DAO:
    def get_daily_sales(self):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT *
                    FROM go_daily_sales"""

        cursor.execute(query)
        tabella=[]
        tabella_retailers = go_retailers_DAO.Retailers_DAO().get_retailers()
        tabella_products = go_product_DAO.Product_DAO().get_product()
        tabella_methods = go_method_DAO.Method_DAO().get_methods()


        for sale in cursor:
            retailer = None
            product = None
            method = None

            for a in tabella_retailers:
                if a.retailer_code == sale[0]:
                    retailer = a
            for b in tabella_products:
                if b.product_number == sale[1]:
                    product = b
            for c in tabella_methods:
                if c.code==sale[2]:
                    method = c
            tabella.append(Daily_sales(retailer, product, method, sale[3], sale[4], sale[5], sale[6]))


        cursor.close()
        cnx.close()
        return tabella

    def get_anno(self):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT YEAR(Date)
                    FROM go_daily_sales"""
        cursor.execute(query)
        tabella = []
        for i in cursor:
            if i not in tabella:
                tabella.append(i)
        cursor.close()
        cnx.close()
        return tabella





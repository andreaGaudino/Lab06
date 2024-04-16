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
        query = """SELECT YEAR(Date), Date
                    FROM go_daily_sales"""
        cursor.execute(query)
        tabella = []
        for i in cursor:
            if i not in tabella:
                tabella.append(i)
        cursor.close()
        cnx.close()
        return tabella

    def get_migliori(self, anno, brand, retailer):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT  gds.Date,sum(gds.Quantity*gds.Unit_sale_price) as Ricavo, gr.Retailer_code, gp.Product_number
                    FROM go_sales.go_daily_sales AS gds 
                    INNER JOIN go_sales.go_products AS gp
                    ON gds.Product_number = gp.Product_number
                    inner join go_sales.go_retailers gr 
                    on gds.Retailer_code = gr.Retailer_code 
                    WHERE  gds.Retailer_code = %s and year(gds.Date)= %s and gp.Product_brand = %s
                    group by gds.`Date` 
                    order by Ricavo desc 
                    limit 5
                    """
        cursor.execute(query, (anno, brand, retailer))
        tabella = []
        for i in cursor:
            tabella.append([i[0], i[1], i[2], i[3]])
        cursor.close()
        cnx.close()
        return tabella





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
            if i[0] not in tabella:
                tabella.append(i[0])
        cursor.close()
        cnx.close()
        return tabella

    def get_migliori(self, anno, brand, retailer):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """
            SELECT gds.Date, SUM(gds.Quantity * gds.Unit_sale_price) as Ricavo, gr.Retailer_code, gp.Product_number
            FROM go_sales.go_daily_sales AS gds
            INNER JOIN go_sales.go_products AS gp ON gds.Product_number = gp.Product_number
            INNER JOIN go_sales.go_retailers AS gr ON gds.Retailer_code = gr.Retailer_code
        """

        # Costruzione della clausola WHERE in base ai valori dei parametri
        where_clause = []
        parameters = []

        # Verifica e costruzione della clausola WHERE per il parametro Retailer_code
        if retailer != 'Nessun filtro':
            where_clause.append("gds.Retailer_code = %s")
            parameters.append(retailer)

        # Verifica e costruzione della clausola WHERE per il parametro Date (anno)
        if anno != 'Nessun filtro':
            where_clause.append("YEAR(gds.Date) = %s")
            parameters.append(anno)

        # Verifica e costruzione della clausola WHERE per il parametro Product_brand
        if brand != 'Nessun filtro':
            where_clause.append("gp.Product_brand = %s")
            parameters.append(brand)

        # Unione delle clausole WHERE (se presenti)
        if where_clause:
            query += " WHERE " + " AND ".join(where_clause)

        # Aggiunta delle clausole GROUP BY, ORDER BY e LIMIT
        query += """
            GROUP BY gds.Date
            ORDER BY Ricavo DESC
            LIMIT 5
        """

        # Esecuzione dell'istruzione SQL con i parametri
        cursor.execute(query, parameters)

        # Recupero dei risultati
        results = cursor.fetchall()

        # Chiusura del cursore e della connessione
        cursor.close()
        cnx.close()
        return results
    def analizza_vendite(self,anno, brand, retailer):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """ select sum(gds.Quantity*gds.Unit_sale_price) as Ricavo, count(*),count(distinct gr.Retailer_code), count(distinct gp.Product_number) 
                    FROM go_sales.go_daily_sales AS gds 
                    INNER JOIN go_sales.go_products AS gp
                    ON gds.Product_number = gp.Product_number
                    inner join go_sales.go_retailers gr 
                    on gds.Retailer_code = gr.Retailer_code 
                    
                    """
        # Costruzione della clausola WHERE in base ai valori dei parametri
        where_clause = []
        parameters = []

        # Verifica e costruzione della clausola WHERE per il parametro Retailer_code
        if retailer != 'Nessun filtro':
            where_clause.append("gds.Retailer_code = %s")
            parameters.append(retailer)

        # Verifica e costruzione della clausola WHERE per il parametro Date (anno)
        if anno != 'Nessun filtro':
            where_clause.append("YEAR(gds.Date) = %s")
            parameters.append(anno)

        # Verifica e costruzione della clausola WHERE per il parametro Product_brand
        if brand != 'Nessun filtro':
            where_clause.append("gp.Product_brand = %s")
            parameters.append(brand)

        # Unione delle clausole WHERE (se presenti)
        if where_clause:
            query += " WHERE " + " AND ".join(where_clause)
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results




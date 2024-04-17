import flet as ft

from database.go_daily_sales_DAO import Daily_sales_DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleTopVendite(self, e):
        anno = self._view.lista_anno.value
        brand = self._view.lista_brand.value
        retailer = self._view.lista_retailer.value
        self._view.stampa.clean()
        self._view.update_page()
        if anno is None:
            self._view.create_alert("Nessun anno selezionato")
            return
        if brand is None:
            self._view.create_alert("Nessun brand selezionato")
            return
        if retailer is None:
            self._view.create_alert("Nessun retailer selezionato")
            return

        tabella = Daily_sales_DAO().get_migliori(anno, brand, retailer)
        for i in tabella:
            self._view.stampa.controls.append(ft.Text(f"Data: {i[0]}, Ricavo: {i[1]}, Retailer: {i[2]}, Product: {i[3]}"))
        self._view.update_page()

    def handleAnalizzaVendite(self, e):
        anno = self._view.lista_anno.value
        brand = self._view.lista_brand.value
        retailer = self._view.lista_retailer.value
        self._view.stampa.clean()
        self._view.update_page()
        if anno is None:
            self._view.create_alert("Nessun anno selezionato")
            return
        if brand is None:
            self._view.create_alert("Nessun brand selezionato")
            return
        if retailer is None:
            self._view.create_alert("Nessun retailer selezionato")
            return



        tabella = Daily_sales_DAO().analizza_vendite(anno, brand, retailer)
        for i in tabella:
            self._view.stampa.controls.append(
                ft.Text(f"Statistiche vendite\n"
                        f"Giro d'affari: {i[0]}\n"
                        f"Numero vendite: {i[1]}\n"
                        f"Numero retailers coinvolti: {i[2]}\n"
                        f"Numero prodotti coinvolti: {i[3]}"))
        self._view.update_page()
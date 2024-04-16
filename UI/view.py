import flet as ft

from database.go_daily_sales_DAO import Daily_sales_DAO
from database.go_product_DAO import Product_DAO
from database.go_retailers_DAO import Retailers_DAO


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.lista_anno = ft.Dropdown(label="Anno")
        self.lista_brand = ft.Dropdown(label="Brand")
        self.lista_retailer = ft.Dropdown(label="Retailer", width=500)

        self.popola_lista_brand()
        self.popola_lista_retailers()
        self.popola_lista_anno()
        row1 = ft.Row([self.lista_anno, self.lista_brand, self.lista_retailer], alignment=ft.MainAxisAlignment.CENTER)

        self.btn_topVendite = ft.ElevatedButton(text="Top vendite")
        self.btn_analizzaVendite = ft.ElevatedButton(text="Analizza vendite")
        row2 = ft.Row([self.btn_topVendite, self.btn_analizzaVendite], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)
        self._page.update()




    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def popola_lista_brand(self):
        tabella = Product_DAO().get_product()
        self.lista_brand.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for elem in tabella:
            self.lista_brand.options.append(ft.dropdown.Option(key=elem.product_number, text=elem.product))
        self._page.update()

    def popola_lista_retailers(self):
        tabella = Retailers_DAO().get_retailers()
        self.lista_retailer.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for elem in tabella:
            self.lista_retailer.options.append(ft.dropdown.Option(key=elem.retailer_code, text=elem.retailer_name))
        self._page.update()

    def popola_lista_anno(self):
        tabella = Daily_sales_DAO().get_anno()
        self.lista_anno.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for elem in tabella:
            self.lista_anno.options.append(ft.dropdown.Option(text=elem[0]))
        self._page.update()


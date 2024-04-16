import dataclasses
from datetime import date

from model.method import Method
from model.product import Product
from model.retailers import Retailers


@dataclasses.dataclass
class Daily_sales:
    retailer: Retailers
    product: Product
    method: Method
    date: date
    quantity: int
    unit_price: float
    unit_sales_price: float


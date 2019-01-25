# This tool can load products from excel file
# Format, sequency no mater, but header are mandatory:
# CategoryName | ProductName | Price | Quantity | DescriptionShort | Description
#
# where mandatory: CategoryName, ProductName, Price, Quantity
from mainapp.models import ProductCategory as ProductCat
from mainapp.models import Product as Product
from pathlib import Path
import pandas
from django.db import IntegrityError
# import xlrd

class ExcelIoModelDB:
    xl_col_nm = {
        'cn': "CategoryName",
        'pn': "ProductName",
        'pr': "Price",
        'qt': "Quantity",
        'ds': "DescriptionShort",
        'd_': "Description",
    }
    db_fld_nm = {
        'cn': "name",
        'pn': "name",
        'pr': "price",
        'qt': "quantity",
        'ds': "descriptionShort",
        'd_': "description",
        'im': "image",
    }

    def simple_like_console(self, df: pandas.DataFrame):
        for index, row in df.iterrows():
            category_name = row[self.xl_col_nm['cn']]
            category = ProductCat()
            category.name = category_name
            try:
                category.save()
            except IntegrityError:
                category = ProductCat.objects.get(name=category_name)

            product = Product()
            product.categoryId = category
            product.name = row[self.xl_col_nm['pn']]
            product.price = row[self.xl_col_nm['pr']]
            product.quantity = row[self.xl_col_nm['qt']]
            product.descriptionShort = row[self.xl_col_nm['ds']]
            product.description = row[self.xl_col_nm['d_']]
            try:
                product.save()
            except IntegrityError:
                pass

    @staticmethod
    def read2data_frame(file_name: str):
        if not(Path(file_name).is_file()):
            return
        return pandas.read_excel(file_name)

    def frame2db(self, df: pandas.DataFrame):
        for index, row in df.iterrows():
            category_name = row[self.xl_col_nm['cn']]
            pc = ProductCat.objects.filter(name__exact=category_name)
            if not pc.exists():
                pc = ProductCat(row[self.xl_col_nm['cn']])
                pc.save()
            pr = Product.objects.get(name=row[self.xl_col_nm['cn']])

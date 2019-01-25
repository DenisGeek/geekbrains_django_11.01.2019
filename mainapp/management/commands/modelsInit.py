from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from mainapp.XL2DB import ExcelIoModelDB
from authapp.models import ShopUser

class Command(BaseCommand):
    # initialise models in db
    # python manage.py modelsInit

    @staticmethod
    def loadXl2Db():
        xl_io_db = ExcelIoModelDB()
        import os
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, "ProductsXls.xlsx")

        df = xl_io_db.read2data_frame(file_path)  # get data fro xls
        xl_io_db.simple_like_console(df)  # write data to db

    @staticmethod
    def createUsers():
        super_user = ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', 'admin', age=38)

    def handle(self, *args, **options):
        self.loadXl2Db()
        self.createUsers()

from django.shortcuts import render
from django.conf import settings
from .models import ProductCategory, Product
from .pl import ExcelIoModelDB

# Create your views here.
pageTitles = {
    'main': "Main",
    'catalog': "Catalog",
    'contacts': "Contacts",
}

mainMenuLinks = [
    {'href': 'main', 'name': pageTitles['main']},
    {'href': 'products:index', 'name': pageTitles['catalog']},
    {'href': 'contact', 'name': pageTitles['contacts']},
    {'href': 'load_xls', 'name': "Load XLS"},
]
pageTitle = 'titleDummy'

contextCommon = {
    'pageTitle': pageTitle,
    'mainMenuLinks': mainMenuLinks,
    'mediaUrl': settings.MEDIA_URL,
}

def main(request):
    contextCommon['pageTitle'] = pageTitles['main']
    context = contextCommon
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)  # print to console
    contextCommon['pageTitle'] = pageTitles['catalog']
    context = contextCommon
    products_all = Product.objects.all()
    context.update({'products': products_all})
    return render(request, 'mainapp/catalog.html', context)


def contact(request):
    contextCommon['pageTitle'] = pageTitles['contacts']
    context = contextCommon
    return render(request, 'mainapp/contacts.html', context)


def load_xls(request):

    xl_io_db = ExcelIoModelDB()
    import os
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, "ProductsXls.xlsx")

    df = xl_io_db.read2data_frame(file_path)  # get data fro xls
    xl_io_db.simple_like_console(df)  # write data to db

    return main(request)  # emulate jump to main


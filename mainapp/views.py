from django.shortcuts import render

# Create your views here.
pageTitles={
    'main' : "Main",
    'catalog' : "Catalog",
    'contacts' : "Contacts",
}

mainMenuLinks = [
        {'href': 'main'    , 'name': pageTitles['main']},
        {'href': 'products', 'name': pageTitles['catalog']},
        {'href': 'contact' , 'name': pageTitles['contacts']},
]
pageTitle = 'titleDummy'

contextCommon={
    'pageTitle': pageTitle,
    'mainMenuLinks':mainMenuLinks,
}


contextCommon['pageTitle'] = pageTitles['main']
def main(request):
    return render(request, 'mainapp/index.html', contextCommon)
    
contextCommon['pageTitle'] = pageTitles['catalog']
def products(request):
    return render(request, 'mainapp/catalog.html', contextCommon)
    
contextCommon['pageTitle'] = pageTitles['contacts']
def contact(request):
    return render(request, 'mainapp/contacts.html', contextCommon)

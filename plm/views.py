from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .models import ProgramLanguage

# Create your views here.
def index(request):
    # print(ProgramLanguage.objects.all())
    allLanguages = {}
    categoryLanguages = ProgramLanguage.objects.values('lang_category', 'id')
    # print(categoryLanguages)
    languages = {item['lang_category'] for item in categoryLanguages}
    # print(languages)
    for language in languages:
        lang = ProgramLanguage.objects.filter(lang_category=language)
        allLanguages.update({language:[item for item in lang]})
    # print(allLanguages)
    params = {'lang':allLanguages}
    return render(request, 'plm/index.html', params)

def about(request):
    return render(request, 'plm/about.html')

def category(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'plm/category.html')

def saved(request):
    lang = ProgramLanguage.objects.filter(lang_saved=True)
    params = {'languages':lang}
    return render(request, 'plm/saved.html', params)

def save(request,cid):
    langs = ProgramLanguage.objects.get(id=cid)
    langs.lang_saved = not langs.lang_saved
    langs.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('/success/')
    # allLanguages = {}
    # categoryLanguages = ProgramLanguage.objects.values('lang_category', 'id')
    # languages = {item['lang_category'] for item in categoryLanguages}
    # for language in languages:
    #     lang = ProgramLanguage.objects.filter(lang_category=language)
    #     allLanguages.update({language:[item for item in lang]})
    # params = {'lang':allLanguages}
    # return render(request, 'plm/index.html', params)

def load_more(request,category):
    langs = ProgramLanguage.objects.filter(lang_category=category)
    params = {'category':langs}
    return render(request, 'plm/load_more.html', params)

def read_more(request,cid):
    f = open('./plm/media/Python.txt', 'r')
    file_content = f.read()
    f.close()
    lang = ProgramLanguage.objects.get(id=cid)
    params = {'language':lang, 'file_content':file_content}
    return render(request, 'plm/read_more.html', params)

import re
def searchMatch(query, language):
    search = [language.lang_name, language.lang_category, language.lang_brief_desc]
    for text in search:
        if re.search(query,text, re.M|re.I):
            return True
    return False
    # queries = [query,query.lower(),query.upper(),query.capitalize()]
    # # search = [re.split(',',language.lang_brief_desc.split())]
    # search = list(str(language.lang_brief_desc).split(" "))
    # for q in queries:
    #     if (q in language.lang_name) or (q in search) :
    #         return True
    # return False

def search(request):
    query = request.GET.get("Search")
    allLanguages = {}
    categoryLanguages = ProgramLanguage.objects.values('lang_category', 'id')
    languages = {item['lang_category'] for item in categoryLanguages}
    for language in languages:
        langtemp = ProgramLanguage.objects.filter(lang_category=language)
        lang = [item for item in langtemp if searchMatch(query,item)]
        if len(lang)!=0:
            allLanguages.update({language:[item for item in lang]})
    params = {'lang':allLanguages}
    return render(request, 'plm/search.html', params)
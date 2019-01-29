from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse("I like eggs")

def count(request):

    fulltext = request.GET['fulltext']
    print(fulltext)

    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] +=1
        else:
            #add to the dictionary
            worddict[word]=1
    sorted_words=sorted(worddict.items(), key=operator.itemgetter(1), reverse= True)

    return render(request, 'count.html',{'full':fulltext, 'count':len(wordlist),'sorted_words':sorted_words})

def about(request):
    return render(request, 'about.html')

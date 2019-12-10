from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word not in worddictionary:
            worddictionary[word] = 0
        worddictionary[word] += 1

    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1), reverse=True)

    length = len(wordlist)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': length, 'sortedwords': sortedwords})

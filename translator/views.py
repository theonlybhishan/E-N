from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
def translate(request):
    if request.method =='POST':
        data = request.POST
        word = data.get('word')
        payload = {'q':word}
        r = requests.get('https://www.englishnepalidictionary.com/', params= payload).text
        # print(dir(r))
        # print(word)
        soup = bs(r,'lxml')
        meaning = soup.find('div',class_='search-result').h3.text
        print(meaning)

        context={
            'meaning': meaning
        }
        return render(request,'index.html',context)
    return render(request,'index.html')
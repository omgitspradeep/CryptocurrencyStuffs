from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def home(request):
    # Get Crypto exchange rates
    rate_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM&tsyms=USD")
    rate_api = json.loads(rate_request.content)

    # Get crypto news
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news_api = json.loads(news_request.content)
    # https://min-api.cryptocompare.com/data/v2/news/?lang=EN
    # https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR
    
    return render(request,"crypto/home.html",{'news_api':news_api,'rate_api':rate_api})

def detail(request):
    if request.method =="POST":
        q = request.POST["query"].upper()
        if q in ['BTC','XRP','ETH','BCH','EOS','LTC','XLM']:
            apiUrl="https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+q+"&tsyms=USD"
            print(apiUrl)
            queryData=json.loads((requests.get(apiUrl)).content)
            return render(request,"crypto/detail.html",{"queryData":queryData,'currency':q})
    
    return render(request,"crypto/detail.html",{"queryData":"Please type the correct currency code in Search Button"})

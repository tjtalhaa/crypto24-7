

from django.shortcuts import render

# Create your views here.


def home(request):
    import requests
    import json

    # cryptp=o price
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # chart
    chart_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,EOS,LTC&tsyms=USD")
    chart = json.loads(chart_request.content)

    return render(request, 'home.html', {'price': price, 'chart': chart})


def search(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()

        # search call from seach form
        search_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        search = json.loads(search_request.content)

        return render(request, 'search.html', {'search': search})


def blog(request):
    # Crypto news
    import requests
    import json
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'blog.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})

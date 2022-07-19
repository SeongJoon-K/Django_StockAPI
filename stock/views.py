from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def home(request):
    
    try:
        ticker = request.GET['ticker']
        stock_api = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_864b08660adf4a1c96b4594ae419870a")
        stock = json.loads(stock_api.content)

    except Exception as e:
        stock = ""

    
    content = {'stock':stock}

    return render(request, 'stock/home.html', content)

# 경로가 이렇게 되는 이유는 장고에서 기본적으로 templates 폴더를 탐색하게 하기때문임
# 한 프로젝트 안에 앱이 여러개가 돌 수 있는데 한 번 더 앱 이름과 같은 폴더를 생성해서
# 같은 이름의 home.html을 차용하지 않도록 방지하기 위함임
from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world</h1>")

def post(request):
    # print("*****")
    # print(request.method)
    # print(request.POST)
    # print("*****")

    if request.method == 'POST': # POST 요청 처리
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index') # return render(request, 'lotto/default.html', {})

    else: # GET 요청 처리
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})

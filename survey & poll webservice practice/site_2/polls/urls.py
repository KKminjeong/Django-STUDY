from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import

app_name = 'polls'
urlpatterns = [
    # "127.0.0.1:8000/polls/" 이후의 URL은 polls/urls.py가 handling하도록 만들 예정입니다.
    path('', views.index, name='index'), # '127.0.0.1:8000/polls/' 를 받아내도록 만들어줄 것입니다.
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

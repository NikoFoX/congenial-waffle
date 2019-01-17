from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # for example: /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # for example: /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # for example: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # INFO
    # /polls/info
    path('info', views.info, name='info'),

    # SITE MAP
    # /polls/MAP
    path('map', views.map, name='map'),

    # TEST
    # /polls/test
    path('test', views.test, name='test'),
]

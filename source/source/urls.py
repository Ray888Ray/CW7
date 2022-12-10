"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.view.pull_views import IndexView, PullView, PullAddView, PullDeleteView, PullUpdateView
from webapp.view.choice_view import ChoiceUpdatedView, ChoiceDeleteView, ChoiceAddView
from webapp.view.answer_view import AnswerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pull/<int:pk>/view/', PullView.as_view(), name='info'),
    path('pull/add/', PullAddView.as_view(), name='add'),
    path('pull/<int:pk>/delete/', PullDeleteView.as_view(), name='delete'),
    path('pull/<int:pk>/update/', PullUpdateView.as_view(), name='update'),


    path('choice/<int:pk>/update/', ChoiceUpdatedView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete'),
    path('choice/<int:pk>/add/option/', ChoiceAddView.as_view(), name='choice_add'),


    path('answer/<int:pk>/', AnswerView.as_view(), name='answer_option'),
]

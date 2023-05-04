from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('game/', views.getGameRounds),
    path('register/', views.getStudents),
    path('postRound/', views.postRound),
    path('postUser/', views.postUser),
    path('getLogin/',views.loginUser),
    path('updateRound/<int:pk>/', views.GameRoundUpdateView.as_view())
]
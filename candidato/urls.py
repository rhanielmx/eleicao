from django.urls import path
from .views import candidates_list, candidates_profile, candidates_opinion

urlpatterns = [
    path('list/', candidates_list, name='candidates_list'),
    path('profile/<str:url_name>', candidates_profile, name='candidates_profile'),
    path('profile/<str:url_name>/opinion', candidates_opinion, name='candidates_opinion'),
]

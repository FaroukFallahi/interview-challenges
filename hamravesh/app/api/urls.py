
from django.urls import path
from api.views import  endpoint, endpoint_id
urlpatterns = [
    path('', endpoint, name='endpoint'),
    path('<str:id_or_name>', endpoint_id, name='endpoint_id'),
]
  
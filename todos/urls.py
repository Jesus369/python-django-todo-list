from django.conf.urls import url
# From current directory, import views file
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index")
]

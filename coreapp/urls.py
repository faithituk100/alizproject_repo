from django.urls import path
from .views import home_view, detail_view, gallery_view


urlpatterns = [
    path('', home_view, name='home'),
    path('detail', detail_view, name='detail'),
    path('gallery', gallery_view, name='gallery')
]

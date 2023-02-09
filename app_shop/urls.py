from django.urls import path
from .views import ItemDetailView, ItemBuyView


urlpatterns = [
    path('item/<int:pk>', ItemDetailView.as_view(), name='item-detail'),
    path('buy/<int:pk>', ItemBuyView.as_view(), name='buy-item')
]

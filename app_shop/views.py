import logging

from django.shortcuts import get_object_or_404, render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from shop_site.settings import STRIPE_PUBLIC
from .models import Item
from .services import create_stripe_checkout_session

logger = logging.getLogger('item')


class ItemDetailView(GenericAPIView):
    """
    Detail view for item.
    Return html page with buy button.
    """
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return render(request, 'items/item_detail.html', {'item': item, 'stripe_key': STRIPE_PUBLIC})


class ItemBuyView(GenericAPIView):
    """
    Returns session id of item when user adds it to checkout stripe session.
    """
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        session = create_stripe_checkout_session(item)
        logger.info(f'checkout session for {item} is {session.id}')
        return Response({"session_id": session.id})

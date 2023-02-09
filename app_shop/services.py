import stripe
import logging
from shop_site.settings import STRIPE_SECRET


stripe.api_key = STRIPE_SECRET
logger = logging.getLogger('checkout_session')


def create_stripe_checkout_session(item):
    """
    Function creates checkout session from item.
    """
    logger.info(f'Started getting checkout session from item: {item}')
    try:
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    },
                    'unit_amount': item.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel'
        )
    except Exception as exc:
        logger.error(f'Exception {exc} was raised')
        return "Could not find session ID."
    logger.info(f'Stops getting checkout session from item: {item}')
    return session

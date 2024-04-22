import stripe
from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request):
    context = {'stripe_public_key': settings.STRIPE_PUBLIC_KEY}
    return render(request, 'index.html', context)


def create_charge(request):
    token = request.POST['stripeToken']

    try:
        charge = stripe.Charge.create(
            amount=5000,  # $50 in cents
            currency='usd',
            description='Example charge',
            source=token,
        )
    except stripe.error.StripeError as e:
        # Handle error
        return render(request, 'error.html', {'message': str(e)})

    return render(request, 'success.html')

# Don't forget to add the URL configurations in urls.py

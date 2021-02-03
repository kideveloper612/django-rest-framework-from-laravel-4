from snippets.models import Subscription
from datetime import timedelta
from django.utils import timezone


class SubscriptionBusinesss:
    def __init__(self):
        pass

    @staticmethod
    def getByUserId(userId):
        subscription = Subscription.objects.filter(user=userId)

        if subscription:
            return subscription[0]

        return False

    @staticmethod
    def getValidByUserId(userId):
        subscription = SubscriptionBusinesss().getByUserId(userId)

        if subscription and SubscriptionBusinesss().isValid(subscription):
            return subscription

        return False

    @staticmethod
    def isValid(subscription):
        if not subscription.expiration_at:
            return True

        expirationAt = subscription.expiration_at + timedelta(days=35)

        if expirationAt < timezone.now():
            return False

        return True

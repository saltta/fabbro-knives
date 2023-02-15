from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'newsletter'
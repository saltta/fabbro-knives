from django.db import models


class Contact(models.Model):
    """A model for storing contact submissions."""
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

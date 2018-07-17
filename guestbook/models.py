from django.db import models


# Create your models here.
class Guestbook(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    content = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Guestbook(%s, %s, %s)' % (self.id, self.name, self.content)

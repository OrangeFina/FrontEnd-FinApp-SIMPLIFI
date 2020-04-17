from django.db import models

# Create your models here.


class Risk(models.Model):
    response = models.CharField(max_length = 100)
    aType = models.CharField(max_length = 120)
    dafault = models.CharField("Default", max_length=240)

    def __str__(self):
        return self.response
    


# class News(models.Model):
#     title=models.CharField(max_length=64)
#     created_at=models.DateTimeField(auto_now=True)

#     def _repr_(self):
#         return '<News {} @ {}>'.format(self.title, self.created_at)






from django.db import models


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    pipe = models.IntegerField()

    def __str__(self):
        return str(self.id)


class AllCard(models.Model):
    pipeId = models.AutoField(primary_key=True)
    first = models.IntegerField()
    after = models.CharField(max_length=100)
    last = models.IntegerField()
    before = models.CharField(max_length=100)
    


    def __str__(self):
        return str(self.id)




        
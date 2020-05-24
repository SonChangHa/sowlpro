from django.db import models

class table(models.Model):
    tableTitle = models.CharField(max_length=200)

    def __str__(self):
        return self.tableTitle
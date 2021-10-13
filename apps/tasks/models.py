from django.db import models


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    folder_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} : {self.id}'

    class Meta:
        db_table = 'app_task'
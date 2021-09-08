
from django.db import models


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    folder_id = models.BigIntegerField()
    selected = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone1 = models.CharField(max_length=50, blank=True, null=True)
    phone1_label = models.CharField(max_length=10, blank=True, null=True)
    phone2 = models.CharField(max_length=50, blank=True, null=True)
    phone2_label = models.CharField(max_length=10, blank=True, null=True)
    phone3 = models.CharField(max_length=50, blank=True, null=True)
    phone3_label = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    map = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    google_id = models.CharField(max_length=255, blank=True, null=True)
    fillable = [
        'folder_id',
        'name',
        'company',
        'address',
        'phone1',
        'phone1_label',
        'phone2',
        'phone2_label',
        'phone3',
        'phone3_label',
        'email',
        'website',
        'map',
        'notes',
    ]

    def __str__(self):
        return f'{self.name} {self.id}'


class Favorite(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    folder_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    root = models.CharField(max_length=50, blank=True, null=True)
    passkey = models.CharField(max_length=50, blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)
    home_rank = models.IntegerField(blank=True, null=True)
    fillable = [
        'folder_id',
        'name',
        'url',
        'description',
        'login',
        'root',
        'passkey',
        'selected',
        'home_rank',
    ]

    def __str__(self):
        return f'{self.name} {self.id}'


class Folder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    page = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    home_column = models.IntegerField(blank=True, null=True)
    home_rank = models.IntegerField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    fillable = [
        'name',
        'home_column',
        'home_rank',
        'selected',
        'active',
    ]


    def __str__(self):
        return f'{self.name} {self.id}'


class Note(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    folder_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)
    fillable = [
        'folder_id',
        'subject',
        'note',
    ]

    def __str__(self):
        return f'{self.subject} {self.id}'


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    folder_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.id}'

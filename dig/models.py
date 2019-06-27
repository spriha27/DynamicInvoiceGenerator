from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='documents/emailtemplates')

class File(models.Model):
    file = models.FileField(upload_to='documents/datafiles')
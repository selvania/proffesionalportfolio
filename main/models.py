from django.db import models

# Create your models here.
class Word(models.Model):
    """
    Model for words with counts of their comparitive usage for each subject
    """
    word = models.CharField(max_length=55, primary_key=True)
    conversational = models.SmallIntegerField(default=0)
    legal = models.SmallIntegerField(default=0)
    scholarly = models.SmallIntegerField(default=0)
    articles = models.SmallIntegerField(default=0)
    chat = models.SmallIntegerField(default=0)
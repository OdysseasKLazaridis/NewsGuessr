from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Daily_Challenge(models.Model):
    
    created_at = models.DateTimeField(auto_now_add= True, editable = False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
    
class Quiz(models.Model):
    # ForeignKey to Choice model for dynamic choices
    text = models.CharField(max_length=200, default="default text")
    daily_challenge = models.ForeignKey(Daily_Challenge, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    options = (
        ("correct"),
        ("wrong")
    )
    name = models.CharField(max_length=100)  # The display name of the choice
    mentions = models.IntegerField() # The value that will be saved to the database
    is_correct = models.BooleanField(default=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



    





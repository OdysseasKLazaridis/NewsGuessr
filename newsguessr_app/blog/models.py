from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Daily_challenge(models.Model):
    
    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )


    slug = models.SlugField(max_length=250, unique = True)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True, editable = False)
    updated_at = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
    
class Choice(models.Model):
    options = (
        ("correct"),
        ("wrong")
    )
    name = models.CharField(max_length=100)  # The display name of the choice
    mentions = models.IntegerField() # The value that will be saved to the database
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    # ForeignKey to Choice model for dynamic choices

    keyword = models.CharField(max_length= 50)
    choice_field = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)





from django.db import models
from custom_user.models import User
from base.models import BaseModel



class Comment(BaseModel, models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.title


    class Meta:
        db_table = 'comment'

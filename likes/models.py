from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_liked_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='likes_liked_items_ct')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

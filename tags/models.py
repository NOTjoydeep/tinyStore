# from email.headerregistry import ContentTypeHeader
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag appled to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we need to things to make tags indpendent
    # Type of object (product, order, cust)
    # ID 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() 
    # Only side effect of this app if any table doesn't have integer as primary key.
    
    # to indentiy the object to each content
    content_object = GenericForeignKey()




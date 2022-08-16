# from email.headerregistry import ContentTypeHeader
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Custom manager (objects)
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        query_set = TaggedItem.objects\
                    .select_related('tag')\
                    .filter(
                        content_type=content_type,
                        object_id=obj_id
                    )
        
        return query_set

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TaggedItem(models.Model):
    # Custom manager (objects)
    objects = TaggedItemManager()
    # What tag appled to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # we need two things to make tags indpendent
    # Type of object (product, order, cust)
    # ID 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() 
    # Only side effect of this app if any table doesn't have integer as primary key.
    
    # to indentiy the object to each content
    content_object = GenericForeignKey()




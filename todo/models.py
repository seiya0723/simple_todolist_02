from django.db import models

# Create your models here.
import uuid

class Todolist(models.Model):

    class Meta:
        db_table = "todolist"

    #UUID、締め切り、やること
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deadline    = models.DateTimeField(verbose_name="期限")
    content     = models.CharField(verbose_name="やること",max_length=100)

    def __str__(self):
        return self.content


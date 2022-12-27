from django.db.models import *
from django.contrib.auth import get_user_model

# Create your models here.
class dist1(Model):
    STATUS = (
        ('doing', 'fazendo'),
        ('done', 'done')
    )
    user = ForeignKey(get_user_model(), on_delete=CASCADE)
    title = CharField(max_length=255)
    description = TextField(max_length=255)
    done = CharField(max_length=5, choices=STATUS)
    creat_at = DateTimeField(auto_now_add=True)
    update_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    name = fields.CharField(max_length=255)
    is_admin = fields.BooleanField(default=False)
    
    def __str__(self):
        return str(self.name)
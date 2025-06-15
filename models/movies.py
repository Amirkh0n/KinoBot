from tortoise import fields
from tortoise.models import Model


class Movie(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200, null=True)
    description = fields.TextField(null=True)
    year = fields.IntField(null=True)
    short_video_id = fields.IntField(null=True)
    full_video_id = fields.IntField(null=True)
    duration = fields.CharField(max_length=100, null=True)
    size = fields.CharField(max_length=100, null=True)
    views = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
        
    async def view(self):
        self.views += 1
        await self.save()
from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='media/music/artist', null=True)
    age = models.IntegerField(null=True)
    page_views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Album(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='media/music/album', null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    duration = models.IntegerField(null=True)
    music = models.URLField(null=True)
    listens = models.PositiveBigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

from django.db import models

class Poster(models.Model):
    image = models.ImageField(upload_to='posters/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poster uploaded on {self.uploaded_at}"

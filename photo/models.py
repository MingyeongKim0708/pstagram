from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_photos')
    photo = models.ImageField(blank=True, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #옵션
    class Meta:
        ordering = ['-updated'] #업데이트 내림차순(-)으로 정렬

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)]) #객체를 수정하게 되면 상세페이지로 이동

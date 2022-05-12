from django.db import models
from django.urls import reverse

class Bookmark(models.Model): #Bookmark 클래스 생성: 모델의 기본
    site_name = models.CharField(max_length=100) #필드: 정보 저장
    url = models.URLField('Site URL')
    def __str__(self):
        #객체를 출력할 때 나타낼 값
        return "이름: "+self.site_name + ", 주소: " +self.url
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
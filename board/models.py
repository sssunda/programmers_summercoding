from django.db import models
from django import forms


# Create your models here.
class Post(models.Model):
    # 제목_100 글자 이내
    title = models.CharField(max_length=100, verbose_name='제목')
    # 내용_텍스트필드
    text = models.TextField(verbose_name='내용')
    # 우선순위_3글자 이내 ('001','002', ~, '999', 'end')
    rank = models.CharField(max_length=3, verbose_name='우선 순위')
    # 마감기한 체크
    due_chk = models.BooleanField(default=False)
    # 마감기한_마감기한 체크가 False일 경우, null 허용필요
    due_date = models.DateField(blank=True, null=True, verbose_name='마감기한')
    # 완료여부
    complete_chk = models.BooleanField(default=False, verbose_name='완료 여부')
    # 만든 시점
    created_at = models.DateField(auto_now_add=True)
    # 수정 시점
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

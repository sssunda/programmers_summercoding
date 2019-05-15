from django.db import models

# Create your models here.
class Post(models.Model):
    # 제목_100 글자 이내
    title = models.CharField(max_length=100)
    # 내용_텍스트필드
    text = models.TextField()
    # 우선순위_3글자 이내 ('001','002', ~, '999', 'end')
    rank = models.CharField(max_length=3)
    # 마감기한 체크
    due_chk = models.BooleanField(default=False)
    # 마감기한_마감기한 체크가 False일 경우, null 허용필요
    due_date = models.DateField(blank=True, null=True)
    # 완료여부
    complete_chk = models.BooleanField(default=False)

    def __str__(self):
        return self.title
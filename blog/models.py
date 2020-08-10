from django.utils import timezone
from django.db import models

from django import forms

def min_len_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('제목은 3글자 이상 입력해주세요 !')


# Create your models here.

class Post(models.Model):
    #작성자
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)

    # 제목
    title=models.CharField(max_length=200,validators=[min_len_3_validator])

    # 게시글 내용
    text=models.TextField()

    #작성 일자
    created_date=models.DateTimeField(default=timezone.now)

    #게시 일자
    published_date=models.DateTimeField(blank=True,null=True)


    # 필드 추가 - 삭제할 예정
    #test=models.TextField()
    # 다시 삭제할 부분

    # 게시 일자에 현재 날짜시간을 대입해주는 함수
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    # 객체 주소 대신에 글 제목을 반환해주는 toString() 함수

    def __str__(self):
        return self.title

    #승인된 Comments 만 반환해주는 함수
    def approved_comments(self):
        #comments는 related_name=comments!
        return self.comments.filter(approved_comment=True)

# Post에 있는 comment (댓글) 클래스
class Comment(models.Model):
    #post정보
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')

    #작성자
    author=models.CharField(max_length=100)

    #댓글 내용
    text=models.TextField()

    #댓글 작성일자
    created_date=models.DateTimeField(default=timezone.now)

    #댓글 승인여부
    approved_comment=models.BooleanField(default=False)

    #댓글 승인
    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.text






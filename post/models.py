from django.db import models


# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=256,verbose_name='제목')
    userid=models.ForeignKey(
        'dsuser.Dsuser',
        verbose_name='작성자',
        on_delete=models.CASCADE
    )
    img_url=models.CharField(max_length=256,verbose_name='이미지주소')
    contents=models.TextField(verbose_name='내용')
    tags=models.ManyToManyField('tag.Tag',verbose_name='태그')
    register_date=models.DateTimeField(auto_now_add=True,verbose_name='등록시간')

    def __str__(self):
        return self.title 

    class Meta:
        db_table='djangostagram_post'
        verbose_name='게시글'
        verbose_name_plural='게시글'
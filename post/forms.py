from django import forms 

class PostForm(forms.Form):
    title=forms.CharField(
        label='제목',
    )
    contents=forms.CharField(
        label='내용',
        widget=forms.Textarea,
        error_messages={
            'required':'내용을 입력하세요',
        }
    )
    img_url=forms.CharField(
        label='이미지주소',
        error_messages={
            'required':'이미지 주소를 입력하세요'
        }
    )
    tags=forms.CharField(required=False,label='태그',)
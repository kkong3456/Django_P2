from django import forms 
from django.contrib.auth.hashers import check_password 
from .models import Dsuser 

class LoginForm(forms.Form):
    userid=forms.CharField(
        max_length=32,
        label='사용자이름',
    )
    password=forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput,
    )

    def clean(self):
        cleaned_data=super().clean()
        userid=cleaned_data.get('userid')
        password=cleaned_data.get('password')

        if userid and password:
            try:
                dsuser=Dsuser.objects.get(userid=userid)
            except Dsuser.DoesNotExist:
                self.add_error('userid','아이디가 없습니다.')
                return

            if not check_password(password,dsuser.password):
                self.add_error('password','비밀번호가 틀렸습니다.')
            else:
                self.user_id=dsuser.id



from django import forms
from django.db.models import fields
from .models import Portfolio, Profile, Business

from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.hashers import check_password

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['pf_title', 'pf_content', 'pf_attach']

        # pf_content의 위젯으로 summernote 사용
        widgets = {
            'pf_content': SummernoteWidget(),
        }

        labels = {
            'pf_title': '제목',
            'pf_content': '내용',
            'pf_attach': '썸네일',
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['deal_title', 'deal_content', 'price', 'status']

        # deal_content 위젯으로 summernote 사용
        widgets = {
            'deal_content': SummernoteWidget(),
        }

        labels = {
            'deal_title': '제목',
            'deal_content': '내용',
            'price': '가격',
            'status': '결제 상태',
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'email', 'phone_number', 'introduce']


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')

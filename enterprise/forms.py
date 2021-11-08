from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):

    username = UsernameField(
        label="기업 이름",
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    error_messages = {
        'invalid_login': format_html("적절한 이름과 비밀번호를 입력해 주세요. <br/> 이 필드는 대소문자를 구분합니다."),
        'inactive': "This account is inactive.",
    }


class LoginFormView(LoginView):
    form_class = LoginForm


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': '두 비밀번호가 일치하지 않습니다.',
    }
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=format_html("""비밀번호는 개인정보와 비슷할 수 없습니다.<br/>
                                비밀번호는 최소 8글자 이상이어야 합니다.<br/>
                                비밀번호는 흔히 사용되는 비밀번호일 수 없습니다.<br/>
                                비밀번호는 숫자만 사용될 수 없습니다.
                                """),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ("name", "b_no")
        field_classes = {'name': UsernameField}
        labels = {
            "name": "기업 이름",
            "b_no": "사업자 번호"
        }

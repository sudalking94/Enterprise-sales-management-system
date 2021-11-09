from django import forms
from .models import Customer, Group


class CustomerModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['group'].queryset = Group.objects.filter(
                enterprise=self.request.user)

    def save(self, *args, **kwargs):
        customer = super().save(commit=False)
        customer.enterprise = self.request.user
        customer.save()

    class Meta:
        model = Customer
        fields = (
            "name",
            "picture",
            "birth",
            "gender",
            "group",
            "memo",
        )
        labels = {
            "name": "이름",
            "picture": "프로파일 사진",
            "birth": "생일",
            "gender": "성별",
            "group": "소속",
            "memo": "메모",
        }

        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}, ),
        }

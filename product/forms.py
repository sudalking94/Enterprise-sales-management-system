from django import forms
from .models import Product, SalesLog


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fieldds = (
            "name",
            "price"
        )
        exclude = ('enterprise',)
        labels = {
            "name": "제품 이름",
            "price": "가격",
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        product = super().save(commit=False)
        product.enterprise = self.request.user
        product.save()


class SaleModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        sales_log = super().save(commit=False)
        sales_log.enterprise = self.request.user
        sales_log.save()

    class Meta:
        model = SalesLog
        fields = '__all__'
        exclude = ('enterprise',)

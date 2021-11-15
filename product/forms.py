from django import forms
from django.forms.widgets import Select
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
    """
    판매관리 등록 폼
    """
    customer = forms.ChoiceField(widget=forms.Select(), label="구매자")
    product = forms.ChoiceField(widget=forms.Select(), label="제품 이름")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['customer'].choices = [('', '구매한 고객을 선택하세요.')] + [
            (obj.customer, obj.customer) for obj in SalesLog.objects.filter(enterprise=self.request.user)]
        self.fields['product'].choices = [('', '판매된 제품을 선택하세요.')] + [
            (obj.product, obj.product) for obj in SalesLog.objects.filter(enterprise=self.request.user)]

    def save(self, *args, **kwargs):
        sales_log = super().save(commit=False)
        sales_log.enterprise = self.request.user
        sales_log.save()

    class Meta:
        model = SalesLog
        fields = (
            'customer',
            'product',
            'price',
            'pay_way',
        )

        labels = {
            "price": "가격",
            "pay_way": "결제 방식",
        }

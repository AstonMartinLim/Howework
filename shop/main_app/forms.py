from django.forms import ModelForm
from main_app.models import CustomUser, Product, Purchase, Return


class UserCreateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'wallet']


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name_of_product', 'description', 'price', 'quantity']


class PurchaseCreateForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['quantity']


class ReturnCreateForm(ModelForm):
    class Meta:
        model = Return
        fields = []



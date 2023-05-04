from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages

from main_app.exceptions import NotEnoughProductException, NotEnoughMoneyException
from main_app.forms import UserCreateForm, ProductCreateForm, PurchaseCreateForm, ReturnCreateForm
from main_app.models import CustomUser, Product, Purchase, Return


# Create your views here.


class ProductsListView(ListView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 5
    queryset = Product.objects.all()
    extra_context = {"purchase_form": PurchaseCreateForm()}
    success_url = 'cart'


class CartUser(CreateView):
    form_class = PurchaseCreateForm
    template_name = 'cart.html'
    success_url = 'list_of_purchased_products'
    extra_context = {"purchase_form": PurchaseCreateForm()}

    def form_valid(self, form):
        try:
            self.object = form.save()
        except NotEnoughProductException:
            messages.add_message(self.request, messages.ERROR, "Sorry, not enough product unit")
        except NotEnoughMoneyException:
            messages.add_message(self.request, messages.ERROR, "Sorry, you do not have enough money")
        else:
            messages.add_message(self.request, messages.SUCCESS, "Purchase was successful")
            return HttpResponseRedirect('list_of_purchased_products')
        return redirect(reverse("cart"))


class CreateNewProduct(CreateView):
    form_class = ProductCreateForm
    template_name = 'add_product.html'
    success_url = '/'


class ChangeProduct(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'change_product.html'
    success_url = 'shop.html'
    queryset = Product.objects.all()


class ReturnProduct(ListView):
    model = Return
    form_class = ReturnCreateForm
    template_name = 'return_product.html'
    success_url = '/'


class ReturnProductList(ListView):
    template_name = "return_list.html"
    model = Return
    paginate_by = 5


class PurchasedProductsListView(ListView):
    model = Purchase
    template_name = 'list_of_purchased_products.html'
    paginate_by = 5
    extra_context = {"form": ReturnCreateForm}
    queryset = Purchase.objects.all()


class LoginUser(LoginView):
    template_name = 'login.html'
    success_url = 'shop.html'


class LogoutUser(LogoutView):
    template_name = 'shop.html'


class RegistrationNewUser(CreateView):
    form_class = UserCreateForm
    template_name = 'registration.html'
    success_url = 'login.html'

"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD
from baskets.views import BasketViewSet, BasketItemViewSet
from ecommerce.router import router
from payments.views import BankViewSet, BankAccountViewSet
=======
from baskets.views import BasketItemViewSet, BasketViewSet
from customers.views import CustomerViewSet, AddressViewSet, CityViewSet, CountryViewSet
from ecommerce.router import router
from orders.views import OrderItemViewSet, OrderViewSet, BillingAddressViewSet, ShippingAddressViewSet, \
    OrderBankAccountViewSet
from payments.views import BankAccountViewSet, BankViewSet
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
from products.views import ProductViewSet, CategoryViewSet
from customers.views import *
from orders.views import *

router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
<<<<<<< HEAD
router.register("baskets", BasketViewSet)
router.register("basket-items", BasketItemViewSet)
router.register("customers", CustomerViewSet)
router.register("countries", CountryViewSet)
router.register("cities", CityViewSet)
router.register("addresses", AddressViewSet)
router.register("orders", OrderViewSet)
router.register("order-items", OrderItemViewSet)
router.register("billing-addresses", BillingAddressViewSet)
router.register("shipping-addresses", ShippingAddressViewSet)
router.register("order-bank-accounts", OrderBankAccountViewSet)
router.register("banks", BankViewSet)
router.register("bank-accounts", BankAccountViewSet)
=======
router.register("basket_items", BasketItemViewSet)
router.register("baskets", BasketViewSet)
router.register("customers", CustomerViewSet)
router.register("addresses", AddressViewSet)
router.register("cities", CityViewSet)
router.register("countries", CountryViewSet)
router.register("order_items", OrderItemViewSet)
router.register("orders", OrderViewSet)
router.register("billing_addresses", BillingAddressViewSet)
router.register("shipping_addresses", ShippingAddressViewSet)
router.register("order_bank_accounts", OrderBankAccountViewSet)
router.register("bank_accounts", BankAccountViewSet)
router.register("banks", BankViewSet)

>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d

urlpatterns = [
    path("api/", include(router.urls)),
    path('admin/', admin.site.urls),
]

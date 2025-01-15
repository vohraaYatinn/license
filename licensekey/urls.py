from django.urls import path
from .views import WalletGet

urlpatterns = [

    path(r'license-key/', WalletGet.as_view(), name="notification-get"),

]

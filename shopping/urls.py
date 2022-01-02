from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from . import views

urlpatterns = [
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
	path('store', views.store, name="store"),
	path('cart', views.cart, name="cart"),
	path('checkout', views.checkout, name="checkout"),

	path('update_item', views.updateItem, name="update_item"),
	path('process_order', views.processOrder, name="process_order"),
]
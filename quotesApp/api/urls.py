
from .views import get_quote, QuotesViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'quotes', QuotesViewSet)

urlpatterns = [
    path('get_quote/', get_quote),
    path('quotes_list/', include(router.urls))
]

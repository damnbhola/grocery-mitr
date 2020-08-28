from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('brands', BrandsViewSet, basename='brands')
router.register('stores', StoresViewSet, basename='stores')
router.register('sliders', SlidersViewSet, basename='sliders')
router.register('faqs', FaqsViewSet, basename='faqs')
router.register('orders', OrderViewSet, basename='orders')
urlpatterns = router.urls

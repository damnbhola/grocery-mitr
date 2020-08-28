from rest_framework import serializers
from ..models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()
    brand = BrandsSerializer()
    store = StoresSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class SlidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'question', 'answer')


class FaqsSerializer(serializers.ModelSerializer):
    children = FaqSerializer(many=True)

    class Meta:
        model = Faqs
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = '__all__'


"""
class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    numbers = NumberSerializer(many=True)
    orders = OrderSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
"""

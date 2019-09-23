from rest_framework import serializers
from .models import Category, Blog, Epaper, Trailer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class EpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epaper
        fields = '__all__'


class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = '__all__'


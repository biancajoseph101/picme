from rest_framework import serializers
from .models import Image, Category


class ImageSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        # view_name='category_detail',
        many=True,
        # read_only=True
    )
    # category_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(),
    #     source='category'
    # )

    class Meta:
        model = Image
        fields = ('id', 'category', 'title', 'img')


class CategorySerializer(serializers.ModelSerializer):
    image_list = ImageSerializer(
        # view_name='image_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'img_url', 'image_list')

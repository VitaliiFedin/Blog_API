from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        many=False
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username',
        )

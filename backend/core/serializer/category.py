from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from backend.core import models
from backend.core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "description"]

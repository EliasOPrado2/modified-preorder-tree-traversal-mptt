from rest_framework import serializers
from .models import TestTree

class TestTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestTree
        fields = '__all__'
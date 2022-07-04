from .models import Pictures
from rest_framework import serializers
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ('name', 'image')
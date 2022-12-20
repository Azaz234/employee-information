from importlib.metadata import files
from rest_framework import serializers
from website.models import students
class customersserializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields="__all__"
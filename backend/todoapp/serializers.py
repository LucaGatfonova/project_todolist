from pyexpat import model
from attr import field
from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'description', 'date', 'status')
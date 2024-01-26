from rest_framework import serializers
from .models import card


class cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = card
        fields = ['id','img','title','body']
        
    def create(self, validated_data):
        return card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.img = validated_data.get('img', instance.img)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)

        instance.save()
        return instance
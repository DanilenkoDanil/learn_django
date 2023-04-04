from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLES_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=250)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style=serializers.ChoiceField(choices=STYLES_CHOICES, default='Igor')

    def create(self,validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    

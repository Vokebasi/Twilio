from rest_framework import serializers
from .models import Publication, PublicationImage

class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname')
    created_at = serializers.DateTimeField(format='%d:%m:%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d:%m:%Y %H:%M')
    views_count = serializers.ReadOnlyField(source='views_count')

    class Meta:
        model = Publication
        fields = ('author', 'title', 'content', 'created_at', 'updated_at', 'views_count')

    def save(self, **kwargs):
        print(**kwargs)
        self.validated_data['author'] = self.context['request'].user
        print(self.validated_data)
        return super().save(**kwargs)


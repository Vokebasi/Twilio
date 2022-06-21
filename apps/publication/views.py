from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PublicationSerializer
from .models import Publication

class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.filter(published=True)
    serializer_class = PublicationSerializer

    def retrieve(self, request, *args, **kwargs):
        publication = self.get_object()
        publication.views_count += 1
        publication.save()
        return super(PublicationViewSet, self).retrieve(request, *args, **kwargs)
        
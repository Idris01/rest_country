from rest_framework import mixins
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CountrySerializer
from .models import Country


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["continent", "common_name"]


class ContinentAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CountrySerializer

    def get_queryset(request, *args, **kwargs):
        name = request.kwargs["continent"]
        return Country.objects.filter(continent__name=name)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

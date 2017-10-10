from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PopShowSerializer, PopMovieSerializer, ActiveUserSerializer, PopGenreSerializer, PopPlanSerializer
from .models import PopShow, PopMovie, ActiveUser, PopGenre, PopPlan

class PopShowViewSet(ModelViewSet):
    serializer_class = PopShowSerializer
    queryset = PopShow.objects.all()

class PopMovieViewSet(ModelViewSet):
    serializer_class = PopMovieSerializer
    queryset = PopMovie.objects.all()

class ActiveUserViewSet(ModelViewSet):
    serializer_class = ActiveUserSerializer
    queryset = ActiveUser.objects.all()

class PopGenreViewSet(ModelViewSet):
    serializer_class = PopGenreSerializer
    queryset = PopGenre.objects.all()

class PopPlanViewSet(ModelViewSet):
    serializer_class = PopPlanSerializer
    queryset = PopPlan.objects.all()

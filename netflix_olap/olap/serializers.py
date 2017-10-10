from rest_framework import serializers
from .models import PopShow, PopMovie, PopPlan, PopGenre, ActiveUser

class PopShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopShow
        fields = ('user_id', 'show_id', 'show_name', 'ratings_id')

class PopMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopMovie
        fields = ('user_id', 'movie_id', 'movie_name', 'ratings_id')

class PopGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopGenre
        fields = ('user_id', 'genre_id', 'genre_name', 'ratings_id')

class PopPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopPlan
        fields = ('user_id', 'plan_id', 'plan_name')

class ActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveUser
        fields = ('user_id', 'watched_num')

from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg



class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        field = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None
    
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(' A data de lançamento nao pode ser anterior a 1900')
        return value
    
    def validate_resume(self, value):
        if len (value) >500:
            raise serializers.ValidationError('Resumo nao deve ser maior do que 500 caracteres.')
        return value


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    avarage_stars = serializers.FloatField()
    
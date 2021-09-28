from rest_framework import serializers
from .models import Profile,Award, Rating, Users,categories, photos

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields='__all__'

class photosSerializer(serializers.ModelSerializer):
    class Meta:
        model = photos
        fields='__all__'

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields='__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields='__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields='__all__'
from rest_framework import serializers
from app.models import Opinion
from app.models import WitsUser
from app.models import user_registrated

class UserRegSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WitsUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = WitsUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.is_active = False
        user.is_activated = False
        user.set_password(validated_data['password'])
        user.save()
        user_registrated.send(UserRegSerializer, instance=user) #sending email
        return user
    

class OpinionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    
    class Meta:
        model = Opinion
        fields = ['id', 'created', 'location', 'caption', 'image', 'owner', 'level']


class UserSerializer(serializers.ModelSerializer):
    opinions = serializers.PrimaryKeyRelatedField(many=True, queryset=Opinion.objects.all())
    
    class Meta:
        model = WitsUser
        fields = ['id', 'username', 'opinions']

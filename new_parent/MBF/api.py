from django.contrib.auth.models import User
from .models import BottleFed, Baby, Family
from rest_framework import serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BottleFedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BottleFed
        fields = ('event_time', 'baby', 'amount')

class BottleFedViewSet(viewsets.ModelViewSet):
    queryset = BottleFed.objects.all()
    serializer_class = BottleFedSerializer

class BabySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baby
        fields = ('first_name', 'last_name', 'birth_date', 'family')

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = ('name',)

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

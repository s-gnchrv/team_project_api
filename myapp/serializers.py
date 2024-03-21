from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from . import models


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['groups'] = list(user.groups.values_list('name', flat=True))
        return token


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.full_name
        return None

    def get_phone(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.phone
        return None

    def get_groups(self, obj):
        return list(obj.groups.values_list('name', flat=True))

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'phone', 'groups')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    representative = UserSerializer()

    class Meta:
        model = models.Organization
        fields = '__all__'


class ViolationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ViolationType
        fields = '__all__'


class ViolationSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.id')
    type = ViolationTypeSerializer()
    project = ProjectSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = models.Violation
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.id')
    violation = ViolationSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = models.Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attachment
        fields = '__all__'




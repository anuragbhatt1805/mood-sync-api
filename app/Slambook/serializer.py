from rest_framework import serializers
from . import models
from Template import models as TemplateModel


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer for Answer model"""
    class Meta:
        model = models.AnswersTemplate
        fields = ('id', 'filled_by', 'created_at', 'slambook', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17')
        read_only_fields = ('id', 'created_at', 'filled_by', 'slambook')


class SlamBookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SlambookTemplate
        fields = ('id', 'name', 'community', 'created_by', 'created_at', 'template')
        extra_kwargs = {
            'created_by': {'read_only': True},
            'created_at': { 'read_only': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Get the question names and update the representation
        template_id = representation.get('template')
        template = TemplateModel.Template.objects.get(id=template_id)
        template_name = template.name

        representation['template'] = {
            'id':template_id,
            "name":template_name
        }

        return representation
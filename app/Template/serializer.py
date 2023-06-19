from rest_framework import serializers
from . import models

class DiaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ('id', 'question_text', 'question_type')

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Template
        fields = ('id', 'name', 'description', 'author', 'created_at', 'updated_at', 'is_active', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17')
        extra_kwargs = {
            'author': {'read_only': True},
            'created_at': { 'read_only': True},
            'updated_at': { 'read_only': True}
        }
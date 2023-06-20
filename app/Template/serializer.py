from rest_framework import serializers
from . import models


class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ('id', 'question_text')
        

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Template
        fields = ('id', 'name', 'description', 'author', 'created_at', 'updated_at', 'is_active', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17')
        extra_kwargs = {
            'author': {'read_only': True},
            'created_at': { 'read_only': True},
            'updated_at': { 'read_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Get the question names and update the representation
        question_ids = [representation.get(f'q{i}') for i in range(1, 18)]
        questions = models.Questions.objects.filter(id__in=question_ids)
        question_names = {question.id: question.question_text for question in questions}

        for i in range(1, 18):
            question_id = representation.get(f'q{i}')
            if question_id in question_names:
                representation[f'q{i}'] = {
                    'id': question_id,
                    "name": question_names[question_id]
                    }

        return representation
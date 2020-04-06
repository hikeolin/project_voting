from rest_framework import serializers
from .models import Poll, Candidate

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ['tvotes', 'category']

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ['id', 'fname', 'lname', 'votes', 'img_link']
        read_only_fields = ['votes']
from .serializers import PollSerializer, CandidateSerializer
from .models import Poll, Candidate
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PollViewSet(viewsets.ViewSet):

    def list(self, req):
        qset = Poll.objects.filter(archived=False)
        serializer = PollSerializer(qset, many=True)
        return Response(serializer.data)

    def retrieve(self, req, pk=None):
        qset = Poll.objects.all()
        poll = get_object_or_404(qset, pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)


class CandidateViewSet(viewsets.ViewSet):

    def list(self, req):
        qset = Candidate.objects.all()
        serializer = CandidateSerializer(qset, many=True)
        return Response(serializer.data)

    def retrieve(self, req, pk=None):
        qset = Candidate.objects.all()
        candidate = get_object_or_404(qset, pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

class PollCandidateViewSet(viewsets.ViewSet):

    def list(self, req, pk=None):
        poll = Poll.objects.get(pk=pk)
        qset = poll.candidate_set.all()
        serializer = CandidateSerializer(qset, many=True)
        return Response(serializer.data)

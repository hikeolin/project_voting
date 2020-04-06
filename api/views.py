from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from rest_framework.response import Response    
from api import permissions as perms 
from api.models import Poll
import json


@api_view(['POST'])
@permission_classes([IsAuthenticated, perms.IsStaff | perms.IsAdmin])
def create_poll(req):
    try:
        data = json.loads(req.body)
        p = Poll.objects.create(**data)
        p.save()
        return Response({'detail': 'resource successfully created'},
        status=status.HTTP_201_CREATED)
    except json.decoder.JSONDecodeError:
        return Response({'detail': 'Unable to process payload body'},
        status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'detail': 'Internal server error'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated, perms.IsStaff | perms.IsAdmin])
def update_poll_profile(req, uid):
    pass

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_poll(req, uid):
    pass

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, perms.IsAdmin])
def delete_poll(req):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated, perms.IsStaff | perms.IsAdmin])
def create_poll_candidate(req, uid):
    pass

@api_view(['PATCH'])
@permission_classes([IsAuthenticated, perms.IsStaff | perms.IsAdmin])
def update_poll_candidate(req, uid):
    pass

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, perms.IsStaff | perms.IsAdmin])
def delete_poll_candidate(req, uid):
    pass 

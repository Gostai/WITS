from django.shortcuts import render
from app.models import Opinion
from app.models import WitsUser
#from django.contrib.auth.models import User
from app.serializers import OpinionSerializer, UserSerializer
from app.serializers import UserRegSerializer
from rest_framework import generics
from rest_framework import permissions
from app.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.core.signing import BadSignature

from .utilities import signer

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
# Create your views here.

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return Response({"success": False, "message":"Activation is unsuccessful"})
    user = get_object_or_404(WitsUser, username=username)
    if user.is_activated:
        message = "User is already activated"
    else:
        message = "User saccesfully activated"
        user.is_active = True
        user.is_activated = True
        user.save()
    return Response({"success": True, "message": message})



class UserRegister(generics.CreateAPIView):
    queryset = WitsUser.objects.all()
    serializer_class = UserRegSerializer

class UserList(generics.ListAPIView):
    queryset = WitsUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = WitsUser.objects.all()
    serializer_class = UserSerializer

class OpinionList(generics.ListCreateAPIView):
    """
    List all opinions, or create a new opinion.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
   
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class OpinionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a opinion instance.
    """    
    
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


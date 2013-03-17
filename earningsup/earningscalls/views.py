from earningscalls.models import EarningsCall
from earningscalls.serializers import EarningsCallSerializer
from earningscalls.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from earningscalls.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'earningscalls': reverse('earningscall-list', request=request, format=format)
    })
    
    
class EarningsCallList(generics.ListCreateAPIView):
    model = EarningsCall
    serializer_class = EarningsCallSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class EarningsCallDetail(generics.RetrieveUpdateDestroyAPIView):
    model = EarningsCall
    serializer_class = EarningsCallSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

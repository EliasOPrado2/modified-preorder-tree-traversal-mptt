from rest_framework import viewsets
from .models import TestTree
from .serializers import TestTreeSerializer

# Create your views here.
class TestTreeViewSet(viewsets.ModelViewSet):
    queryset = TestTree.objects.all()
    serializer_class = TestTreeSerializer
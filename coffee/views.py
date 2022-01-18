from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Coffee
from .serializers import CoffeeSerializer
from .permissions import IsMakerOrReadOnly

class CoffeeList(ListCreateAPIView):
    queryset = Coffee.objects.all()
    model = Coffee
    serializer_class = CoffeeSerializer 

class CoffeeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsMakerOrReadOnly,)
    model = Coffee
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer 


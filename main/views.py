from rest_framework.generics import ListAPIView
from .models import Channels
from .serializers import ChannelSerializer

class ChannelListView(ListAPIView):
    queryset = Channels.objects.all()
    serializer_class = ChannelSerializer

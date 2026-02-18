from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mahsulot
from .serializers import MahsulotSerializer

class MahsulotAPI(APIView):
    def get(self, request):
        malumot = Mahsulot.objects.all() 
        serializer = MahsulotSerializer(malumot, many=True)
        return Response(serializer.data)

    def post(self, request):
        kop_narsami = isinstance(request.data, list)
        serializer = MahsulotSerializer(data=request.data, many=kop_narsami)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        malumot = Mahsulot.objects.get(pk=pk)
        serializer = MahsulotSerializer(malumot, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        malumot = Mahsulot.objects.get(pk=pk)
        malumot.delete()
        return Response({"message": "Mahsulot o'chirildi"})
    
    def patch(self, request, pk):
        malumot = Mahsulot.objects.get(pk=pk)
        serializer = MahsulotSerializer(malumot, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_object(self, pk):
        return Mahsulot.objects.get(pk=pk)
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import ImageSerializer, CategorySerializer
from .models import Image, Category


class FileUploadView(APIView):
    parser_classes = (MultiPartParser)

    def post(self, request, format='png'):
        up_file = request.FILES['img']
        destination = open('./media/images/' + up_file.name,
                           encoding="ISO-8859-1")
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        return Response(up_file)
    # queryset = Image.objects.all()
    # serializer_class = ImageUploadSerializer
    # parser_classes = (MultiPartParser, FormParser)

    # def perform_create(self, serializer, format=None):
    #     # owner = self.request.user
    #     if self.request.data.get('img') is not None:
    #         img = self.request.data.get('img')
    #         serializer.save(img=img)


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

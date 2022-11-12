from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import *
from .serializers import *

# class HelloAPI(APIView):
#     def get(self,request):
#         data = {
#             "xabar":"Get accepted"
#         }
#         return  Response(data)
#     def post(self,request):
#         info = request.data
#         natija ={
#             "xabar":"Info added",
#             "added info":info
#         }
#         return Response(natija)
#
# class SingerAPIView(APIView):
#     def get(self,request):
#         singers = Singer.objects.all()
#         serializer = SingerSerializer(singers,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         singer = request.data
#         serializer = SingerSerializer(data=singer)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"xabar":"saved","added info":serializer.data}
#             return Response(natija,status=status.HTTP_201_CREATED)
#         return Response({"xabar":"error!"})
#
# class SongerAPIView(APIView):
#     def get(self,request,pk):
#         singer = Singer.objects.filter(id=pk)
#         serializer = AlbomSerializer(singer)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         singer = Singer.objects.get(id=pk)
#         serializer = SingerSerializer(singer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"xabar": 'Saqlandi',
#                       "yangi ma'lumot": serializer.data}
#             return Response(natija)
#         return Response({"xabar": "Malumotda xatolik bor!", "detail":serializer.errors})
#
#
#     def delete(self,request,pk):
#         singer = Singer.objects.get(id=pk)
#         singer.delete()
#         return Response({"xabar": "singer deleted"})

class AlbomsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        alboms = Albom.objects.all()
        serializer = AlbomSerializer(alboms,many=True)
        return Response(serializer.data)
    def post(self,request):
        albom = request.data
        serializer = AlbomSerializer(data=albom)
        if serializer.is_valid():
            serializer.save()
            natija = {"albom":"new list saved","added info":serializer.data}
            return Response(natija)
        return Response({"xabar":"error!"})

class AlbomViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    @action(methods=['GET','POST'],detail=True)
    def songs(self,request,pk):
        if request.method =="POST":
            albom = Albom.objects.get(id=pk)
            qoshiq = request.data
            serializer = SongSerializer(data=qoshiq)
            if serializer.is_valid():
                serializer.save(albom=albom)
                natija = {"song":"new song added",'data':serializer.data}
                return Response(natija)
            return Response({'xabar':"smth went wrong!",'detail':serializer.errors})
        songs = Song.objects.filter(albom__id=pk)
        serializer = SongSerializer(songs,many=True)
        return Response(serializer.data)


class SongViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    @action(methods=['GET','POST'],detail=True)
    def alboms(self,request,pk):
        if request.method == "POST":
            song = Song.objects.get(id=pk)
            albom = request.data
            serializer = AlbomSerializer(data=albom)
            if serializer.is_valid():
                serializer.save(song=song)
                natija = {"song":"new song added",'data':serializer.data}
                return Response(natija)
            return Response({'xabar':"smth went wrong!",'detail':serializer.errors})
        alboms = Albom.objects.filter(song__id=pk)
        serializer = AlbomSerializer(alboms,many=True)
        return Response(serializer.data)


class SingerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    @action(methods=['GET',"POST"],detail=True)
    def alboms(self,request,pk):

        if request.method =="POST":
            singer = Singer.objects.get(id=pk)
            albom = request.data
            serializer = AlbomSerializer(data=albom)
            if serializer.is_valid():
                serializer.save(singer=singer)
                natija = {"song":"new albom added",'data':serializer.data}
                return Response(natija)
            return Response({'xabar':"smth went wrong!",'detail':serializer.errors})


        albom = Albom.objects.filter(singer__id=pk)
        serializer = SongSerializer(albom,many=True)
        return Response(serializer.data)



# class OnealbomAPIView(APIView):
#     def get(self,request,pk):
#         albom = Albom.objects.filter(id=pk)
#         serializer = AlbomSerializer(albom,many=True)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         albom = Albom.objects.get(id=pk)
#         serializer = AlbomSerializer(albom, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"song": 'new song added',
#                       "new info": serializer.data}
#             return Response(natija)
#         return Response({"xabar": "Error please check your code"})
#
#     def delete(self, request, pk):
#         albom = Albom.objects.get(id=pk)
#         albom.delete()
#         return Response({"xabar": "song deleted"})
# class SongsAPIView(APIView):
#     def get(self,request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         song = request.data
#         serializer = SongSerializer(data=song)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"albom":"new list saved","added info":serializer.data}
#             return Response(natija)
#         return Response({"xabar":"error!"})
# class SongAPIView(APIView):
#     def get(self,request,pk):
#         song = Song.objects.filter(id=pk)
#         serializer = SongSerializer(song)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         song = Song.objects.get(id=pk)
#         serializer = SongSerializer(song, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"xabar": 'Saqlandi',
#                       "yangi ma'lumot": serializer.data}
#             return Response(natija)
#         return Response({"xabar": "Malumotda xatolik bor!", "detail":serializer.errors})

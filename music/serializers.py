from rest_framework.exceptions import ValidationError

from .models import *
from rest_framework.serializers import ModelSerializer, Serializer

class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__" # ['id','ism']
    def validate_jins(self,qiymat):
        if qiymat.lower() != 'erkak'and qiymat.lower() != 'ayol':
            raise ValidationError("Jins kiritishda xatolik bor")
        return qiymat
    def validate_t_yil(self,year):
        if str(year)>"2004-01-01":
            raise ValidationError("singer mustn't be lower than 18 years old")
        return year


class AlbomSerializer(ModelSerializer):
    class Meta:
        model = Albom
        fields = "__all__"

class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

    def validate_mp3_fayl(self,file):
        if not [".mp3"] in file[-4:].split():
            raise ValidationError("This type isn't support for song")
        return file
    def validate_davomiylik(self,value):
        if int(str(value)[5:7])>10:
            raise ValidationError(f"song's duration is impossible {str(value)} ")
        return value


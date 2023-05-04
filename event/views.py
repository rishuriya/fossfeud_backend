from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import gameRounds, Registered
from .serializer import *
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from django.http import QueryDict

@api_view(['GET'])
def getStudents(request):
    response={}
    getId=request.query_params.get('id')
    print(getId)
    if(getId!=None and len(getId)!=0):
        register = Registered.objects.all().filter(Qrid=getId)
    else:
        register = Registered.objects.all()
    serializer = StudentsSerializer(register, many=True)
    print(serializer.data)
    response["rounds"]=serializer.data
    return Response(response)

@api_view(['GET'])
def getGameRounds(request):
    response={}
    gameName = request.query_params.get('gameName')
    gameID=Games.objects.values('id').filter(Name=gameName)
    if(gameName!=None and len(gameID)!=0):
        round_data= gameRounds.objects.all().filter(Game_id=gameID[0]["id"])
    else:
        round_data= gameRounds.objects.all()
    serializers=RoundsSerilizer(round_data, many=True)
    total_data=len(serializers.data)
    for t in range(total_data):
        total_participants=len(serializers.data[t]["Participants"])
        for i in range(total_participants):
            student=Registered.objects.all().filter(id=serializers.data[t]["Participants"][i])
            studentSerialiser=StudentsSerializer(student, many=True)
            ##studentSerialiser.data.append(studentSerialiser.data[0])
            ##print(studentSerialiser.data)
            serializers.data[t]["Participants"].append(studentSerialiser.data[0])
        for j in range(total_participants):
            serializers.data[t]["Participants"].pop(0)
        game=Games.objects.values().filter(id=serializers.data[t]["Game"])
        gameSerialiser=GamesSerilizer(game,many=True)
        serializers.data[t]["Game"]=gameSerialiser.data
        response["rounds"]=serializers.data
    return Response(response)

@api_view(['POST'])
def postRound(request):
    print(request.data)
    request.data["Name"]="Round "+ request.data["Name"]
    serializer = RoundsSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    serializer = StudentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def loginUser(request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)
    status_code=400
    if user is not None:
        status_code=200
    return Response(status_code)

class GameRoundUpdateView(generics.UpdateAPIView):
    queryset = gameRounds.objects.all()
    serializer_class = RoundsSerilizer

    def put(self, request, *args, **kwargs):
        print(request.data)
        query_dict = QueryDict('', mutable=True)
        query_dict.update(request.data)
        p_list=query_dict.getlist('Participant')[0]
        list_string = map(str, p_list)
        query_dict.pop('Participant')
        query_dict.setlist('Participants', list_string)
        instance = self.get_object()
        print(query_dict)
        serializer = self.serializer_class(instance, data=query_dict)
        if serializer.is_valid():
            serializer.save()
            print("saved")
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("not saved")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
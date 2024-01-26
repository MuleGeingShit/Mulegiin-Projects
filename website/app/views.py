from .models import card
from . serializers import cardSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(["GET",'POST'])
def home(request):
    if request.method == "GET":
        data = card.objects.all()
        serializer = cardSerializer(data,many = True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = cardSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET',"PUT",'DELETE'])
def movie_detail(request,pk):
    try:
        id = card.objects.get(pk=pk)
    except card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = cardSerializer(id)
        return Response(serializer.data)
    

    if request.method == "PUT":
        data = card.objects.get(pk = pk)
        serializer = cardSerializer(data,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    if request.method == "DELETE":
        data = card.objects.get(pk = pk)
        data.delete()
        return Response({'messege':f'{pk} id tai post ustlaa'},status=status.HTTP_204_NO_CONTENT)

    



from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InputSerializer, OutputSerializer
from datetime import datetime

# views handling API using DjangoRestFramework
@api_view(['GET'])
def operation_code(request):
    return Response({'operation_code': 1})

@api_view(['POST'])
def process_data(request):
    serializer = InputSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data['data']
        numbers = [int(x) for x in data if x.isdigit()]
        alphabets = [x.upper() for x in data if x.isalpha()]
        user_id = 'user_rollnumber'
        response_data = {
            'user_id': user_id,
            'is_success': True,
            'numbers': numbers,
            'alphabets': alphabets,
        }
        return Response(response_data)
    return Response({'error': 'Invalid data'}, status=400)

# Views Handling Frontend
def index(request):
    return render(request, 'index.html')
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

# 뷰를 작성할 때 함수를 사용했는지, 클래스를 사용했는지의 차이
# FBV(Function Based View, 함수 기반 뷰) , CBV(Class Based View, 클래스 기반 뷰)

# FBV
@api_view(['GET']) # 데코레이터(Decorator)
def helloApi(request):
    return Response("hello world!")

# CBV
class HelloAPI(APIView):
    def get(self, request, format=None):
        return Response("hello aaa world")
    
@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


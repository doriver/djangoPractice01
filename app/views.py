from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer

from rest_framework import generics, mixins

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

class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):            # GET 메소드 처리 함수(전체 목록)
        return self.list(request, *args, **kwargs)      # mixins.ListModeMixin과 연결
    
    def post(self, request, *args, **kwargs):           # POST 메소드 처리 함수(1권 등록)
        return self.create(request, *args, **kwargs)    # mixins.CreateModeMixin과 연결
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):            # GET 메소드 처리 함수(1권 가져오기)
        return self.retrieve(request, *args, **kwargs)  # mixins.RetrieveModelMixin과 연결
    
    def put(self, request, *args, **kwargs):            # PUT 메소드 처리 함수(1권 수정)
        return self.update(request, *args, **kwargs)    # mixins.UpdateModelMixin과 연결
    
    def delete(self, request, *args, **kwargs):         # DELETE 메소드 처리 함수(1권 삭제)
        return self.destroy(request, *args, **kwargs)   # mixins.DestroyModelMixin과 연결


class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'
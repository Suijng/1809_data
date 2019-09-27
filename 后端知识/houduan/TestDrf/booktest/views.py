from django.shortcuts import render
from .models import Publisher
from .models import *
from app01.serializers import PublisherSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from rest_framework.reverse import reverse
from rest_framework import viewsets

# Create your views here.

@api_view(['GET','POST','DELETE'])
def publisher_list(request,pk):
    if request.method == 'GET': #获取
        try:
            p=Publisher.objects.get(pk=pk)
            s=PublisherSerializers(p)#序列化一个对象
            return Response(s.data,status=status.HTTP_200_OK)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # queruset = Publisher.objects.all()
        # s = PublisherSerializers(queruset,many=True)
        # return Response(s.data)
    elif request.method == 'PUT': #更新
        try:
            p = Publisher.objects.get(pk=pk)#先找到原数据
            p1 = PublisherSerializers(p,data=request.data)
    # else : #创建
    #     p = PublisherSerializers(data= request.data) #序列化
            if p.is_valid(): # 校验数据
                p1.save()
                return Response(p.data,status=status.HTTP_201_CREATED)
            else:
                return Response(p1.errors, status=status.HTTP_400_BAD_REQUEST)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            p = Publisher.objects.get(pk=pk)
            p.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class PubliserDetailView(APIView):
    def get_object(self,pk):
        p = Publisher.objects.get(pk=pk)
        return p
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        p = self.get_object(pk)
        s = PublisherSerializers(p)
        return Response(s.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        p = self.get_object(pk)
        p1 = PublisherSerializers(p,data=request.data)
        if p1.is_valid():
            p1.save()
            return Response(p1,data,status=status.HTTP_201_CREATED)
        else:
            return Response(p1.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        p = self.get_object(pk)





class PublisherListView(mixins.ListModelMixin,
                        mixins.CreateMidelMixin,
                        generics.GenericAPIView):
    queryst = Publisher.objects.all() #指定原数据
    serializers_class = PublisherSerializers #使用的序列化
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class PubliserDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all() #指定原数据
    serializer_class = serializers.PublisherSerializer #使用的序列化


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all() #指定原数据
    serializer_class = serializers.PublisherSerializer #使用序列化


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticated)

#重构视图
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response(
#         {
#             'publishers': reverse('publisher-list', request=request, format=format),
#             'books': reverse('books_list', request=request, format=format)
#         }
#     )



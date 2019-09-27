from django.shortcuts import render

# Create your views here.
from .models import Schools
from rest_framework import status
from rest_framework.response import Response
from utils.pagination import MyPageNumberPagination

from .serializers import SchoolSerializers,SchoolDetailSerializers

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,UpdateModelMixin


#  学校列表
class SchoolView(ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,GenericViewSet):

    queryset = Schools.objects.all()
    serializer_class = SchoolSerializers

    pagination_class = MyPageNumberPagination

    def get_serializer_class(self):
        # 动态设置序列化的类
        if self.action == 'retrieve':
            return SchoolDetailSerializers
        return SchoolSerializers

    def destroy(self, request, *args, **kwargs):
        print('-------------------------------')
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        school_id = kwargs.get('pk')
        if school_id:
            school = Schools.objects.filter(id=school_id)
            serializer = self.get_serializer(school,many=True)
            return Response(serializer.data)


# 学校详情
class SchoolDetailView(CreateModelMixin,UpdateModelMixin,GenericViewSet):

    queryset = Schools.objects.all()
    serializer_class = SchoolDetailSerializers

    def create(self, request, *args, **kwargs):
        ret = {
            'code':1,
            'msg':'添加成功'
        }
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(ret, status=status.HTTP_201_CREATED, headers=headers)
        else:
            # 验证失败打印错误信息
            print(serializer.errors)
            ret['code'] = 0
            ret['msg'] = '参数错误,添加失败'
            return Response(ret)









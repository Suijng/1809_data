from user.models import User,Category,Book,Chpater
from rest_framework import serializers


class ResgsterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(error_messages=
                {
                    'required' :'密码不能为空'
                },
        )

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        import re
        from rest_framework.exceptions import ValidationError
        rea = re.match(r'[A-Z]', value)
        reb = re.search(r'[a-b]', value)
        rec = re.search(r'[0-9]', value)
        red = len(value)

        if rea:
            # 判断首字母大写
            if reb and rec and red > 7:
                return value
            else:
                raise ValidationError('密码格式错误')
        else:
            raise ValidationError('首字母必须大写')




#***************** 分类的序列化
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','info','categoryname']



#***************** 分类下的书籍序列化
class BookSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='bookdetail',lookup_field='id',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = Book
        fields = ['bookname','bauthor','burl','url']


#*********
class BookDetailSerializer(serializers.ModelSerializer):
    bstate = serializers.CharField(source='get_bstate_display')
    category = serializers.CharField(source='category.categoryname')
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    # 书籍章节列表的第一页url地址
    url = serializers.HyperlinkedIdentityField(
        view_name='bookchpaters',lookup_field='id',
        lookup_url_kwarg='bookid'
    )

    class Meta:
        model = Book
        fields = "__all__"



#************** 书籍章节列表的序列化
class ChpaterListSerializer(serializers.ModelSerializer):
    # 获取书籍的名称
    bookname = serializers.CharField(source='book.bookname')
    # 章节详情URL地址
    url = serializers.HyperlinkedIdentityField(
        view_name='chpaterdetail',lookup_field='id',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = Chpater
        # 名称，书籍名称、是否vip章节
        fields = ['chpatername','bookname','chvip','url']


#********
class ChpaterDetailSerializer(serializers.ModelSerializer):
    bookname = serializers.CharField(source='book.bookname')
    bauthor = serializers.CharField(source='book.bauthor')
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Chpater
        fields = '__all__'




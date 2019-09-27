from django.shortcuts import render,redirect
from .models import *
from .forms import UserForm,RegisterForm
from blogusers import admin

import hashlib

# def mymd5(data):
#     return hashlib.md5(data.encode(encoding='utf8')).hexdigest()
#
# class UserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         #自定义操作
#         obj.password = mymd5(request.POST['password'])
#         super().save_model(request,obj,form,change)


# Create your views here.

# def hash_code(s, salt='mysite'):
#     h = hashlib.sha256()
#     s += salt
#     h.update(s.encode())  # update方法只接收bytes类型
#     return h.hexdigest()


def index(request):
    return render(request, 'index.html')


#登录
def login(request):
    if request.session.get('is_login',None): #不能重复
        return  redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请填写内容'
        if login_form.is_valid():
            # username = request.POST.get('username')
            # password = request.POST.get('password')

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # print(username, password)
            # message='所有内容必须填写'
            # if username and password: #用户名和密码不能为空
            #     username = username.strip() #把前后无效空格去掉
            try:
                user = User.objects.get(name=username) #匹配用户名是否存在
                if user.password == hash_code(password): #核对密码
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/') #正确返回首页
                else:
                    message = '密码不正确'
            except:
                message = '用户名不存在'
        return render(request,'login.html',locals()) #不存在返回登录页面
    else:
        login_form = UserForm()
        return render(request, 'login.html',locals())

#注册
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()

    return render(request, 'register.html',locals())


def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/') #没有登录也就不存在退出
    request.session.flush()
    return redirect("/index/")
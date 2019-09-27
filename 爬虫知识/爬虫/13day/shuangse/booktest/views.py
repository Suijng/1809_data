from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

    else:
        hong = request.POST.get('hong')
        lan = request.POST.get('lan')
        hong_list = hong.split(',')

        l = []
        for r in hong_list:
            if int(r) < 10:
                l.append('0' + str(int(r)))
            else:
                l.append(r)



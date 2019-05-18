from django.shortcuts import render
from django.template.context_processors import csrf
from .models import Userinfo
from django.forms.models import model_to_dict

# Create your views here.

def login(request):
    ctx={}
    return render(request, "login.html",ctx)

def showall(request):
    ctx={}
    return render(request, "showall.html",ctx)

def myhtml(request):
    ctx={}
    return render(request, "userinfo.html",ctx)

def add_data(request):
    username=request.POST['username']
    pin = request.POST['passwd']
    userinfo = Userinfo()
    userinfo.username=username
    userinfo.password=pin
    userinfo.save()
    ctx={}
    ctx.update(csrf(request))
    ctx['added']='添加数据成功！'
    return render(request, "userinfo.html",ctx)

def query(request):
    b=Userinfo.objects.all()
    return render(request,'showall.html',{'datas':b})

def delete(request):
    ctx = {}
    return render(request, "delete.html", ctx)

def delete_result(request):
    username = request.POST['username']
    passwd=request.POST['passwd']
    ctx = {}
    ctx.update(csrf(request))
    try:
        a = Userinfo.objects.filter(username=username,password=passwd)
    except:
        ctx['result'] = '输入有误！'
    else:
        if not a.exists():
            ctx['result'] = '数据不存在！'
        else:
            a.delete()
            ctx['result'] = '数据删除！'
        print(a)
    return render(request, "delete.html", ctx)

def search(request):
    ctx = {}
    return render(request, "search.html", ctx)

def find(request):
    userid=request.POST['userid']
    ctx={}
    ctx.update(csrf(request))
    try:
        a=Userinfo.objects.filter(userid=userid)
    except :
        ctx['result'] = '输入有误！'
    else:
        if not a.exists():
            ctx['result'] = '数据不存在！'
        else:
            ctx['result'] = '数据存在！'
        #a=model_to_dict(a)
        ctx['datas']=a
        print(a)
        #return render(request, 'showall.html', {'datas': a})
    return render(request, "search.html",ctx)

def update(request):
    ctx = {}
    return render(request, "update.html", ctx)

def update_result(request):
    username=request.POST['username']
    password = request.POST['passwd']
    update_password = request.POST['update_passwd']
    ctx = {}
    ctx.update(csrf(request))
    try:
        a = Userinfo.objects.filter(username=username,password=password)
    except:
        ctx['result'] = '输入有误！'
    else:
        if not a.exists():
            ctx['result'] = '数据不存在！'
        else:
            a.update(password=update_password)
            ctx['result'] = '数据已变更！'
        print(a)
    return render(request, "delete.html", ctx)
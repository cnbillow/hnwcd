from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,Http404
from women.models import Articles
from women.models import CityNews,Projects,Videos,Abouts,Liuyans
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,InvalidPage
# Create your views here.

def index(request):
    return render(request,'index.html')

# def info(request):
#     infor=Articles.objects.order_by('ArticleID')
#     return render_to_response('info.html',{'info':infor})

def NewsList(request,column_list):
    list = Articles.objects.filter(CategoryID_id=column_list)
    result_list = list[::-1]
    paginator = Paginator(result_list,16)
    page = request.GET.get('page')
    try:
        result = paginator.page(page)
    except (PageNotAnInteger,InvalidPage):
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    
    if result:
        return render(request,'newslist.html',{'info':result})
    else:
        raise Http404
    
def CityNew(request):
    list = CityNews.objects.all()
    result_list = list[::-1]
    paginator = Paginator(result_list,16)
    page = request.GET.get('page')
    try:
        result = paginator.page(page)
    except InvalidPage:
        result = paginator.page(1)
        
    return render(request,'citynews.html',{'city':result})
    

def Project(request):
    result = Projects.objects.all()
    return render(request,'prolist.html',{'prolist':result[::-1]})
    
def Video(request):
    list = Videos.objects.all()
    result_list = list[::-1]
    paginator = Paginator(result_list,16)
    page = request.GET.get('page')
    try:
        result = paginator.page(page)
    except InvalidPage:
        result = paginator.page(1)
    return render(request,'viewlist.html',{'viewlist':result})
    
def About(request):
    result = Abouts.objects.all()
    return render(request,'abouts.html',{'about':result})
    
def Show(request,id):
    result = Articles.objects.filter(ArticleID=id)
    return render(request,'show.html',{'data':result})
    
def ZSShow(request,id):
    result = CityNews.objects.filter(CityNewID=id)
    return render(request,'show.html',{'data':result})

def ByCity(request,cid):
    result = CityNews.objects.filter(CityID_id=cid)
    return render(request,'bycitylist.html',{'data':result,})


def check_code(request):
    import io
    from .backend import check_code as CheckCode
    
    stream = io.BytesIO()
    img, code = CheckCode.create_validate_code()
    img.save(stream,"png")
    request.session["CheckCode"] = code
    return HttpResponse(stream.getvalue())
    
def Comment(request):
    from .forms import Comment
    
    if request.method == 'POST':
        form = Comment(data=request.POST)
        input_code = request.POST.get('check_code')
        #print(input_code.upper(),request.session['CheckCode'].upper())
        flag = input_code.upper() == request.session['CheckCode'].upper()
        if form.is_valid() and flag:
            li = form.cleaned_data['Content']
            comment = Liuyans(Content=li)
            comment.save()
            return redirect("Comment")
        
        else :
            error=r'error'
            form = Comment()
            result = Liuyans.objects.filter(IsShow="true")
            return render(request,'comment.html',{'data':result[::-1],'form':form,'error':error})
            
    else:
        form = Comment()
        result = Liuyans.objects.filter(IsShow="true")
        return render(request,'comment.html',{'data':result[::-1],'form':form,})

def VideoShow(request,id):
    result = Videos.objects.filter(VideoID=id)
    return render(request,'video.html',{'data':result})
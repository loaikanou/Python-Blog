from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogModel as Blog
from .forms import CreateForm

# Create your views here.
def home_page(request):
    return HttpResponse("Hello World !")

def test_arg(request, test_res):
    return HttpResponse(test_res)

def home_template(request):

    query = Blog.objects.all()
    context = {'list':query}

    # return render(request, 'blog/home.html', context={'hello':'Hello Python 3.7'})
    return render(request, 'blog/home.html', context=context)

def post_detail(request, post_id):
    # return HttpResponse(id)
    query = Blog.objects.get(id=post_id)
    context = {'post':query}
    return render(request, 'blog/detail.html', context=context)

def post_create(request):
    # if request.method == "POST":
    #     print(request.POST)

    if request.method == "POST":# اذا نوع الطلب بوست
        author = request.POST['author']# استقبال المدخل اسم الكاتب
        title = request.POST['title']# استقبال المدخل العنوان
        post = request.POST['post']# استقبال المدخل المحتوى
        Blog.objects.create(author=author, title=title, post=post)#اضافة المحتويات الى قاعدة البيانات

    return render(request, 'blog/create.html')

def update(request, post_id):#تستقبل بارمترين البارمتر الثاني الاي دي الخاص بالبيانات
    query = Blog.objects.get(id=post_id)# جلب المعلومات حسب الاي دي
    context = {'object':query}# اضفنا قاموس مفتاح وقيمة القيمة عباره عن البيانات من المتغير
    if request.method == 'POST':# شرط لو كان الارسال من نوع بوست
        author = request.POST['author']# اسندنا البيانات التي استقبلناها لمتغير 
        title = request.POST['title']
        post = request.POST['post']

        query.author = author # قمنا بتغير البيانات حسب البيانات اللي استقبلناها من اليوزر
        query.title = title# نفس ماسبق
        query.post = post# نفس ماسبق
        query.save()# قمنا بحفظ البيانات بعد التعديل 

    return render(request, 'blog/update.html', context)# اعدنا القيمة للقالب update


def add_post(request):
    form = CreateForm(request.POST or None)#نوع الطلب بوست
    if form.is_valid():#شرط للتحقق من المدخلات 
        form.save()# الحفظ الى قاعدة البيانات 
    else:# نفي الشرط
        form = CreateForm # يعيد الفورم للعرض لو لم يتحقق من الشرط

    context = {# شرحناه كثير بالدروس السابقه 
        'form':form
    }
    return render(request, 'blog/add.html', context)

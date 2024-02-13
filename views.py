from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from django.http import HttpResponse
import razorpay
import requests
import decimal



from .forms import SearchForm

# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method=='POST':
        nam=request.POST.get('nm')
        mob=request.POST.get('mb')
        em1=request.POST.get('em')
        pas=request.POST.get('ps1')
        pas2=request.POST.get('ps2')
        obj=reg_tbl.objects.create(fn=nam,mb=mob,em=em1,ps=pas,ps2=pas2)
        obj.save()
        if obj:
            return render(request,"login.html")
        else:
            return render(request,"register.html")
    else:
        return render(request,"register.html")
def login(request):
    if request.method=='POST':
        # nm1=request.POST.get('nm')
        em1=request.POST.get('em')
        pas=request.POST.get('ps')
        obj=reg_tbl.objects.filter(em=em1,ps=pas)
        if obj:
            # request.session['nma']=nm1
            request.session['ema']=em1
            request.session['psa']=pas
            for ls in obj:
                request.session['idn']=ls.id
            return render(request,"main.html")
        else:
            msg="invalid email Id & password"
            # request.session['nma']=''
            request.session['ema']=''
            request.session['psa']=''
            return render(request,"login.html",{'error':msg})
    else:
        return render(request,"login.html")
def main(request):
    return render(request,"main.html")
def medicines(request):
    return render(request,"medicines.html")
def details(request):
    obj=reg_tbl.objects.all()
    return render(request,"details.html",{"data":obj})
def edit(request):
    idno=request.GET.get('idn')
    obj=reg_tbl.objects.filter(id=idno)
    return render(request,"details2.html",{"details":obj})
def update(request):
    if request.method=='POST':
        idno=request.POST.get("idn")
        name1=request.POST.get("nm1")
        mobile1=request.POST.get("mb1")
        email1=request.POST.get("em1")
        password1=request.POST.get("ps1")
        obj=reg_tbl.objects.get(id=idno)
        obj.name=name1
        obj.mobile=mobile1
        obj.email=email1
        obj.password=password1
        obj.save()
        return redirect("/details")
    else:
        return render(request,"details2.html")
def delete(request):
    idl=request.GET.get("idn")
    obj=reg_tbl.objects.filter(id=idl)
    obj.delete()
    return redirect("/details")

def product_list(request):
    products = Product.objects.all()
    return render(request, "addtocart.html", {'products': products})
 

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    request.session['amont_cart']=str(total_price)
    x=float(total_price)
    y=x*100
    request.session['razor_amount']=int(y)
    z=request.session['razor_amount']
    print(z)
    return render(request, "cart.html", {'cart_items': cart_items, 'total_price': total_price})
 

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1

    cart_item.save()
    return HttpResponse("<script>alert('Medicine added to cart');window.location='/product_list';</script>")
 

def remove_from_cart(request, item_id):

    cart_item = CartItem.objects.get(id=item_id)

    cart_item.delete()

    return redirect('userapp:view_cart')
def cart(request):
    return render(request,"cart.html")
def addtocart(request):
    return render(request,"addtocart.html")


def search(request):
    query=request.GET.get('query','')
    products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,"search.html",{
        'query': query,
        'products':products,

    })


def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>")

    return render(request,"contactus.html")
def aboutus(request):
    return render(request,"aboutus.html")

def payment(request, id):
    amount =request.session['razor_amount']
    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_1ggfesqSHVkHcQ", "z0jCd9GhTBQsAAbKdiHrLQc5"))
    x = CartItem.objects.filter(id=id)
    x.update(Payment_status="Done")
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "payment.html")

def payment_page(request):
    return render(request,"payment.html")


def paymentpage(request):
    return render(request,'booking_status.html')


def admin_login(request):
    if request.method=='POST':
        name=request.POST['em']
        passwrd=request.POST['ps']
        try:
            data=admin_loginpage.objects.get(Name=name)
            if data.Password==passwrd:
                return render(request,'adminhome.html')
            else:
                messages.info(request,"password is incorrect")
                return render(request,'adminhome.html')
        except Exception:
            messages.info(request,"password is incorrect")
            return render(request,'adminhome.html')
    else:
        return render(request,'adminhome.html')
    

def adminlogin(request):
    return render(request,"adminlogin.html")

def productspage(request):
    return render(request,"products.html")

def deleteproductpage(request):
    products = Product.objects.all()
    return render(request, "deleteproduct.html", {'products': products})


def products(request):
    if request.method=="POST":
        x=request.POST['name']
        y=request.POST["description"]
        z=request.POST["price"]
        obj=Product.objects.create(name=x,description=y,price=z)
        obj.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/productspage';</script>")
    
def deleteproduct(request,n):
    if request.method=="GET":
        a=Product.objects.filter(name=n)
        a.delete()
        return HttpResponse("<script>alert('Deleted Successfully');window.location='/deleteproductpage';</script>")

# def decrease_quantity(request, product_id):
#     cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#     return redirect('view_cart')

def cartItem(request):
    if request.method=="GET":
       
       cart_items = CartItem.objects.filter(user=request.user)
       total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "cartItem.html", {'cart_items': cart_items, 'total_price': total_price})
 
def registerdetails(request):
    obj=reg_tbl.objects.all()
    return render(request,"registerdetails.html",{"data":obj})

def contactdetails(request):
    obj=Contact.objects.all()
    return render(request,"contactdetails.html",{"data":obj})

def increment_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('userapp:view_cart')

def decrement_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('userapp:view_cart')
# def index(request):
#     return render(request,"index.html")

def logout_view(request):
    return redirect('userapp:index')

def purchase(request):
    if request.method=="POST":
        purchase=Purchase()
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        purchase.name=name
        purchase.email=email
        purchase.address=address
        purchase.save()
        if purchase:
            return render(request,"booking_status.html")
        else:
            return render(request,"purchase.html")
    else:
        return render(request,"purchase.html")

def adminpurchase(request):
    obj=Purchase.objects.all()
    return render(request,"adminpurchase.html",{"data":obj})

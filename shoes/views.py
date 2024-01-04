from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from db.models import Product, Customer, Contacts, CartItem
from django.shortcuts import render, redirect

def home(request):
	return render(request,"home.html")

def login(request):
	return render(request,"login.html")

def signup(request):
	return render(request,"signup.html")

def forget(request):
	return render(request,"forget.html")

def addcart(request):
	return render(request,"addcart.html")

def video(request):
	return render(request,"video.html")

def ordertarking(request):
	return render(request,"order_tarking.html")


def signupafter(request):
	ename = (request.POST["ename"])
	email = (request.POST["email"])
	epassword = (request.POST["epassword"])
	res = Customer( ename = ename, email = email, epassword = epassword)
	res.save()
	return HttpResponse("Data Insert")

def loginafter(request):
	ename = (request.POST["ename"])
	epassword = (request.POST["epassword"])
	showdata = Customer.objects.get(ename = ename, epassword = epassword )
	display={
	'showdata':showdata
	}
	return render(request,"home.html",display)

def addcart(request):
	showdata = Product.objects.all()
	display={
	'showdata':showdata
	}
	return render(request,"addcart.html",display)

def ordertarking(request):
	showdata = Product.objects.all()
	display={		
	'showdata':showdata
	}
	return render(request,"order_tarking.html",display)

def delete(request,product):
	empdata = Product.objects.get(product=product)
	empdata.delete()
	return HttpResponseRedirect('/addcart/')

def Contacts(request):
	cname = (request.POST["cname"])
	cemail = (request.POST["cemail"])
	ccomment = (request.POST["ccomment"])
	res = Contacts( cname = cname, cemail = cemail, ccomment = ccomment)
	res.save()
	return HttpResponse("Thank you")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'D:/shoes/shoes/templates/home.html', {'products': products})
 
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'D:/shoes/shoes/templates/order_traking.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
 

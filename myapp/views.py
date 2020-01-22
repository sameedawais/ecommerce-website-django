from django.http import HttpResponse,request
from django.shortcuts import render,redirect
from .models import product,contact,order,orderupdate
from math import ceil
import json

def index(request):
    # fetch = product.objects.all()
    # n = len(fetch)
    # logic = n//4 + ceil((n/4)-(n//4))
    double_list = []
    fetch_catagories = product.objects.values('product_catagory')
    remove_doubling = {item['product_catagory'] for item in fetch_catagories}
    for i in remove_doubling:
        fetch_items = product.objects.filter(product_catagory=i)
        n = len(fetch_items)
        logic = n//4 + ceil((n/4)-(n//4))
        double_list.append([fetch_items,logic,range(1,n)])
    return render(request,'index.html',{'double_list':double_list})

def searchMatch(query,item):
    if query.lower() in item.product_name.lower() or query.lower() in item.product_catagory.lower() or query.lower() in item.product_desc.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    double_list = []
    fetch_catagories = product.objects.values('product_catagory','id')
    remove_doubling = {item['product_catagory'] for item in fetch_catagories}
    for i in remove_doubling:
        fetch_i = product.objects.filter(product_catagory=i)
        fetch_items = [item for item in fetch_i if searchMatch(query,item)]
        n = len(fetch_items)
        logic = n//4 + ceil((n/4)-(n//4))
        if len(fetch_items) !=0:
            double_list.append([fetch_items,logic,range(1,n)])
        done = {'double_list':double_list,"msg":""}
        if len(double_list) == 0 or len(query)<3:
            done = {'msg':"Please make sure to enter relevant search keyword"}
    return render(request,'search.html',done)

def about(request):
    return render(request,"about.html")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        f_name = request.POST.get('f_name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        description = request.POST.get('address','')
        contact1 = contact(name=name,f_name=f_name,email=email,phone=phone,description=description)
        contact1.save()
    return render(request,"contact.html",{'thank_you':'Thank You for Contacting With Us '})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        try:
            orders = order.objects.filter(order_id=orderId, email=email)
            if len(orders)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for i in update:
                    updates.append({'text':i.update_desc, 'time':i.timestamp})
                    response = json.dumps([updates, orders[0].item_name], default=str)
                    return HttpResponse(response)
            else:
                return HttpResponse('else')

        except Exception as e:
            return HttpResponse('{}')

    return render(request,"tracker.html")



def productview(request,id):
    fetch_data = product.objects.filter(id=id)
    return render(request,"productview.html",{'fetch_data':fetch_data})

def checkout(request):
    if request.method=='POST':
        items_Json = request.POST.get('itemsJson','')
        amount = request.POST.get('amount','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        country = request.POST.get('country','')
        city = request.POST.get('city','')
        zip_code = request.POST.get('zip_code','')
        order1 = order(item_name=items_Json,name=name,email=email,phone=phone,address=address,country=country,city=city,zip_code=zip_code,price=amount)
        order1.save()
        update1 = orderupdate(order_id=order1.order_id, update_desc = "Order has been placed")
        update1.save()
        thank = True
        id = order1.order_id
        return render(request,"checkout.html",{'thank':thank,'id':id})
    return render(request,"checkout.html")
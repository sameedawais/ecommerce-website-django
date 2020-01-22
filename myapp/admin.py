from django.contrib import admin

# Register your models here.
from .models import product,contact,order,orderupdate

class mydata(admin.ModelAdmin):
    list_display= ('product_name','product_catagory','product_subcatagory','product_desc','product_time','product_image')
admin.site.register(product,mydata)


class contactdata(admin.ModelAdmin):
    list_display = ('name','f_name','email','phone','description')
admin.site.register(contact,contactdata)

class orderdata(admin.ModelAdmin):
    list_display = ('item_name','name','email','phone','address','country','city','zip_code','price')
admin.site.register(order,orderdata)

class updatedata(admin.ModelAdmin):
    list_display = ('order_id','update_desc','timestamp')
admin.site.register(orderupdate,updatedata)
from django.db import models

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    product_catagory = models.CharField(max_length=100,default="")
    product_subcatagory = models.CharField(max_length=100,default="")
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=400)
    product_time = models.DateField()
    product_image = models.ImageField(upload_to="shop/images",default="")
    class Meta:
        db_table="product"

class contact(models.Model):
    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    description = models.CharField(max_length=500)
    class Meta:
        db_table="contact"

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=5000,default="")
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=40,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    country = models.CharField(max_length=20,default="")
    city = models.CharField(max_length=20,default="")
    zip_code = models.CharField(max_length=20,default="")
    price = models.CharField(max_length=200,default="")
    class Meta:
        db_table="order"

class orderupdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    class Meta:
        db_table="orderupdate"
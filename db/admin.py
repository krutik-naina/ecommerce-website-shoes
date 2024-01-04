from django.contrib import admin

# Register your models here.

from db.models import Customer
class CustomerAdmin(admin.ModelAdmin):
	list_listview = ('ename','email','epassword')
admin.site.register(Customer,CustomerAdmin)


from db.models import Product
class ProductmAdmin(admin.ModelAdmin):
	list_listview = ('imag','products','price')
admin.site.register(Product,ProductmAdmin)

from db.models import Contacts
class ContactsAdmin(admin.ModelAdmin):
	list_listview = ('cname','cemail','ccomment')
admin.site.register(Contacts,ContactsAdmin)

from db.models import CartItem
admin.site.register(CartItem)

from django.contrib import admin
from products.models import ProductMen, ProductMenImage, Variation , ProductWomen, ProductWomenImage, ProductKids, ProductKidsImage, ProductAccessory, ProductAccessoriesImage

# Register your models here.


# ProductMen, ProductMenImage, ProductWomen, ProductWomenImage, ProductKids, ProductKidsImage, ProductAccessories, ProductAccessoriesImage

class ProductMenAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title','description']
    list_display = ['__str__','title', 'price', 'timestamp','updated','active']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {'slug':('title',)}

    class Meta:
        model = ProductMen

class ProductWomenAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title','description']
    list_display = ['__str__','title', 'price', 'timestamp','updated','active']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {'slug':('title',)}

    class Meta:
        model = ProductWomen

class ProductKidsAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title','description']
    list_display = ['__str__','title', 'price', 'timestamp','updated','active']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {'slug':('title',)}

    class Meta:
        model = ProductKids

class ProductAccessoriesAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title','description']
    list_display = ['__str__','title', 'price', 'timestamp','updated','active']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {'slug':('title',)}

    class Meta:
        model = ProductAccessory

admin.site.register(ProductMen, ProductMenAdmin)
admin.site.register(Variation)
admin.site.register(ProductWomen, ProductWomenAdmin)
admin.site.register(ProductKids, ProductKidsAdmin)
admin.site.register(ProductAccessory, ProductAccessoriesAdmin)
admin.site.register(ProductMenImage)
admin.site.register(ProductWomenImage)
admin.site.register(ProductKidsImage)
admin.site.register(ProductAccessoriesImage)
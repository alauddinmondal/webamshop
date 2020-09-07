from django.db import models
from django.urls import reverse

# Create your models here.


class ProductMen(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title','slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('mdressdetails', args=[self.slug])
        return reverse('mdressdetails', kwargs={'slug':self.slug})


class ProductMenImage(models.Model):
    productmen = models.ForeignKey(ProductMen, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/men')
    menimgalt = models.CharField(max_length=120, null=True, blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.productmen.title


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')

VAR_CATEGORIES = (
    ('size','size'),
    ('color','color'),
    ('package','package'),
)

class Variation(models.Model):
    productmen = models.ForeignKey(ProductMen, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductMenImage, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    object = VariationManager()




class ProductWomen(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title','slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('femaledressdetails', kwargs={'slug':self.slug})
       

class ProductWomenImage(models.Model):
    productwomen = models.ForeignKey(ProductWomen, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/women')
    wmenimgalt = models.CharField(max_length=120, null=True, blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.productwomen.title


class ProductKids(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title','slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('kidsdressdetails', kwargs={'slug':self.slug})
       

class ProductKidsImage(models.Model):
    productkids = models.ForeignKey(ProductKids, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/kids')
    kidsimgalt = models.CharField(max_length=120, null=True, blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.productkids.title


class ProductAccessory(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title','slug') 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('accessdressdetails', kwargs={'slug':self.slug})
       

class ProductAccessoriesImage(models.Model):
    productaccessory = models.ForeignKey(ProductAccessory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/accessories')
    accessimgalt = models.CharField(max_length=120, null=True, blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.productaccessory.title

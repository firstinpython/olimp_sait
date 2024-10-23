from django.contrib import admin
from .models import Posts,Services,Time,Review,HeaderThings
# Register your models here.
admin.site.register(Posts)
admin.site.register(Services)
admin.site.register(Time)
admin.site.register(Review)
admin.site.register(HeaderThings)
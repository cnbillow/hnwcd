from django.contrib import admin
from .models import Abouts,Branches,Categories,Articles,Cities,CityNews,Donates,Links,Liuyans,People,ProCates,Projects,ProNews,Qrs,Users,Videos,Years,img
from image_cropping import ImageCroppingMixin


# Register your models here.
class AboutsAdmin(admin.ModelAdmin):
    list_display=('Title','PublishDate','Rank',)
    
class BranchesAdmin(admin.ModelAdmin):
    list_display=('Name','Rank')

class CategoriesAdmin(admin.ModelAdmin):
    list_display=('Name','CategoryID',)

class ArticlesAdmin(admin.ModelAdmin):
    list_display=('Title','CategoryID','Author','PublishDate')
    
class CitiesAdmin(admin.ModelAdmin):
    list_display=('Name','Rank')

class CityNewsAdmin(admin.ModelAdmin):
    list_display=('Title','Author','PublishDate')
    
class DonatesAdmin(admin.ModelAdmin):
    list_display=('Name','Time','Money')

class LinksAdmin(admin.ModelAdmin):
    list_display=('Name','LinkURL','Rank')

class LiuyansAdmin(admin.ModelAdmin):
    list_display=('LId','Time','Content')

class PeopleAdmin(admin.ModelAdmin):
    list_display=('Name','BranchID')

class ProCatesAdmin(admin.ModelAdmin):
    list_display=('Name','ProCateID')

class ProjectsAdmin(admin.ModelAdmin):
    list_display=('ProName','Author','Time','YearID','ProCateID')

class ProNewsAdmin(admin.ModelAdmin):
    list_display=('Title','ProID','Author','PublishDate')
    
class QrsAdmin(admin.ModelAdmin):
    list_display=('Name','QID')

class UsersAdmin(admin.ModelAdmin):
    list_display=('UserName','Password','IsSuper')
    
class VideosAdmin(admin.ModelAdmin):
    list_display=('Title','Author','Time')

class YearsAdmin(admin.ModelAdmin):
    list_display=('YearName','YearID')

admin.site.register(Abouts,AboutsAdmin)
admin.site.register(Branches,BranchesAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Cities,CitiesAdmin)
admin.site.register(CityNews,CityNewsAdmin)
admin.site.register(Donates,DonatesAdmin)
admin.site.register(Links,LinksAdmin)
admin.site.register(Liuyans,LiuyansAdmin)
admin.site.register(People,PeopleAdmin)
admin.site.register(ProCates,ProCatesAdmin)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(ProNews,ProNewsAdmin)
admin.site.register(Qrs,QrsAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Videos,VideosAdmin)
admin.site.register(Years,YearsAdmin)

class imgAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('image','cropping')

admin.site.register(img,imgAdmin)


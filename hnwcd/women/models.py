from django.db import models
from DjangoUeditor.models import UEditorField
from image_cropping import ImageCropField, ImageRatioField

# Create your models here.
class Abouts(models.Model):
    AbID=models.AutoField(primary_key=True,)
    Title=models.CharField('标题',max_length=256)
    Content=UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    PublishDate=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    Rank=models.IntegerField('顺序',unique=True,blank=True)
    
    def __str__(self):
        return self.Title
    
    
    class Meta:
        verbose_name='关于我们'
        verbose_name_plural='关于我们'
        
        
class Branches(models.Model):
    BranchID=models.AutoField(primary_key=True,)
    Name=models.CharField('姓名',max_length=50)
    Content=UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='mini', filePath='uploads/files/') 
    Rank=models.IntegerField('顺序',unique=True,blank=True)

    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name='理事会职位'
        verbose_name_plural='理事会职位'
        ordering=['BranchID']
        
        
class Categories(models.Model):
    CategoryID=models.AutoField('文章分类',primary_key=True,)
    Name=models.CharField('类别',max_length=20)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name='类别名称'
        verbose_name_plural='类别名称'
        ordering=['CategoryID']
        
        
class Articles(models.Model):
    isCheckChoice=(
        ('1','是'),
        ('0','否'),
    )
    isTopChoice=(
        ('1','是'),
        ('0','否'),
    )
    
    ArticleID=models.AutoField(primary_key=True,)
    Title=models.CharField('文章标题',max_length=256)
    Author=models.CharField('作者',max_length=256,null=True)
    Content=UEditorField('文章内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    PublishDate=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    #CategoryID=models.IntegerField('ID')
    #CategoryID=models.ManyToManyField(Categories,verbose_name='所属类别')
    CategoryID=models.ForeignKey(Categories)
    
    #isCheck=models.IntegerField(default=1)
    isCheck=models.CharField('是否审核',max_length=1,choices=isCheckChoice,default='0')
    
    #isTop=models.IntegerField(default=0)
    isTop=models.CharField('是否置顶',max_length=1,choices=isCheckChoice,default='0')
    Count=models.IntegerField('阅读次数',default=1,null=True)
    
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name='文章'
        verbose_name_plural='文章'
     
    
class Cities(models.Model):
    CityID=models.AutoField(primary_key=True,)
    Name=models.CharField('城市名字',max_length=56)
    Rank=models.IntegerField('顺序',unique=True,blank=True)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name='市州ID'
        verbose_name_plural='市州ID'
        ordering=['CityID']

        
class CityNews(models.Model):
    isCheckChoice=(
        ('1','是'),
        ('0','否'),
    )

    CityNewID=models.AutoField(primary_key=True,)
    Title=models.CharField('标题',max_length=56)
    Author=models.CharField('作者',max_length=56)
    Content=UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    PublishDate=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    #CityID=models.IntegerField('城市')
    CityID=models.ForeignKey("Cities",to_field="CityID")
    isCheck=models.CharField('是否审核',max_length=1,choices=isCheckChoice,default='0')
    Count=models.IntegerField(null=True)

    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name='市州动态'
        verbose_name_plural='市州动态'
        

class Donates(models.Model):
    Donate=models.AutoField(primary_key=True,)
    Name=models.CharField('姓名',max_length=56)
    Time=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    Money=models.DecimalField('捐赠金额',max_digits=16,decimal_places=2)

    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name='爱心捐赠'
        verbose_name_plural='爱心捐赠'

        
class Links(models.Model):
    LinkID=models.AutoField(primary_key=True,)
    Name=models.CharField('姓名',max_length=56)
    LinkURL=models.CharField('网址',max_length=256)
    Rank=models.IntegerField('顺序',unique=True,blank=True)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name="友情链接"
        verbose_name_plural='友情链接'
        

class Liuyans(models.Model):
    IsShowChoice=(
        ('true','是'),
        ('false','否'),
    )
    LId=models.AutoField(primary_key=True,)
    Content=UEditorField('留言内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='', filePath='uploads/files/')
    IsShow=models.CharField('是否显示',default='false',null='True',max_length=56,choices=IsShowChoice)
    Time=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    Reply=UEditorField('留言回复', null='True', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='mini', filePath='uploads/files/')
    
    def __str__(self):
        return self.Content

    class Meta:
        verbose_name="网友留言"
        verbose_name_plural='网友留言'
        
class People(models.Model):
    PId=models.AutoField(primary_key=True,)
    Name=models.CharField('姓名',max_length=56)
    Position=models.CharField('职务',max_length=56)
    Content=UEditorField('具体职务', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='', filePath='uploads/files/')
    #BranchID=models.IntegerField('职务ID',blank=True)
    BranchID=models.ForeignKey(Branches)
    isCheck=models.IntegerField(default=1)
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name="理事会机构"
        verbose_name_plural='理事会机构'


class ProCates(models.Model):
    ProCateID=models.AutoField(primary_key=True,)
    Name=models.CharField('公益类型',max_length=56)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name="公益类型"
        verbose_name_plural='公益类型'


class Years(models.Model):
    YearID=models.AutoField(primary_key=True,)
    YearName=models.CharField('年份',max_length=10)

    def __str__(self):
        return self.YearName
    
    class Meta:
        verbose_name='年份'
        verbose_name_plural='年份'
        ordering=['-YearID']


class Projects(models.Model):
    IsCheckChoice=(
        ('1','是'),
        ('0','否'),
    )
    IsIndexChoice=(
        ('true','是'),
        ('false','否'),
    )
    IsFriendChoice=(
        ('true','是'),
        ('false','否'),
    )
    
    ProID=models.AutoField(primary_key=True,)
    ProName=models.CharField('公益项目',max_length=56)
    Author=models.CharField('作者',max_length=50,null=True)
    Content=UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='mini', filePath='uploads/files/')
    ImgURL=UEditorField('图片',
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='pic', filePath='uploads/files/')
    IsFriend=models.CharField(max_length=5,choices=IsFriendChoice,default='false')
    Time=models.DateTimeField('开始时间',auto_now_add=True,editable=True)
    #YearID=models.IntegerField(default=0)
    YearID=models.ForeignKey(Years)
    #ProCateID=models.IntegerField(default=0)
    ProCateID=models.ForeignKey(ProCates)
    IsIndex=models.CharField('是否置顶',max_length=5,choices=IsIndexChoice,default='false')
    IsCheck=models.CharField('是否审核',max_length=1,choices=IsCheckChoice,default='0')
    
    def __str__(self):
        return self.ProName

    class Meta:
        verbose_name="公益项目"
        verbose_name_plural='公益项目'
        

class ProNews(models.Model):
    IsCheckChoice=(
        ('1','是'),
        ('0','否'),
    )
    
    ProNewID=models.AutoField(primary_key=True,)
    Title=models.CharField('标题',max_length=56)
    Author=models.CharField('作者',max_length=50,null=True)
    Content=UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='mini', filePath='uploads/files/')
    PublishDate=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    #ProID=models.IntegerField(default=0)
    ProID=models.ForeignKey(Projects)
    IsCheck=models.CharField('是否审核',max_length=1,choices=IsCheckChoice,default='0')

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name="公益新闻"
        verbose_name_plural='公益新闻'


class Qrs(models.Model):
    QID=models.AutoField(primary_key=True,)
    Name=models.CharField('名字',max_length=56)
    ImgURL=UEditorField('图片', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='pic', filePath='uploads/files/')
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name="滚动图"
        verbose_name_plural='滚动图'
        

class Users(models.Model):
    UserID=models.AutoField(primary_key=True,)
    UserName=models.CharField('用户名',max_length=56)
    Password=models.CharField('密码',max_length=56)
    IsSuper=models.CharField(max_length=56)
    
    def __str__(self):
        return self.UserName
    
    class Meta:
        verbose_name='用户'
        verbose_name_plural='用户'   
        
class Videos(models.Model):
    IsIndexChoice=(
        ('true','是'),
        ('false','否'),
    )
    VideoID=models.AutoField(primary_key=True,)
    Title=models.CharField('标题',max_length=56)
    Author=models.CharField('作者',max_length=56)
    Content=UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='mini', filePath='uploads/files/')
    Time=models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    FilePath=UEditorField('视频',
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='video', filePath='uploads/files/')
    Rank=models.IntegerField('顺序',null=True,blank=True)
    Isindex=models.CharField('是否置顶',max_length=5,choices=IsIndexChoice,default='false')
    PicPath=UEditorField('图片',
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='pic', filePath='uploads/files/')
    Count=models.IntegerField(blank=True,default=1)
    
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name='爱心视频'
        verbose_name_plural='爱心视频'
        
from image_cropping import ImageCropWidget
class img(models.Model):
    image=ImageCropField(blank=True, upload_to='uploaded/images/')
    cropping = ImageRatioField('image', '700x700')
    
    # class Meta:
    #     widgets = {
    #         'image': ImageCropWidget,
    #     }



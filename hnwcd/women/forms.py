from django import forms
from women.models import Liuyans

class Comment(forms.ModelForm):
    Content = forms.CharField(
      label="留言内容",required=True,error_messages={'required':'111'},
      widget=forms.Textarea(attrs={'placeholder':'plz留言内容'})
      )
    
    class Meta:
        model = Liuyans
        fields = ("Content",)
        
    def clean_Content(self):
            Content = self.cleaned_data['Content']
            return Content
        
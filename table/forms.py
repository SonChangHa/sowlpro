from django import forms

from .models import FreeTable, NoticeTable

class FreeTableForm(forms.ModelForm):

    class Meta:
        model = FreeTable
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':"제목을 입력하세요.", 'name':"subject", 'class':"form-control"}),
            'text': forms.Textarea(attrs={'cols':"10", 'placeholder':"내용을 입력하세요.", 'class':"form-control", 'name':"content"})
        }
        labels = {
            'title': '글 제목',
            'text': '글 내용'
        }
    def __init__(self, *args, **kwargs):
        super(FreeTableForm, self).__init__( *args, **kwargs)

class NoticeTableForm(forms.ModelForm):
    class Meta:
        model = NoticeTable
        fields = ('title', 'text',)
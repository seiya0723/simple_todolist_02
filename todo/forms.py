#モデルのフィールド定義を継承し、フォームとする。
from .models import Todolist
from django import forms
from django.forms import ModelForm,Textarea,DateTimeInput


#ModelFormを継承し、Metaクラスに利用するモデルクラス名、フィールド、ウィジェット等を記述。モデルを継承したフォームは教科書P91を参照。
class TodolistForm(ModelForm):
    class Meta:
        model   = Todolist
        widgets = { "deadline":DateTimeInput(attrs={"class":"form-control my-2","autofocus":"","value":"2020-09-17 14:30:00"} ),
                    "content":Textarea(attrs={"class":"form-control my-2","placeholder":"ここにやることを入力する","rows":"3"} ),
                    }
        fields  = [ "deadline","content" ]


#モデルを継承せずにフォームを1から作る場合は、Formを継承
#【注意】モデルで定義したidは編集不可(editable=False)の要素のため、継承することができない
class TododeleteForm(forms.Form):
    todo_delete  = forms.UUIDField()

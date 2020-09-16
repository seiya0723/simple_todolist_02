from django.contrib import admin
from .models import Todolist
from .forms import TodolistForm

class TodolistModelAdmin(admin.ModelAdmin):
    #一覧表示時に表示させるカラム
    list_display    = ["id","deadline","content"]
    #並び替え
    ordering        = ["deadline"]
    #管理画面で編集できるカラム
    fields          = ["deadline","content"]

    #フォームのデザインをforms.pyで定義したものを使用しない場合、継承する必要はない(Adminではバリデーションチェック自動)
    #【注意】DateTimeFieldは、Adminでアクセスして編集、送信を行う際、日付と時刻が一緒くたになったフォームを作って編集、送信を行うことはできない。詳しくは『Enter a list of values.』で検索
    #【詳細】https://stackoverflow.com/questions/56035838/what-does-the-error-enter-a-list-of-values-mean-using-jquery-datetimepicker


#管理画面でTODOリストのテーブルを操作できるようにする
admin.site.register(Todolist,TodolistModelAdmin)



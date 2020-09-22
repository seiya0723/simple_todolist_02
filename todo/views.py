from django.shortcuts import render

# Create your views here.
from django.views import View

#モデルとフォームを読み込む
from .models import Todolist
from .forms import TodolistForm,TododeleteForm


from django.utils import timezone

#Viewを継承してGET文、POST文の関数を作る。教科書P35にクラスベースのビュー関数の書き方が解説されている
class TodoView(View):

    def reference(self):
        form        = TodolistForm()
        data        = Todolist.objects.order_by("deadline")

        return form,data

    def get(self, request, *args, **kwargs):

        form,data   = self.reference()
        context     = { "data"  : data,
                        "form"  : form }

        #render(レスポンス返すために必要になるリクエスト,レンダリングするテンプレートのパス,レンダリング対象に与える変数)
        return render(request,"todo/index.html",context)

    def post(self, request, *args, **kwargs):

        #TODOリストの作成
        if "deadline" in request.POST and "content" in request.POST:
            print(request.POST)

            #教科書P87の『ビューでの利用例』を参照。フォームのバリデーション結果で処理を切り替える
            formset = TodolistForm(request.POST)
            if formset.is_valid():
                formset.save()
            else:
                print("バリデーションエラー")
        

        #TODOリストの削除
        if "todo_delete" in request.POST:

            print(request.POST)
            
            formset = TododeleteForm(request.POST)
            if formset.is_valid():

                #バリデーションOKの場合、受け取った内容をクリーン化(教科書P94の緑部分)、削除のクエリを実行させる(fillterは教科書P57、deleteはP62)
                clean_data  = formset.clean()
                Todolist.objects.filter(id=clean_data["todo_delete"]).delete()
            else:
                print("バリデーションエラー")


        form,data   = self.reference()
        context     = { "data"  : data,
                        "form"  : form }

        return render(request,"todo/index.html",context)

#↓クラスベースのビューを関数化させるメソッドが.as_view()。教科書P36と config/urls.pyの英語の解説部分を参照
index       = TodoView.as_view()

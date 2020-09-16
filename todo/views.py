from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Todolist
from .forms import TodolistForm,TododeleteForm


from django.utils import timezone

#Viewを継承してGET文、POST文の関数を作る
class TodoView(View):

    def reference(self):
        form        = TodolistForm()
        data        = Todolist.objects.order_by("deadline")

        return form,data

    def get(self, request, *args, **kwargs):

        form,data   = self.reference()
        context     = { "data"  : data,
                        "form"  : form }

        return render(request,"todo/index.html",context)

    def post(self, request, *args, **kwargs):

        #TODOリストの作成
        if "deadline" in request.POST and "content" in request.POST:

            """
            #バリデーション無しでそのままDBに記録する方法
            posted  = Todolist( deadline    = request.POST["deadline"],
                                content     = request.POST["content"],
                                )
            posted.save()
            """

            #バリデーションをした上でDBに記録する方法
            data    = { "deadline"    : request.POST["deadline"],
                        "content"     : request.POST["content"],
                        }
            #forms.pyで定義したバリデーションに倣って、ユーザが入力したデータを代入。formsetオブジェクトを生成する
            formset = TodolistForm(data)

            if formset.is_valid():
                formset.save()
            else:
                print("バリデーションエラー")
        

        #TODOリストの削除
        if "todo_delete" in request.POST:

            """
            target_id   = request.POST["todo_delete"].replace("-","")

            posted  = Todolist.objects.filter(id=target_id)
            posted.delete()
            """

            data    = { "id"    : request.POST["todo_delete"],
                        }
            formset = TododeleteForm(data)

            #【注意】formのバリデーションを経由させることで、文字列型ではなくUUID型となりreplaceによる変換処理は不要になる。
            if formset.is_valid():
                clean_data  = formset.clean()
                Todolist.objects.filter(id=clean_data["id"]).delete()
            else:
                print("バリデーションエラー")


        data  = Todolist.objects.order_by("deadline")

        form,data   = self.reference()
        context     = { "data"  : data,
                        "form"  : form }

        return render(request,"todo/index.html",context)

index       = TodoView.as_view()



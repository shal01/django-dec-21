from django.shortcuts import render,redirect

from todoapp.forms import TodoForm,UserRegistrationForm,LoginForm,TodoUpdateForm,UserProfileForm
from todoapp.models import Todos,UserProfile
from django.views.generic import View,ListView,UpdateView,DetailView,CreateView
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from todoapp.decorting import signin_required
from django.urls import reverse_lazy


class SignUpView(View):
    template_name="registration.html"
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{"form":form})
        form.save()
        return redirect("sign-in")


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"log_in.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("login success")
                return redirect("alltodos")
            else:
                print("login failed")
                return redirect("sign-in")
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("sign-in")

















@method_decorator(signin_required,name="dispatch")
class TodoCreateView(CreateView):
    model=Todos
    form_class = TodoForm
    template_name = "addtodo.html"
    success_url = reverse_lazy('alltodos')



    # def get(self,request):
    #     form=TodoForm()
    #     return render(request,"addtodo.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=TodoForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         print(form.cleaned_data)
    #         # todo=form.save(commit=False)
    #         # todo.user=request.user
    #         # todo.save()
    #         form.save()
    #         print("Todo created")
    #         return redirect("alltodos")

            # Todos.objects.create(
            #     task_name=form.cleaned_data.get("task_name"),
            #     user=form.cleaned_data.get("user"),
            #     status=form.cleaned_data.get("completed_status")
            # )

            # return redirect("alltodos")
        # else:
            # return render(request,"addtodo.html",{"form":form})
        #     return redirect("addtodo")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



@method_decorator(signin_required,name="dispatch")
class TodoDetails(DetailView):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     todo=Todos.objects.get(id=id)
    #     return render(request,"details.html",{"todo":todo})
    model = Todos
    template_name = "detail.html"
    context_object_name = "todo"
    pk_url_kwarg = "id"

@method_decorator(signin_required,name="dispatch")
class TodoEditView(UpdateView):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     form=TodoForm(instance=todo)
    #     return render(request,"Todo_edit.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #         id = kwargs.get("id")
    #         todo = Todos.objects.get(id=id)
    #         form=TodoForm(request.POST,instance=todo)
    #         if not form.is_valid():
    #             return render(request, "Todo_edit.html", {"form": form})
    #         form.save()
    #         return redirect("alltodos")
    model = Todos
    template_name = "Todo_edit.html"
    form_class = TodoUpdateForm
    success_url = reverse_lazy("alltodos")
    pk_url_kwarg = "id"



@method_decorator(signin_required,name="dispatch")
class TodoListView(ListView):
    # def get(self, request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #         qs=Todos.objects.filter(user=request.user)
    #         return render(request, 'todolist.html', {'todos': qs})
    #     else:
    #         return redirect("sign-in")
    model = Todos
    template_name = "todolist.html"
    context_object_name ='todos'
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)


@method_decorator(signin_required,name="dispatch")
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return redirect("alltodos")





@method_decorator(signin_required,name="dispatch")
class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name ="user_profile.html"
    success_url = reverse_lazy('alltodos')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)









# Create your views here.
# function base view and class based view

# def registration(request):
#     print(request)
#     return render(request,"registration.html")
#
# def signin(request):
#     print(request)
#     return render(request,"login.html")
#
# def index(request):
#     return HttpResponse("<h1> Welcome user <h2>")
from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from django.contrib.auth import authenticate, login as dj_login,logout as django_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import UserRole,SysFeature,RoleCode,SysFeatureRole,PermissionType

from django.urls import reverse
from .forms import SignUpForm,RoleCodeForm,SysFeatureForm,UserRoleForm,SysFeatureRoleForm
import csv,io
# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'login.html')

def admin_portal(request):
    return render(request, 'admin_portal/list_user.html')

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            dj_login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            context['error'] = 'Provide valid credential'
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'admin_portal/signup.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'admin_portal /change_password.html', {
        'form': form
    })


def list_user(request):
    users = User.objects.all()
    return render(request, 'admin_portal/list_user.html', { 'users': users})


def list_userrole(request):
    userroles = UserRole.objects.all()
    return render(request, 'admin_portal/list_userrole.html', { 'userroles': userroles})


def manage_role(request):
    users = User.objects.all()
    roles = RoleCode.objects.all()
    form = UserRoleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_userrole')
    return render(request, 'admin_portal/manage_role.html', { 'users': users, 'roles': roles})


def add_user(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_user')
    return render(request, 'admin_portal/add_user.html', {'form':form})


def edit_user(request, pk):
    user= get_object_or_404(User, pk=pk)
    form = SignUpForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('list_user')
    return render(request, 'admin_portal/edit_user.html', {'form':form})


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        user.delete()
        return redirect('list_user')
    return render(request, 'admin_portal/user_confirm_delete.html', {'object':user})


def delete_userrole(request, pk):
    userrole = get_object_or_404(UserRole, pk=pk)
    if request.method=='POST':
        userrole.delete()
        return redirect('list_userrole')
    return render(request, 'admin_portal/userrole_confirm_delete.html', {'object':userrole})


def list_role(request):
    roles = RoleCode.objects.all()
    return render(request, 'admin_portal/list_role.html', { 'roles': roles})


def add_role(request):
    form = RoleCodeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_role')
    return render(request, 'admin_portal/add_role.html', {'form':form})


def edit_role(request, pk):
    rolecode= get_object_or_404(RoleCode, pk=pk)
    form = RoleCodeForm(request.POST or None, instance=rolecode)
    if form.is_valid():
        form.save()
        return redirect('list_role')
    return render(request, 'admin_portal/edit_role.html', {'form':form})


def delete_role(request, pk):
    rolecode= get_object_or_404(RoleCode, pk=pk)
    if request.method=='POST':
        rolecode.delete()
        return redirect('list_role')
    return render(request, 'admin_portal/role_confirm_delete.html', {'object':rolecode})


def list_feature(request):
    features = SysFeature.objects.all()
    return render(request, 'admin_portal/list_feature.html', { 'features': features})


def add_feature(request):
    form = SysFeatureForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_feature')
    return render(request, 'admin_portal/add_feature.html', {'form':form})


def import_feature(request):
    template = 'admin_portal/import_feature.html'

    prompt = {
        'order' : 'Order of CSV should be name'
    }

    if request.method == "GET":
        return render(request,template,prompt)

    csv_file = request.FILES.get('file')
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not CSV file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    next(io_string)

    for column in csv.reader(io_string,delimiter = ',',quotechar = "|"):
        _,created = SysFeature.objects.update_or_create(
            name = column[0]
        )

    features = SysFeature.objects.all()
    return render(request, 'admin_portal/list_feature.html', { 'features': features})


def edit_feature(request, pk):
    feature= get_object_or_404(SysFeature, pk=pk)
    form = SysFeatureForm(request.POST or None, instance=feature)
    if form.is_valid():
        form.save()
        return redirect('list_feature')
    return render(request, 'admin_portal/edit_feature.html', {'form':form})


def delete_feature(request, pk):
    feature= get_object_or_404(SysFeature, pk=pk)
    if request.method=='POST':
        feature.delete()
        return redirect('list_feature')
    return render(request, 'admin_portal/feature_confirm_delete.html', {'object':feature})


def delete_assignfeatures(request, pk):
    assignfeature= get_object_or_404(SysFeatureRole, pk=pk)
    if request.method=='POST':
        assignfeature.delete()
        return redirect('list_assignfeatures')
    return render(request, 'admin_portal/assignfeature_confirm_delete.html', {'object':assignfeature})


def list_assignfeatures(request):
    assignfeatures = SysFeatureRole.objects.all()
    return render(request, 'admin_portal/list_assignfeatures.html', { 'assignfeatures': assignfeatures})


def assign_feature(request):
    sysfeatures = SysFeature.objects.all()
    roles = RoleCode.objects.all()
    permissiontypes = PermissionType.objects.all()
    form = SysFeatureRoleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_assignfeatures')
    return render(request, 'admin_portal/assign_feature.html', { 'sysfeatures': sysfeatures, 'roles': roles, 'permissiontypes' : permissiontypes})


def index(request):
    context = {}
    context['user'] = request.user
    return render(request, 'index.html',context)


def logout(request):
    if request.method == "POST":
        django_logout(request)
    return HttpResponseRedirect(reverse('login'))


def view_property(request):
    return render(request, 'view_property.html')
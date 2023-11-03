from django.shortcuts import render,redirect
from .models import adminModel
from django.contrib import messages
from .helpers import create_jwt_token,require_access_token

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            CHECK_MEMBER = adminModel.objects.get(email=email)
        except adminModel.DoesNotExist:
            messages.error(request, "Member does not exist")
            return render(request, 'login.html')
        else:
            if len(email) != 0 and len(password) != 0 and CHECK_MEMBER:
                if password == CHECK_MEMBER.password:
                    request.session['token'] = create_jwt_token(email)

                    print(request.session.get('token'))
                    messages.success(request, "Now you are logged in")
                    return redirect('dashboard_view')
                else:
                    messages.error(request, "Incorrect Email or Password")
                    return render(request, 'login.html')
    return render(request, 'login.html')

@require_access_token
def logout(request):
    request.session.clear()
    messages.success(request, "You are logged out")
    return redirect('login_view')
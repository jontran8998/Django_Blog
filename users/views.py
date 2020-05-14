from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegiserForm

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserRegiserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created! Your are now able to log in')
      return redirect('login')
  else:
    form = UserRegiserForm()
  return render(request, 'users/register.html', {'form': form})



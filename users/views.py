from django.shortcuts import render
from django.contrib.auth.forms import UsersCreationForm


def register(request):
	form = UsersConfig()
	return render(request, 'users/register.html', {'form': form})

from django.shortcuts import render
posts = [
{
	'author': 'Artur Doe',
	'title': 'Winter Diary',
	'content': 'First note',
	'date_posted': 'September 21, 2018'
},
{
	'author': 'Jane Moe',
	'title': 'Summer Diary',
	'content': 'Second note',
	'date_posted': 'September 21, 2018'
}

]

def home(request):
	context = {
	'posts': posts
	}
	return render(request, 'blog/home.html', context)


def about(request):	
		return render(request, 'blog/about.html')


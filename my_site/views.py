from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Mesage, PortfolioItem


# Home page ::::::::::::::::::::::::::::::::::::::::::::::
def home(request):
	data = {
		'works': PortfolioItem.objects.all(),
	}
	
	return render(request, 'pages/index.html', data)


# About page :::::::::::::::::::::::::::::::::::::::::::::
def about(request):
	return render(request, 'pages/about.html', {})


# Portfolio page :::::::::::::::::::::::::::::::::::::::::
def portfolio(request):
	data = {
		'works': PortfolioItem.objects.all(),
	}
	
	return render(request, 'pages/portfolio.html', data)


# Info page ::::::::::::::::::::::::::::::::::::::::::::::
def info(request):
	return render(request, 'pages/info.html', {})


# Services page ::::::::::::::::::::::::::::::::::::::::::
def services(request):
	return render(request, 'pages/services.html', {})


# Contacts page ::::::::::::::::::::::::::::::::::::::::::
def contacts(request):
	if request.POST:
		data = {
			'name': request.POST['user_name'],
			'email': request.POST['user_email'],
			'site': request.POST['user_site'] or 'none',
			'msg': request.POST['user_msg'], 
		}

		msg = Mesage(	name=data['name'], email=data['email'], 
						website=data['site'], text=data['msg']	)
		msg.save()
		return render(request, 'pages/feedback.html', { 'name': data['name'] })
	else:
		return render(request, 'pages/contacts.html', {})


# Work page ::::::::::::::::::::::::::::::::::::::::::::::
def work(request, pk):
	# work_list = PortfolioItem.objects.all()
	# paginator = Paginator(work_list, 1)
	# page = request.GET.get('item')

	# try:
	# 	work = paginator.page(page)
	# except PageNotAnInteger:
	# 	work = paginator.page(1)
	# except EmptyPage:
	# 	work = paginator.page(paginator.num_pages)

	works = PortfolioItem.objects.all()
	work = get_object_or_404(PortfolioItem, pk=pk)
	data = {
		'works': works,
		'work': work
	}

	return render(request, 'pages/work.html', data)



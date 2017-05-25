from django.template.context_processors import csrf
from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Mesage, PortfolioItem
from .forms import ContactsForm


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
	args = {}
	args.update(csrf(request))
	args['form'] = ContactsForm

	if request.POST:
		form = ContactsForm(request.POST)
		if form.is_valid():
			form.save()
			import pdb; pdb.set_trace()
			return render(request, 'pages/feedback.html', { 'name': form.cleaned_data['name'] })
	else:
		form = ContactsForm()
		return render(request, 'pages/contacts.html', args)



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



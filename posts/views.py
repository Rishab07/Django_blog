from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
 

def posts_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	return render(request,"posts/detail.html",{"instance":instance})



def about(request):
	return render(request,"posts/about.html",{})



def posts_list(request):
	name_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		name_list = name_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query)
			)
		if not name_list:
			return render(request,"posts/search.html",{'error':"No match Found for your search."})

	paginator = Paginator(name_list,4) # Show 6 contacts per page
	page = request.GET.get('page')
	try:
		name = paginator.page(page)
	except PageNotAnInteger:
# If page is not an integer, deliver first page.
		name = paginator.page(1)
	except EmptyPage:
# If page is out of range (e.g. 9999), deliver last page of results.
		name = paginator.page(paginator.num_pages)

	if query:
		return render(request,"posts/search.html",{'name':name})
	else:
		return render(request,"posts/index.html",{"name":name})




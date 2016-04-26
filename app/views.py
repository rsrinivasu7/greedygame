from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app.forms import GenreForm, TrackForm
from app.models import Genre, Track
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
import json
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

# Create your views here.
def genre_list(request):
	genre_list = Genre.objects.all()
	return render_to_response('genre_list.html', {"genre_list":genre_list}, context_instance=RequestContext(request))

def add_genre(request,pk = 0):
	if request.method == 'POST':
		try:
			genre_id = request.POST.get("id",None)
			genre = Genre.objects.get(id = genre_id)
		except ObjectDoesNotExist:
			genre =	 None
		genre_form = GenreForm(data=request.POST ,instance = genre)
		
		if genre_form.is_valid():
			genre_form.save()
			if genre==None:
				messages.success(request, 'Genre Added Successfully.')
			else:
				messages.success(request, 'Genre Updated Successfully.')
			return genre_list(request)
	else:
		try:
			genre = Genre.objects.get(id = pk)
		except ObjectDoesNotExist:
			genre =	 None
			if pk != 0 :
				messages.warning(request, 'Genre Object Not Found.')
				return track_list(request)
		genre_form = GenreForm(instance = genre)
	return render_to_response('add_genre.html', {"genre_form":genre_form,"genre_id":pk}, context_instance=RequestContext(request))

def add_track(request,pk=0):
	if request.method == 'POST':
		try:
			track_id = request.POST.get("id",None)
			track = Track.objects.get(id = track_id)
		except ObjectDoesNotExist:
			track =	 None
			
		track_form = TrackForm(data=request.POST ,instance = track)
		if track_form.is_valid():
			track_form.save()
			if track == None:
				messages.success(request, 'Track Added Successfully.')
			else:
				messages.success(request, 'Track Updated Successfully.')	 
			return track_list(request)
	else:
		try:
			track = Track.objects.get(id = pk)
		except ObjectDoesNotExist:
			track =	 None
			if pk != 0 :
				messages.warning(request, 'Track Object Not Found.')
				return track_list(request)
		track_form = TrackForm(instance = track)
	return render_to_response('add_track.html', {"track_form":track_form,"track_id":pk}, context_instance=RequestContext(request))

def track_list(request):
	track_list = Track.objects.all()
	paginator = Paginator(track_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		tracks = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		tracks = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		tracks = paginator.page(paginator.num_pages)
	return render_to_response('track_list.html', {"track_list":tracks}, context_instance=RequestContext(request))

def track(request,pk = 0):
	try:
		track = Track.objects.get(id = pk)
	except ObjectDoesNotExist:
		messages.warning(request, 'Track Object Not Found.')
		return track_list(request)
	return render_to_response('view_track.html', {"track":track}, context_instance=RequestContext(request))

def genre(request,pk = 0):
	try:
		genre = Genre.objects.get(id = pk)
	except ObjectDoesNotExist:
		messages.warning(request, 'Genre Object Not Found.')
		return track_list(request)
	return render_to_response('view_genre.html', {"genre":genre}, context_instance=RequestContext(request))

def search_track(request):
	track_list = Track.objects.all()
	if request.is_ajax():
		q = request.GET.get('term', '')
		tracks = Track.objects.filter(title__icontains = q )[:10]
		results = []
		for track in tracks:
			track_json = {}
			track_json['id']	= track.id
			track_json['label'] = track.title
			track_json['value'] = track.title
			track_json['type']	= 'tracks'
			results.append(track_json)
			
		genres = Genre.objects.filter(name__icontains = q )[:10]
		for genre in genres:
			track_json = {}
			track_json['id']	= genre.id
			track_json['label'] = genre.name
			track_json['value'] = genre.name
			track_json['type']	= 'genres'
			results.append(track_json)			  
		data = json.dumps(results)
	else:
		data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)
	
def handler404(request):
	response = render_to_response('404.html', {},
								  context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('500.html', {},
								  context_instance=RequestContext(request))
	response.status_code = 500
	return response
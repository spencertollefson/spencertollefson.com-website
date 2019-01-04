from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
import json
from .forms import PostForm
from django.db.models import Q
import os
from django.conf import settings



def bloglist(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/bloglist.html', {'posts': posts})

# def journal_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request, 'blog/journal_list.html', {'posts': posts})

def journal_list(request):
    numbers_list = Post.objects.filter(Q(published_date__lte=timezone.now()) & Q(type='journal')).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/journal_list.html', {
        'posts': posts
    })

def blogdetail(request, slug):
    post = get_object_or_404(Post, slug=slug, type='blog')
    return render(request, 'blog/blogdetail.html', {'post': post})

def journal_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, type='journal')
    return render(request, 'blog/journal_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

# def resume(request):
#     return render(request, 'blog/resume.html')

def resume(request):
    redirect('download_resume', permanent=True)

# def download_resume(request):
#     file = open('Spencer_Tollefson_resume.pdf', 'rb')
#     file.seek(0)
#     pdf = file.read()
#     file.close()
#     return HttpResponse(pdf, 'application/pdf')


def download_resume(request):
    file_path = 'Spencer_Tollefson_Resume.pdf'
    print('the current working dir is:')
    print(os.getcwd())
    if os.path.exists(file_path):
        print('it exists!')
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename="Spencer_Tollefson_Resume.pdf"'
            return response
    print('CANONT FIND FILE')
    raise Http404 
    

def robots(request):
    return render(request, 'robots.txt')

# def tsa_claim(request):
#     return render(request, 'blog/tsa_claims_predictor.html')

#from flask import Flask, abort, render_template, jsonify, request
import joblib

from .api import make_prediction, make_prediction_over_n_days

#app = Flask('TSA-app')

month_dictionary = {
                    'January': '1',
                    'February': '2',
                    'March': '3',
                    'April': '4',
                    'May': '5',
                    'June': '6',
                    'July': '7',
                    'August': '8',
                    'September': '9',
                    'October': '10',
                    'November': '11',
                    'December': '12' 
}

# @app.route('/predict_multiple', methods=['POST'])
def do_prediction_multiple_days(request):
    if not request.is_ajax():
            print('error')
    data = json.loads(request.body)
    data['Month_inc_date'] = month_dictionary[data['Month_inc_date']]

    response = make_prediction_over_n_days(data, 50)
    return JsonResponse(response)


# #@app.route('/', methods=['GET'])
def tsa_claim(request):
    featuredir = './web_app/featurelists'
    airports = sorted(joblib.load(f'{featuredir}/airports.joblib'))
    airlines = sorted(joblib.load(f'{featuredir}/airlines.joblib'))
    airlines.remove('USAir')
    airlines.remove('Northwest Airlines')
    airlines.remove('AirTran Airlines')
    airlines.remove('Continental Airlines')
    claim_types = sorted(joblib.load(f'{featuredir}/claim_types.joblib'))
    claim_sites = sorted(joblib.load(f'{featuredir}/claim_sites.joblib'))
    item_cats = sorted(joblib.load(f'{featuredir}/item_category.joblib'))
    days = list(range(1, 61))
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    return render(request, 'blog/tsa_claim_outcome_prediction.html', {'airports':airports, 'airlines':airlines,
                           'claim_types':claim_types, 'claim_sites':claim_sites,
                           'item_cats':item_cats, 'days':days, 'months':months})


    

# @login_required
# def post_draft_list(request):
#     posts = Post.objects.filter(Q(published_date__isnull=True) | Q(published_date__gt=timezone.now())).order_by('created_date')
#     return render(request, 'blog/post_draft_list.html', {'posts': posts})

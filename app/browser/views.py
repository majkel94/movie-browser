import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import requests

from browser import models

OMBD_SETTINGS = settings.OMDB_API_SETTINGS


@login_required(login_url='login')
def omdb_search(request):
    params = request.GET.copy()
    params['page'] = params.get('page', 1)

    authorized_params = {**params, **{'apikey': OMBD_SETTINGS['OMDB_API_KEY']}}
    response = requests.get(url=OMBD_SETTINGS['OMDB_API_URL'], params=authorized_params)

    context = _get_template_context(response, params)
    return render(request, 'results.html', context)


def _get_template_context(response, params) -> dict:
    page_num = _paginate_results(response, OMBD_SETTINGS['OMDB_API_PAGE_SIZE'])
    query_params = _get_query_params(params)
    return {
        'movies': response.json().get('Search', []),
        'query_params': query_params,
        'current_page': int(params['page']),
        'pages': list(range(1, page_num + 1)),  # count pages from 1
    }


def _paginate_results(response, by):
    return int(response.json().get('totalResults', 0)) // by


def _get_query_params(params):
    protected_fields = {'csrfmiddlewaretoken', 'apikey', 'page'}
    query_params = (f'{p}={v}' for p, v in params.items() if p not in protected_fields)
    return '&'.join(query_params)


@login_required(login_url='login')
def favourites(request):
    if request.method == 'POST':
        details = _lowercase_movie_details(request.POST.get('FavMovie'))
        models.FavMovie.objects.create(user=request.user, **details)
    context = {'movies': models.FavMovie.objects.filter(user=request.user)}
    return render(request, 'favourite.html', context)


def _lowercase_movie_details(movie_data):
    data = json.loads(movie_data.replace("'", '"'))

    return {k.lower(): v for k, v in data.items()}
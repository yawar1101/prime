from django.shortcuts import render
# from django.db.models import Q
from .models import Restaurant

def dish_search(request):
    query = request.GET.get('query')
    print(query)
    results = []
    
    if query:
        results = Restaurant.objects.filter(items__has_key=query).all()

    # print(f'Search query: {query}')
    # print(f'Results: {results}')

    # else:
    #     results = []

    return render(request, 'search_app/search.html', {'results': results, 'query': query})

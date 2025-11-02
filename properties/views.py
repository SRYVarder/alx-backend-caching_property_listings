from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties


@cache_page(60 * 15)
def property_list(request):
    """
    View to list all properties.
    The response is cached for 15 minutes in Redis.
    """
    properties = get_all_properties()
    data = [
        {
            "id": prop.id,
            "title": prop.title,
            "description": prop.description,
            "price": float(prop.price),
            "location": prop.location,
            "created_at": prop.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for prop in properties
    ]
    return JsonResponse({"data": data})

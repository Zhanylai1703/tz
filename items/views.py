from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Item
from items.serializers import ItemSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import permissions

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def add_items(request):
    item = ItemSerializer(data=request.data)
  
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def view_items(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_param.dict())
    else:
        items = Item.objects.all()
  
    # if there is something in items else raise error
    if items:
        data = ItemSerializer(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def update_items(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete_items(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
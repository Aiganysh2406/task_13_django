from django.shortcuts import render

# Create your views here.
from models import Item

Item.objects.create(
    title='hello',
    price=12,
    description='cjfvzndkf'
)


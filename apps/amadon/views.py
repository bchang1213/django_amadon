# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
	return render(request,"index.html")

def buy(request):
	product1 = {
	'product_id': 1001,
	'product_name': 'Dojo T-Shirt',
	'product_price': 19.99,
	}
	product2 = {
	'product_id': 1002,
	'product_name': 'Dojo Sweater',
	'product_price': 29.99,
	}
	product3 = {
	'product_id': 1003,
	'product_name': 'Dojo Cup',
	'product_price': 4.99,
	}
	product4 = {
	'product_id': 1004,
	'product_name': 'Algorithm Book',
	'product_price': 49.99,
	}
	bought_item = {}

	return redirect('/buy/checkout')

def checkout(request):
	return render(request, "checkout.html")
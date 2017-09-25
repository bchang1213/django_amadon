# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products import items
from django.shortcuts import render, redirect

def index(request):
	context = {
		'items': items
	}
	print context
	return render(request,"index.html", context)

def buy(request, product_id):
	for item in items:
		if item['product_id'] == int(product_id):
			amount_charged = item['product_price'] * int(request.POST['quantity'])
			
	# handle exceptions for session keys if they do not yet exist
	try:
		request.session['total_charged']
	except KeyError:
		request.session['total_charged'] = 0

	try:
		request.session['total_items']
	except KeyError:
		request.session['total_items'] = 0        

	request.session['total_charged'] += amount_charged
	request.session['total_items'] += int(request.POST['quantity'])
	request.session['last_transaction'] = amount_charged
	return redirect('/checkout')

def checkout(request):
	return render(request, "checkout.html")
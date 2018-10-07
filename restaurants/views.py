from django.shortcuts import render

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	rests_list=[
		{
			"restaurant_name":"Burger King",
			"food_type":"Fast Food",
		},
		{
			"restaurant_name":"KFC",
			"food_type":"Fast Food",
		},
		{
			"restaurant_name":"Hardees",
			"food_type":"Fast Food",
		},
	]

	

	context = { 
		"my_list":rests_list
	}
	return render(request, 'list.html', context)


def restaurant_detail(request):

	rest_list={
			"restaurant_name":"Burger King",
			"food_type":"Fast Food",
			}

	context = { 
		"my_object":rest_list
	}
	return render(request, 'detail.html', context)

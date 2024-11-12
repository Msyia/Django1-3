from django.shortcuts import render
from subscribeapp.models import Customer
from subscribeapp.forms import NewSubscriber

# Create your views here.
def index(request):
    return render(request, 'subscribeapp/index.html')

def customer(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customer':customer_list}
    return render(request, 'subscribeapp/customer.html', context=customer_dict)

def subscribe(request):
    form = NewSubscriber()
    
    if request.method == "POST":
        form = NewSubscriber(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return customer(request)
    else:
        print("Error: Invalid Form")
        
    return render(request, 'subscribeapp/subscribe.html', {'form':form})
        
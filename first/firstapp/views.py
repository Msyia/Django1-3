from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # Ambil semua data AccessRecord yang diurutkan berdasarkan tanggal
    webpages_list = AccessRecord.objects.order_by('date')
    
    # Buat dictionary untuk konteks yang akan dikirim ke template
    date_dict = {'access_records': webpages_list}
    
    # Gabungkan dengan dictionary lainnya jika ada
    my_dict = {'insert_me': "Hello I'm from first_app"}
    
    # Kirim konteks yang benar ke template
    return render(request, 'first_app/index.html', context={**date_dict, **my_dict})

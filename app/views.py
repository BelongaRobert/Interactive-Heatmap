from django.shortcuts import render
""" from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.views import View
from .models import ipv4
import io,csv """



# Create your views here.

def home(request):
    return render(request, "home.html")

""" class CSVUploadView(View):
    def get(self, request):
        template_name = 'csvupload.html'
        return render(request, template_name)
    def post(self, request):
        paramFile = io.TextIOWrapper(request.FILES['ipv4file'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            ipv4(
                network = row['network'],
                geoname_id = row['geoname_id'],
                registered_country_geoname_id = row['registered_country_geoname_id'],
                represented_country_geoname_id = row['represented_country_geoname_id'],
                is_anonymous_proxy = row['is_anonymous_proxy'],
                is_satellite_provider = row['is_satellite_provider'],
                postal_code = row['postal_code'],
                latitude = row['latitude'],
                longitude = row['longitude'],
                accuracy_radius = row['accuracy_radius'],
           
         )
        for row in list_of_dict
     ]
        try:
            msg = ipv4.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ',e)
            returnmsg = {"status_code": 500}
       
        return JsonResponse(returnmsg) """

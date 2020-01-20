from django.http import HttpResponse, Http404,JsonResponse,HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from vehicle.models import Vehicle,VehicleCategory
from django.template.response import TemplateResponse
from hospital.models import HospitalUser
from vendor.models import VendorUser

def vehicle_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax():      
        try:
            vehicleId = request.POST.get('id', '')
            response = Vehicle.objects.filter(pk=vehicleId).update(status=3)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Vehicle Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/vehicle/vehicleuser/")
    else:
        return HttpResponse('Invalid request passed')

def hospitaluser_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax(): 
        try:
            Hospital_userId = request.POST.get('id', '')
            response = HospitalUser.objects.filter(pk=Hospital_userId).update(status=3)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Hospital User Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/hospital/hospitaluser/")
    else:
        return HttpResponse('Invalid request passed')

def category_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax(): 
        try:
            categoryId = request.POST.get('id', '')
            response = VehicleCategory.objects.filter(pk=categoryId).update(status=2)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Category Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/vehicle/vehiclecategory/")
    else:
        return HttpResponse('Invalid request passed')

def vendoruser_soft_delete(request): 
    result = {}
    if request.method == 'POST' and request.is_ajax(): 
        try:
            vendor_id = request.POST.get('id', '')
            response = VendorUser.objects.filter(pk=vendor_id).update(status=3)
            if (response == True):
                result['status'] = True
                result['msg'] = 'Vendor User Deleted Successfully successfully!'
                return JsonResponse(result)
            else:
                result['status'] = False
                result['msg'] = 'Something went wrong!'
                return JsonResponse(result)
        except Http404:
            return HttpResponseRedirect("/admin/vendor/vendoruser/")
    else:
        return HttpResponse('Invalid request passed')

def vehicle_save(request):
    print(request.POST.get('type'))
    
    return HttpResponse('Invalid request passed')

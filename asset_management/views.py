
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company, Device, CheckOut
from .serializers import CompanySerializer, DeviceSerializer, CheckOutSerializer

@api_view(['GET', 'POST'])
def company_list_create(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def company_retrieve_update_destroy(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        device.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def checkout_list(request):
    if request.method == 'GET':
        checkouts = CheckOut.objects.all()
        serializer = CheckOutSerializer(checkouts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CheckOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def checkout_detail(request, pk):
    try:
        checkout = CheckOut.objects.get(pk=pk)
    except CheckOut.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CheckOutSerializer(checkout)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CheckOutSerializer(checkout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        checkout.delete()
        return Response(status=204)

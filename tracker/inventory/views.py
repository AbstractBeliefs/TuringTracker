from django.shortcuts import render

from inventory.models import *
from django.contrib.auth.models import User

def index(request):
    stockedDevices = Device.objects.exclude(deviceState=Device.Shipped).count()
    readyDevices = Device.objects.filter(deviceState=Device.Shippable).count()

    context = {
        "recordedDevices": Device.objects.count(),
        "volunteers": User.objects.count(),
        "donors": Donor.objects.count(),
        "stocked": stockedDevices,
        "shippable": min(readyDevices, 100),
        "unshippable": min(stockedDevices - readyDevices, 100-min(readyDevices, 100)),
    }

    return render(request, "index.html", context)

def deviceList(request):
    context = {
        'openDevices': Device.objects.exclude(deviceState=Device.Shippable).exclude(deviceState=Device.Shipped),
        'shippableDevices': Device.objects.filter(deviceState=Device.Shippable),
        'shippedDevices': Device.objects.filter(deviceState=Device.Shipped),
    }

    return render(request, "deviceList.html", context)

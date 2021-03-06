from django.db import models
from django.contrib.auth.models import User


################################
# Shipment classes

class Shipment(models.Model):
    date = models.DateField("date shipment was prepared")
    shipmentOpen = models.BooleanField("shipment open to changes", default=True)

    def __unicode__(self):
        return u"Shipment %d opened %s" %(self.id, str(self.date))

class Pallet(models.Model):
    shipment = models.ForeignKey(Shipment, verbose_name="shipment this pallet is part of")
    number = models.IntegerField("pallet number")

    def __unicode__(self):
        return u"Pallet %d of shipment %d" %(self.number, self.shipment.id)

################################
# People classes

class Donor(models.Model):
    name = models.CharField("donor name", max_length=75)
    address = models.TextField("donor address", max_length=300, blank=True)
    email = models.CharField("donor email address", max_length=150, blank=True)
    phone = models.CharField("donor phone number", max_length=20, blank=True)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)    # 1-2-1 relationship to related user
    phone = models.CharField("volunteer phone number", max_length=20, blank=True)
    area = models.CharField("volunteers area of responsibility", max_length=100, blank=True)

    def __unicode__(self):
        return self.user.username


################################
# Device classes

class Device(models.Model):
    # Device types
    Desktop = "DT"
    Laptop = "LT"
    Printer = "LP"
    Monitor = "MT"
    PhoneTab = "PT"
    Other = "OT"
    DEVICE_TYPE_CHOICES = (
        (Desktop, "Desktop"),
        (Laptop, "Laptop"),
        (Printer, "Printer"),
        (Monitor, "Monitor"),
        (PhoneTab, "Phone/Tablet"),
        (Other, "Other device"),
    )

    # Device state
    Received = "RC"
    Holding = "HD"
    Testing = "TS"
    Imaged = "IM"
    Wiped = "WP"
    Shippable = "2S"
    Shipped = "S!"
    DEVICE_STATE_CHOICES = (
        (Received, "Received"),
        (Holding, "Holding/Other - see notes"),
        (Testing, "Needs testing"),
        (Imaged, "Reset to default+freespace wiped"),
        (Wiped, "Device has been wiped clean"),
        (Shippable, "Ready to ship"),
        (Shipped, "Shipped out"),
    )

    pallet = models.ForeignKey(Pallet, verbose_name="pallet this device is shipping on", blank=True, null=True)    # May be null as shipping happens well after initial registration
    donor = models.ForeignKey(Donor, verbose_name="donor this device came from")
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    deviceType = models.CharField("device type", max_length=2, choices=DEVICE_TYPE_CHOICES, default=Desktop)
    deviceState = models.CharField("device state", max_length=2, choices=DEVICE_STATE_CHOICES, default=Received)
    notes = models.TextField("notes", max_length=500, blank=True)
    license = models.TextField("license tag", max_length=500, blank=True)

    def __unicode__(self):
        return u"#%d: %s %s" %(self.id, self.manufacturer, self.model)

class DevLogEntry(models.Model):     # This class logs changes to the device class by user and change
    device = models.ForeignKey(Device)
    user = models.ForeignKey(User)
    entryTime = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=250)

    def __unicode__(self):
        return u"Change to %s by %s: %s" %(self.device.id, self.user.username, self.desc)

class ActionPoint(models.Model):    # This class provides yes/no action points, eg. "Data destruction certificate completed"
    device = models.ForeignKey(Device)
    submitter = models.ForeignKey(User, related_name='submitter')
    completer = models.ForeignKey(User, related_name='completer', blank=True, null=True)
    description = models.CharField(max_length=150)
    complete = models.BooleanField(default=False)

    def __unicode__(self):
        return u"Action point for device %d: %s" %(self.device.id, self.description)

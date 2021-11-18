from django.db import models
from django.utils.translation import ugettext_lazy as _

SERVICE_CATEGORY = (
    (0, _('Unknown')),
    (1, _('hotel')),
    (2, _('camera')),
    (3, _('bambini')),
    (4, _('accessibilità')),
)
ROOM_CATEGORY = (
    (0, _('Unknown')),
    (1, _('hotel')),
    (2, _('bnb')),
    (3, _('appartamento')),
)


class Room(models.Model):
    owner = models.ForeignKey('auth.User', related_name='rooms', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    services = models.ManyToManyField('RoomService', blank=True, verbose_name=_(u"I servizi della Stanza"))
    published = models.BooleanField(verbose_name=_(u"Pubblicato"),default=False)
    category = models.IntegerField(default=0, choices=ROOM_CATEGORY, verbose_name=_(u"Categoria"))

    creation_progress = models.IntegerField(default=0)

    guests = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)

    bathrooms = models.IntegerField(default=0)
    bathrooms_isprivate = models.BooleanField(default=None)
    
    position_full_address = models.TextField(default='Unknown')
    position_country = models.CharField(max_length=255,default='Italy')
    position_city = models.TextField(default='Unknown')
    position_locality_regione = models.TextField(default='Unknown')
    position_locality_provincia = models.TextField(default='Unknown')
    position_locality_comune = models.TextField(default='Unknown')
    position_street = models.TextField(default='Unknown')
    position_street_number = models.TextField(default='Unknown')
    position_zipcode = models.TextField(default='Unknown')
    position_geometry_lat = models.DecimalField(max_digits=40,decimal_places=18,default=0)
    position_geometry_lng = models.DecimalField(max_digits=40,decimal_places=18,default=0)

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    file = models.ImageField(blank=False, null=False, upload_to="rooms/img/%Y/%m/%d")
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    room = models.ForeignKey('Room', related_name='images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.file.name


class RoomService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.IntegerField(default=0, choices=SERVICE_CATEGORY, verbose_name=_(u"Categoria"))
    
    def __str__(self):
        return self.title

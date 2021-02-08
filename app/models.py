from django.db import models
from adaptor.model import CsvModel

# Create your models here.
class ipv4 (models.Model):
    network = DecimalField()
    geoname_id = IgnoredField()
    resgistered_country_geoname_id = IgnoredField()
    represented_country_geoname_id = IgnoredField()
    is_anonymous_proxy = IgnoredField()
    is_satellite_provider = IgnoredField()
    postal_code = IgnoredField()
    latitude = DecimalField()
    longitude = DecimalField()
    accuracy_radius = IgnoredField()

class MycsvModel (CsvModel):
    network = IgnoredField()
    geoname_id = IgnoredField()
    resgistered_country_geoname_id = IgnoredField()
    represented_country_geoname_id = IgnoredField()
    is_anonymous_proxy = IgnoredField()
    is_satellite_provider = IgnoredField()
    postal_code = IgnoredField()
    latitude = DecimalField()
    longitude = DecimalField()
    accuracy_radius = IgnoredField()

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from io import BytesIO
from PIL import Image
import base64, sys
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class Artist(models.Model):
    ArtistID = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def save(self, **kwargs):
        self.slug = self.slug if self.slug else self.name.replace(" ", "-").lower()
        super(Artist, self).save()
    
    def thumbnail(self):
        try:
            art = Art.objects.filter(featured__exact="t").get(ArtistID = self.ArtistID) 
            return art
        except:
            return

    def __str__(self):
        return self.name

class Art(models.Model):
    ArtID = models.AutoField(primary_key = True)
    ArtistID = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="art")
    thumbnail = models.ImageField(upload_to="art", blank=True, default='thumbnail.png')
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "art"
    
    def __str__(self):
        return self.name

    def save(self, **kwargs):
        output_size = (250, 250)
        output_thumb = BytesIO()
        img = Image.open(self.image)
        img_name = self.image.name.split('.')[0]
        if img.height > 300 or img.width > 300:
            img.thumbnail(output_size)
            img.save(output_thumb, format='PNG', quality=90)

        self.thumbnail = InMemoryUploadedFile(output_thumb, 'ImageField', f"{img_name}_thumb.png", 'image/png', sys.getsizeof(output_thumb), None)
        super(Art, self).save()
        '''
        if not self.image:
            self.thumbnail = None
        else:
            thumbnail_size = 250, 250
            data_img = BytesIO()
            self.image.open()
            tiny_img = Image.open(self.image)
            tiny_img.thumbnail(thumbnail_size)
            tiny_img.save(data_img, format="BMP")
            tiny_img.close()
            try:
                self.thumbnail = "data:image/jpg;base64,{}".format(
                    base64.b64encode(data_img.getvalue()).decode("utf-8")
                )
            except UnicodeDecodeError as e:
                self.blurred_image = None

        super(Art, self).save(force_insert, force_update, using, update_fields)
        '''
    

class Contact(models.Model):
    ContactID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, null=True)
    message = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    SubscriberID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=255)
    subscribed = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
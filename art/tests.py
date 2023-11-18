from django.test import TestCase
from django.core.files import File
from django.urls import reverse
from art.models import Art, Artist, Contact, Subscriber

import mock, os, re

# Create your tests here.
class ArtistTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = Artist.objects.create(
            name="Leonardo Da Vinci"
        )

    def test_fields(self):
        self.assertIsInstance(self.artist.name, str)

class ArtTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        artist = Artist.objects.create(
            name="Leonardo Da Vinci"
        )

        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'monalisaTMP.jpg'
    
        cls.art = Art.objects.create(
            name = "Mona Lisa",
            image = file_mock,
            ArtistID = artist
        )
    def test_fields(self):
        self.assertIsInstance(self.art.name, str)
        self.assertEqual(self.art.image.name, "art/monalisaTMP.jpg")

    def tearDown(self):
        os.remove("media/art/monalisaTMP.jpg")

class ContactTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.contact = Contact.objects.create(
            name = "Joe Smith",
            email = "joe@smith.com",
            phone = "111-222-3333",
            message = "I am interested in a piece of art"
        )
    def test_fields(self):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        phone_regex = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
        
        self.assertIsInstance(self.contact.name, str)
        self.assertTrue(re.fullmatch(email_regex, self.contact.email))
        self.assertTrue(re.fullmatch(phone_regex, self.contact.phone))
        self.assertIsInstance(self.contact.message, str)

class ContactViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "Name")

    def test_post(self):
        response = self.client.post(reverse("contact"),
            {
                'name': 'Joe Smith', 
                'email': 'joe@smith.com', 
                'phone': '111-222-3333',
                'message': 'I am interested in some art'
            }
        )
        self.assertContains(response, "Thank you")
        self.assertEqual(response.status_code, 200)
        contact = Contact.objects.get(email='joe@smith.com')
        self.assertEqual(contact.email, 'joe@smith.com')

class SubscriberTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.subscriber = Subscriber.objects.create(
            first_name="Joe",
            last_name="Smith",
            email="joe@smith.com"
        )
    def test_fields(self):
        self.assertIsInstance(self.subscriber.first_name, str)
        self.assertIsInstance(self.subscriber.last_name, str)
        self.assertIsInstance(self.subscriber.email, str)
        self.assertIsInstance(self.subscriber.subscribed, bool)

class SubscriberViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse("subscribe"))
        self.assertContains(response, "First Name")
    
    def test_post(self):
        response = self.client.post(reverse("subscribe"),
            {
                'first_name': 'Joe',
                'last_name': 'Smith',
                'email': 'joe@smith.com'
            }
        )
        self.assertContains(response, "Success")
        self.assertEquals(response.status_code, 200)
        subscriber = Subscriber.objects.get(email='joe@smith.com')
        self.assertEqual(subscriber.email, 'joe@smith.com')
        
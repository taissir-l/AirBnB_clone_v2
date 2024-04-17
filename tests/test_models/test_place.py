#!/usr/bin/python3
""" city model testing"""
import os
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """tests for the Place model
    """
    def __init__(self, *args, **kwargs):
        """test class
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """type of city_id
        """
        new = self.value()

        self.assertEqual(
            type(new.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """type of user_id
        """
        new = self.value()

        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """type of name
        """
        new = self.value()

        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description(self):
        """type of description
        """
        new = self.value()

        self.assertEqual(
            type(new.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms(self):
        """number_rooms
        """
        new = self.value()
        self.assertEqual(
            type(new.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms(self):
        """number_bathrooms
        """
        new = self.value()
        self.assertEqual(
            type(new.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_max_guest(self):
        """type of max_guest
        """
        new = self.value()
        self.assertEqual(
            type(new.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_price_by_night(self):
        """price_by_night
        """
        new = self.value()
        self.assertEqual(
            type(new.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_latitude(self):
        """type of latitude
        """
        new = self.value()
        self.assertEqual(
            type(new.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_longitude(self):
        """type of longitude
        """
        new = self.value()
        self.assertEqual(
            type(new.longitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids(self):
        """amenity_ids
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

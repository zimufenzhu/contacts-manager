import sqlite3
from datetime import datetime
import os


class Contact:
    def __init__(self, id=None, name='', phone='', email='', company='', position='', address='', notes=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.company = company
        self.position = position
        self.address = address
        self.notes = notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'company': self.company,
            'position': self.position,
            'address': self.address,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class CustomField:
    def __init__(self, id=None, contact_id=None, field_name='', field_value='', field_type='text'):
        self.id = id
        self.contact_id = contact_id
        self.field_name = field_name
        self.field_value = field_value
        self.field_type = field_type  # text, number, date

    def to_dict(self):
        return {
            'id': self.id,
            'contact_id': self.contact_id,
            'field_name': self.field_name,
            'field_value': self.field_value,
            'field_type': self.field_type
        }
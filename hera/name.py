"""Code for creating names."""

#
# Distributed according to GNU Affero General Public License v3 Only.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import uuid
import orjson

names = {}

def get(id, gender=None):
    genders = ['male', 'female']
    uid = uuid.UUID(id)
    if gender == None:
        gender = genders[uid.int % len(genders)]
    if not gender in genders:
        gender = 'male'
    return names[gender][uid.int % len(names[gender])]


try:
    with open('data/name.json', 'r') as f:
        names = orjson.loads(f.read())
except ImportError:
    print('names not found')

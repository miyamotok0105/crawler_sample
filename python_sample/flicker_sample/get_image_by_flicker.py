#-*- coding:utf-8 -*-
import urllib
import httplib2
import json 
import os

FLICKER_KEY = "xxxxxxxxxxx"
FLICKER_SELECT = "xxxxxxxxxx"

import flickr_api
flickr_api.set_keys(api_key = FLICKER_KEY, api_secret = FLICKER_SELECT)

user = flickr_api.Person.findByUserName("skizo39")
ps = user.getPhotos()

if not os.path.exists(user.username):
    print("Creating directory " + user.username)
    os.mkdir(user.username)
os.chdir(user.username)

for p in ps:
    print("Saving photo " + p.title)
    p.save(p.title+".jpg")

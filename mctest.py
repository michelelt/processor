#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:09:28 2016

@author: mc
"""
import wm_db
import json
import wm_parser

arr={}
arr["CMD"]= "1"
arr["user_id"]="1"
arr["item_name"]= "giubotto"
arr["item_type"]= "1"
arr["item_material"] = "3"
arr["item_color"] = "2"

d=arr
message = json.dumps(d)

wm_parser.parse(message)
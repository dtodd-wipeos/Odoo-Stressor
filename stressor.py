#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Part of Odoo Stressor
# Copyright 2019 David Todd <dtodd@oceantech.com>
# License: MIT License, refer to `license.md` for more information

"""
    The purpose of this program is to cause significant load on an Odoo system
        to ensure proper configuration and distribution of available resources

    This is designed to use the XMLRPC interface that is exposed by default
    Currently it only performs heavy search operations (All rows, No limit)
        among 3 of our biggest tables (one of them is from a module that we developed)
    A more complete solution would do a variety of tasks, such as creating,
        reading, updating, deleting, and searching records with a variety
        in the queries submitted, as well as different limits for the searches.
        This might come eventually in the future, but is sufficient for now.
    
    For documentation on how Odoo processes XMLRPC requests, please refer to
        https://www.odoo.com/documentation/9.0/api_integration.html

    Usage:
        `export odoo_host='<string, required, the hostname of your odoo instance>'` - Include the `http(s)://` at the beginning
        `export odoo_database=<string, required, the database you are interacting with>`
        `export odoo_user=<integer, optional, your user's database id>` - The default value of 1 for the `admin` user will be used if not provided
        `export odoo_pass='<string, required, your user's password>'`
        `export stress_threads=<integer, optional>` - The default value of 100 will be used if not provided
        `export stress_loops=<integer, optional>` - The default value of 1000 will be used if not provided
        `python stressor.py`
"""

from stress import Stress
from api import API

if __name__ == '__main__':
    api = API()
    stress = Stress(api)
    stress.do_stress()

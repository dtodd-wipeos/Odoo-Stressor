#!/bin/bash
# Part of Odoo Stressor
# Copyright 2019 David Todd <dtodd@oceantech.com>
# License: MIT License, refer to `license.md` for more information

# The purpose of this script is to set up the
# environment for the stressor and to execute it

export odoo_host="" # Hostname of the Odoo instance, including http(s)://
export odoo_database="" # The database the Odoo instance works on
export odoo_user=1 # The database id of the user who will be accessing the API, default is 1 for `admin`
export odoo_pass="" # Don't commit secrets
export stress_threads=100 # Default to 100x background threads doing random stress tests
export stress_loops=1000 # Default to running those 100x threads 1000x times

python3 stressor.py

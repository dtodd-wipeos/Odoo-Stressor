#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Part of Odoo Stressor
# Copyright 2019 David Todd <dtodd@oceantech.com>
# License: MIT License, refer to `license.md` for more information

from exceptions import InputError
from api import API

import threading
import random
import time
import os

class Stress:
    """
        Contains the methods that perform the stress testing against Odoo.

        These optional fields are configured via the environment:
            `stress_threads` - Integer, how many threads to spawn per loop
            `stress_loops` - Integer, how many times should the stress test be ran
    """

    # Models that are known to contain a lot of rows in our Odoo instance
    # `erpwarehouse.sellable` won't exist for most people, so you should remove that,
    # else you'll get a ton of exceptions
    MODELS = ['res.partner', 'erpwarehouse.sellable', 'mail.message']

    # The stressors that are available
    STRESS_METHODS = ['search']

    def __init__(self):
        self.stress_threads = int(os.environ.get('stress_threads', 100))
        self.stress_iterations = int(os.environ.get('stress_loops', 1000))
        self.api = API()

    def _do_search(self, model):
        """
            The only available stress method currently. Performs a search
            on the provided model, which should have a lot of rows
        """
        return self.api.do_search(model)

    def _stress_method(self, id, model, message, stress_method):
        """
            Does the heavy lifting of the stress test. Uses the randomly provided
            `model` and `stress_method` to do the stress test
        """
        print("Starting Thread %d" % (id))
        print(message)

        if stress_method not in self.STRESS_METHODS:
            raise InputError('stress_method',
                'Incorrect stress method. Available stressors are: %s' % (', '.join(self.STRESS_METHODS)))

        if stress_method == 'search':
            # We don't use this variable, it's just to suppress output from doing searches
            # which return a huge list of database IDs
            #pylint: disable=unused-variable
            null = self._do_search(model)
        
        # More stress tests would be defined above, and then added via an if statement here

        print("Thread ID %d Done!" % (id))

    def choose_stress(self, id):
        """
            Chooses a random model to run a random stress test against
        """
        model = random.choice(self.MODELS)
        return self._stress_method(
            id,
            model,
            "Stressing model: %s" % (model),
            random.choice(self.STRESS_METHODS))

    def do_stress_iteration(self):
        """
            Loops up to `max(self.stress_threads)`, which will each randomly choose
            a stress method, and model to run the stress test against in a background thread
        """
        for id in range(self.stress_threads):
            t = threading.Thread(target=self.choose_stress, args=[id])
            t.daemon = True # Background the thread to not block the script while the thread is executing
            t.start()
    
    def do_stress(self):
        """
            Loops up to `max(self.stress_iterations)`, which will invoke spawning
            `max(self.stress_threads)` in the background for stress testing after
            the previous wave has finished
        """
        for iteration in range(self.stress_iterations):
            print("Iteration: %d" % (iteration))
            self.do_stress_iteration()

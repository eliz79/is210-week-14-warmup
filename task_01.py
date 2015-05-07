#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Arbitrary arguments causing problems."""

import pet


class Dog(pet.Pet):
    """Docstring."""

    def __init__(self, has_shots=False, **kwargs):
        """Docstring."""
        self.has_shots = has_shots
        
    


    

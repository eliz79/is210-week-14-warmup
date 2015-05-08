#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Arbitrary arguments causing problems."""

import pet


class Dog(pet.Pet):
    """A subclass (child) from the Pet class."""
    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the subclass.

        Args:
            has_shots(bool, optional): Defaults to False
            kwargs: an arbitrary arg dict.

        Attributes:
            has_shots(bool): defaults to False.

        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)

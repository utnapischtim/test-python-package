# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 utnapischtim.
#
# test-python-package is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""test python package"""

from .ext import TestPythonPackage
from .version import __version__

__all__ = ("__version__", "TestPythonPackage")

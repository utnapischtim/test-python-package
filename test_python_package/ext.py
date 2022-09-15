# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 utnapischtim.
#
# test-python-package is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Test python package."""

from . import config


class TestPythonPackage(object):
    """test-python-package extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["test-python-package"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "TEST_PYTHON_PACKAGE_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"],
            )
        for k in dir(config):
            if k.startswith("TEST_PYTHON_PACKAGE_"):
                app.config.setdefault(k, getattr(config, k))

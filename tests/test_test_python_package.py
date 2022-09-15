# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 utnapischtim.
#
# test-python-package is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from test_python_package import TestPythonPackage


def test_version():
    """Test version import."""
    from test_python_package import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = TestPythonPackage(app)
    assert 'test-python-package' in app.extensions

    app = Flask('testapp')
    ext = TestPythonPackage()
    assert 'test-python-package' not in app.extensions
    ext.init_app(app)
    assert 'test-python-package' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to test-python-package' in str(res.data)

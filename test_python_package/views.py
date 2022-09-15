# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 utnapischtim.
#
# test-python-package is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""test python package"""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint, render_template
from flask_babelex import gettext as _

blueprint = Blueprint(
    "test_python_package",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@blueprint.route("/")
def index():
    """Render a basic view."""
    return render_template(
        "test_python_package/index.html", module_name=_("test-python-package")
    )

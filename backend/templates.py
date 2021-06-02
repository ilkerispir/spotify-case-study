#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp2_extras import jinja2

def render_template(app, template_name, params=None):
    renderer = jinja2.get_jinja2()
    return renderer.render_template(template_name, **params)
# -*- coding: utf-8 -*-
from drf_camel.settings import rest_framework_settings
from drf_camel.util import camelize


class CamelCaseJSONRenderer(rest_framework_settings.RENDERER_CLASS):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(
            camelize(data), *args, **kwargs
        )
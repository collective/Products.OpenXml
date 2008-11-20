#-*- coding: utf-8 -*-
# $Id$
"""OpenXml installation"""

from Products.CMFPlone.utils import getFSVersionTuple as ploneVersion
from Products.OpenXml.setuphandlers import setupOpenXml
from Products.OpenXml.setuphandlers import removeOpenXml

if ploneVersion()[:2] == (2, 5):
    # Support for Plone 2.5

    class FakeInstallContext(object):

        def __init__(self, context):
            self.context = context

        def getSite(self):
            return self.context

    def install(self):
        context = FakeInstallContext(self)
        setupOpenXml(context)
        return "OpenXml installed"


def uninstall(self):
    # Note that there is no GenericSetup support for uninstalling today.

    removeOpenXml(self)
    return "OpenXml removed"

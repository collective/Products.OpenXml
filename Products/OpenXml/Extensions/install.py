#-*- coding: utf-8 -*-
# $Id$
"""OpenXml installation"""

from Products.OpenXml.setuphandlers import removeOpenXml

def uninstall(self):
    # Note that there is no GenericSetup support for uninstalling today.

    removeOpenXml(self)
    return

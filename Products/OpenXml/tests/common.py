#-*- coding: utf-8 -*-
# $Id$
"""OpenXml testing package: testing resources"""

from Products.PloneTestCase import PloneTestCase
from Products.OpenXml.config import PROJECTNAME

PloneTestCase.installProduct(PROJECTNAME)
PloneTestCase.setupPloneSite(products=[PROJECTNAME])


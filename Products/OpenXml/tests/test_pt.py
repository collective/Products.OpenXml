#-*- coding: utf-8 -*-
## Copyright (C) 2007 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file LICENSE. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
# $Id$
"""Testing portal_transforms settings"""
import os
import StringIO
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase import PloneTestCase
from Products.OpenXml.config import TRANSFORM_NAME
import common

class PTTestCase(PloneTestCase.PloneTestCase):

    def afterSetUp(self):

        portal = self.getPortal()
        self.pt = getToolByName(portal, 'portal_transforms')


    def testInstallation(self):
        """Checking installation of our transform"""

        self.failUnless(TRANSFORM_NAME in self.pt.objectIds(spec='Transform'),
                        "%s transform expected" % TRANSFORM_NAME)
        return


    def testATfileSearchableText(self):
        """Do we index the text of an openxml office file"""

        self.loginAsPortalOwner()
        class fakefile(StringIO.StringIO):
            pass
        this_dir = os.path.dirname(os.path.abspath(__file__))
        test_filename = os.path.join(this_dir, 'wordprocessing1.docx')
        fakefile = fakefile(file(test_filename, 'rb').read())
        fakefile.filename = 'wordprocessing1.docx'
        file_id = self.portal.invokeFactory('File', fakefile.filename, file=fakefile)
        file_item = getattr(self.portal, file_id)
        # We sample some words from the file and its metadata
        words = ("The", "subject", "of", "the", "document", "custom_value_1",
                 "Lenfant", "example", "title")
        st = file_item.SearchableText()
        for word in words:
            self.failUnless(word in st, "Extected %s in indexable text" % word)
        return


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(PTTestCase))
    return suite


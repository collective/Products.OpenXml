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
"""
Our transform (most job is done by openxmllib)
"""
import openxmllib
from openxmllib import contenttypes as ct
from Products.PortalTransforms.interfaces import itransform
from config import SITE_CHARSET, TRANSFORM_NAME

class openxml_to_text:
    __implements__ = itransform
    __name__ = TRANSFORM_NAME

    inputs = (
        # Wordprocessing formats
        ct.CT_WORDPROC_DOCX_PUBLIC,
        ct.CT_WORDPROC_DOCM_PUBLIC,
        ct.CT_WORDPROC_DOTX_PUBLIC,
        ct.CT_WORDPROC_DOTM_PUBLIC,

        # Spreadsheet formats
        ct.CT_SPREADSHEET_XLSX_PUBLIC,
        ct.CT_SPREADSHEET_XLSM_PUBLIC,
        ct.CT_SPREADSHEET_XLTX_PUBLIC,
        ct.CT_SPREADSHEET_XLTM_PUBLIC,
        # FIXME: note sure we can honour below types...
#        '*.xlam': ct.CT_SPREADSHEET_XLAM_PUBLIC,
#        '*.xlsb': ct.CT_SPREADSHEET_XLSB_PUBLIC

        # Presentation formats
        ct.CT_PRESENTATION_PPTX_PUBLIC,
        ct.CT_PRESENTATION_PPTM_PUBLIC,
        ct.CT_PRESENTATION_POTX_PUBLIC,
        ct.CT_PRESENTATION_POTM_PUBLIC,
        ct.CT_PRESENTATION_PPSX_PUBLIC,
        ct.CT_PRESENTATION_PPSM_PUBLIC,
        # FIXME: Not sure we can honour below types
#        '*.ppam': ct.CT_PRESENTATION_PPAM_PUBLIC
        )

    output = 'text/plain'

    output_encoding = SITE_CHARSET

    def __init__(self,name=None):
        if name:
            self.__name__=name
        return

    def name(self):
        return self.__name__

    def convert(self, orig, data, **kwargs):

        orig_file = kwargs.get('filename') or 'unknown.xxx'
        mimetype = kwargs.get('mimetype')
        doc = openxmllib.openXmlDocument(orig, mimetype)
        data.setData(doc.indexableText().encode(SITE_CHARSET, 'replace'))
        return data

def register():
    return openxml_to_text()

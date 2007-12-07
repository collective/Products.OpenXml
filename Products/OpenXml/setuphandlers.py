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
"""Setup handlers for OpenXml"""

from Products.CMFCore.utils import getToolByName
import config
from Products.OpenXml import logger

def setupOpenXml(context):
    """Add MS Office 2007 content types to MimetypesRegistry"""

    site = context.getSite()

    # Adding our file types to MTR
    mtr = getToolByName(site, 'mimetypes_registry')
    for mt_dict in config.office_mimetypes:
        main_mt = mt_dict['mimetypes'][0]
        mt_name = mt_dict['name']
        if bool(mtr.lookup(main_mt)):
            # Already installed
            logger.info("%s (%s) Mime type already installed, skipped", main_mt, mt_name)
            continue
        mtr.manage_addMimeType(
            mt_name,
            mt_dict['mimetypes'],
            mt_dict['extensions'],
            mt_dict['icon_path'],
            binary=True,
            globs=mt_dict['globs'])
        logger.info("%s (%s) Mime type installed", main_mt, mt_name)

    # Registering our transform in PT
    transforms_tool = getToolByName(site, 'portal_transforms')
    if config.TRANSFORM_NAME not in transforms_tool.objectIds():
        # Not already installed
        transforms_tool.manage_addTransform(config.TRANSFORM_NAME, 'Products.OpenXml.transform')
    return


def removeOpenXml(context):
    """Removing various resources from plone site"""

    # At the moment, there's no uninstall support in GenericSetup. So
    # this is run by the old style quickinstaller uninstall handler.

    site = context
    # Removing our types from MTR
    mtr = getToolByName(site, 'mimetypes_registry')
    mt_ids = [mt_dict['mimetypes'][0] for mt_dict in config.office_mimetypes]
    mtr.manage_delObjects(mt_ids)

    # Removing our transform from PT
    transforms_tool = getToolByName(site, 'portal_transforms')
    transforms_tool.unregisterTransform(config.TRANSFORM_NAME)
    return



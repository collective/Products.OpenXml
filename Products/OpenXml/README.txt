#######
OpenXml
#######

By `Gilles Lenfant <mailto:gilles.lenfant@gmail.com>`_

About OpenXml
#############

OpenXml provides Plone resources for OpenXml documents :

* A set of icons for Office 2007 documents
* A set of PortalTransforms plugins suitable to OpenXml documents
  indexing

Requirements
############

* Plone 2.5, Plone 3.x, or Plone 4.0 (note that indexing of OpenXml 
  documents in ATFile or FileFields only works from Plone 3.x onwards
  due to AT changes in field indexing).

* openxmllib 1.0.0 (+) for Python:
  http://code.google.com/p/openxmllib/

* Note that openxmllib requires the - excellent - lxml. See the
  instructions provided in openxmllib documentation.

Note that if you install OpenXml with zc.buildout, you should not care about
installing openxmllib or lxml.


Install
#######

With zc.buildout
----------------

From now, OpenXml is an egg, but you already know it if you're reading
this browsing the pypi site. So to get the latest distro suitable to
your Plone, you only need to add ``Products.OpenXml`` to the eggs list
of your ``buildout.cfg``.

Without zc.buildout
-------------------

::

  $ easy_install openxmllib

Install the OpenXml directory from the unzipped egg into your instance Products
folder.

License
#######

This software is subject to the provisions of the GNU General Public
License, Version 2.0 (GPL).  A copy of the GPL should accompany this
distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY,
AGAINST INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE

More details in the ``LICENSE`` file included in this package.

Testing
#######

Please read ``tests/README.txt`` for unit tests.

Credits
#######

* Icons gracefully given by `Alexander Gross
  <http://www.therightstuff.de/2006/12/16/Office+2007+File+Icons+For+Windows+SharePoint+Services+20+And+SharePoint+Portal+Server+2003.aspx>`
* Minor Plone 4 updates by `David Breitkreutz (davidjb) <http://davidjb.com>`_

GitHub repository
##############

Point your Git client at https://github.com/collective/Products.OpenXml.

Download
########

You may find newer versions of Products.OpenXml from
http://plone.org/products/openxml

Support
#######

Before asking for support, please make sure that your problem is not
described in the documentation that ships with OpenXml or any required
component (see Requirements_ above).


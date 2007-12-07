#######
OpenXml
#######

By Ingeniweb_

About OpenXml
#############

OpenXml provides Plone resources for OpenXml documents :

* A set of icons for Office 2007 documents
* A set of PortalTransforms plugins suitable to OpenXml documents
  indexing

Requirements
############

* Plone 2.5 or Plone 3 (note that indexing of OpenXml documents only
  works from Plone 3.0 due to AT changes in field indexing)

* openxmllib for Python:
  Download: http://sourceforge.net/project/showfiles.php?group_id=74634
  Subversion: https://ingeniweb.svn.sourceforge.net/svnroot/ingeniweb/openxmllib/

* Note that openxmllib requires the - excellent - lxml. See the
  instructions provided in openxmllib documentation.

.. _Ingeniweb:: http://www.ingeniweb.com

Install
#######

As any traditional Zope product:

* Inflate the OpenXml-x.y.z.tgz in the Products directory of your Zope
  instance.

* Use the quickinstaller on your Plone site(s)


License
#######

Copyright (c) 2007 Ingeniweb SAS

This software is subject to the provisions of the GNU General Public
License, Version 2.0 (GPL).  A copy of the GPL should accompany this
distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY,
AGAINST INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE

More details in the ``LICENSE`` file included in this package.

Testing
#######

Please read ``tests/README.txt' for unit tests.

Credits
#######

* Engineering by `the Ingeniweb team <http://www.ingeniweb.com>`_


SVN repository
##############

Point your SVN client to
https://svn.plone.org/svn/collective/Products.OpenXml/...

Download
########

You may find newer versions of PloneArticle from
http://plone.org/products/openxml

Support
#######

Before asking for support, please make sure that your problem is not
described in the documentation that ships with OpenXml or any required
component (see Requirements_ above).

* `Mail to Ingeniweb support <mailto:support@ingeniweb.com>`_ in
  english or french.

* Report issues in english only in the tracker (available from the
  project's page in Download_ above).

`Donations are welcome for new features <http://sourceforge.net/project/project_donations.php?group_id=74634>`_

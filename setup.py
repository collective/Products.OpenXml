# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

_home_dir = os.path.join(os.path.dirname(__file__), 'Products', 'OpenXml')

version = file(os.path.join(_home_dir, 'version.txt'), 'r').read().strip()
_long_description = file(os.path.join(_home_dir, 'README.txt')).read()
_long_description += file(os.path.join(_home_dir, 'HISTORY.txt')).read() 

setup(
    name='Products.OpenXml',
    version=version,
    description="OpenXml documents support for Plone",
    long_description=_long_description,
    classifiers=[
    "Framework :: Plone",
    "Framework :: Zope2",
    "Programming Language :: Python",
    ],
    keywords='Zope CMF Plone openxml',
    author='Gilles Lenfant',
    author_email='gilles.lenfant@gmail.com',
    url='http://svn.plone.org/svn/collective/Products.OpenXml',
    license='GPLv2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    download_url='http://plone.org/products/openxml',
    install_requires=[
    'setuptools',
    'openxmllib',
    'plone.app.controlpanel',
    'plone.app.portlets',
    'plone.portlets',
    'plone.memoize',
    'plone.i18n',
    ],
)

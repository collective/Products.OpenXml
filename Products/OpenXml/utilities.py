"""
This module contains FileMetaProvider and IContentMetaUpdater utility implementations for
OpenXML documents. The same utilities are used  for presentations, spreadshets and word
docs; there are few differences between them in terms of metadata.

Now, OpenXML metadata includes no "description". Instead it has "subject" that is used
more or less for the same purpose. So we use subject for description. On the other hand,
in Plone, the subject is often used for keywords, so we assign keywords found in OpenXML
doc to subject. Finally, OpenXML has "category" which we do not have in Plone, so we
append that to the set of keywords.

If you don't like these decisions, go ahead and implement an alternative content meta
updater and register that in overrides.zcml
"""

from openxmllib import openXmlDocument

from zope.interface import implementer
from collective.filemeta.interfaces import IFileMetaProvider, IContentMetaUpdater
from collective.filemeta.base import MetadataAnnotationsUpdater, DefaultImageUpdater

@implementer(IFileMetaProvider)
class MetaProvider(object):


   def get_metadata(self, data, mimetype, filename):
      "implement the utility interface"

      self.doc = doc = openXmlDocument(data=data, mime_type=mimetype)
      core = doc.coreProperties

      dc = {
         "title": core.get("title"),
         "subject": core.get("subject"),
      }

      return {
         "dc": dc,
         "keywords": self.keywords,
         "category": core.get("category"),
         "image": self.image,
         "pagecount": self.pagecount,
         "mimetype": mimetype,
         "filename": filename
      }


   @property
   def keywords(self):
      "keywords, tags, whatever... "
      core = self.doc.coreProperties
      keywords = []
      if core.get("keywords"):
         keywords.extend([kw.strip() for kw in core["keywords"].split(',')])
      return keywords


   @property
   def pagecount(self):
      "return number of pages/sheets/slides the document has"
      extras = self.doc.extendedProperties
      return extras.get("Slides") or extras.get("Sheets") or extras.get("Pages") or None

   @property
   def image(self):
      "return representative (cover) image for document"
      cover = self.doc.documentCover()
      if cover:
         img_suffix, img_fp = cover
         img_data = img_fp.read()
         img_fp.close()
         return (img_suffix, img_data)
      else:
         return None


class ContentUpdater(MetadataAnnotationsUpdater, DefaultImageUpdater):
   "updates dc:title, dc:description, dc:subject, page count and cover image thumbnail"

   def update_content(self, obj, metadata):
      "implement the utility interface"

      # only set title & description & subject if they do not yet exist

      if not obj.Title():
         obj.setTitle(metadata["dc"]["title"] or metadata["filename"])

      if not obj.Description():
         obj.setDescription(metadata["dc"]["subject"] or "")

      subject = metadata["keywords"] or []
      if metadata.get("category"):
         subject.append(metadata["category"])

      if not obj.Subject():
         obj.setSubject(subject)

      self.annotate_metadata(obj, "pagecount", metadata["pagecount"])
      self.update_image(obj, metadata["image"])


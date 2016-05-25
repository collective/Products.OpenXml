"""
The OpenXMLDocumentInfo adapter implements IDocumentInfo, providing
access to MS OpenXML metadata, including the embedded cover image.

The same adapter is registered for presentations, spreadshets and word
docs.

"""

from openxmllib import openXmlDocument

from zope.interface import implementer
from collective.documentfile.interfaces import IDocumentInfo


@implementer(IDocumentInfo)
class OpenXMLDocumentInfo(object):
   "extractor of document info from OpenXML file"

   def __init__(self, context):
      "initialize the adapter"
      self.context = context
      self.mimetype = context.contentType
      self.doc = openXmlDocument(data=context.data, mime_type=self.mimetype)

   @property
   def title(self):
      return self.doc.coreProperties.get("title")

   @property
   def description(self):
      # it seems the Office metadata subject is sort of descriptive, thus...
      return self.doc.coreProperties.get("subject")

   @property
   def keywords(self):
      "keywords, tags... "
      props = self.doc.coreProperties
      keywords = []
      if props.get("category"):
         # plone has no separate category metadata, so add to keywords
         keywords.append(props["category"])
      if props.get("keywords"):
         keywords.extend([kw.strip() for kw in props["keywords"].split(',')])
      return keywords

   @property
   def language(self):
      "OpenXML docs have no standard language property, so we use a convention"
      return self.doc.customProperties.get("language", "")

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

import re

DEFAULT_TOKEN = re.compile(r"\n\n+")

class Document:
    def __init__(self, raw_text):
        self.raw_text = raw_text

    def paragraphs(self, token=DEFAULT_TOKEN):
        pgs = re.split(token, self.raw_text)
        return [pg.strip() for pg in pgs if pg]

    def sentences_by_paragraph(self, token=DEFAULT_TOKEN):
        pgs = self.paragraphs(token)

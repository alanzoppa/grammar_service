import re
import nltk

DEFAULT_TOKEN = re.compile(r"\n\n+")
SENT_DETECTOR = nltk.data.load('tokenizers/punkt/english.pickle')
#nltk.tag.batch_pos_tag([nltk.word_tokenize(s) for s in sent_detector.tokenize(text.MR_LEE)])


class Document:

    @staticmethod
    def word_tokenize_paragraph(paragraph):
        return [nltk.word_tokenize(sentence) for sentence in paragraph]

    def __init__(self, raw_text):
        self.raw_text = raw_text

    def paragraphs(self, token=DEFAULT_TOKEN):
        pgs = re.split(token, self.raw_text)
        return [pg.strip() for pg in pgs if pg]

    def sentences_by_paragraph(self, token=DEFAULT_TOKEN):
        pgs = self.paragraphs(token)
        return [SENT_DETECTOR.tokenize(pg) for pg in pgs if pg]

    def tokenized_sentences_by_paragraph(self):
        return [Document.word_tokenize_paragraph(paragraph) for paragraph in self.sentences_by_paragraph()]
        
    def tagged_document(self):
        return [ nltk.batch_pos_tag( paragraph ) for paragraph in self.tokenized_sentences_by_paragraph() ]

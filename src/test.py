#import os #import flaskr
import unittest
from server import app
import json
from ipdb import set_trace
from document import Document
from text import MR_LEE
import nltk
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        #flaskr.init_db()

    def api_post(self, path, data):
        if data.__class__.__name__ != 'str':
            data = json.dumps(data)
        return self.app.post(path, data=data, content_type='application/json')


class TestAPIPrimitives(FlaskrTestCase):
    def test_response_format(self):
        res = self.app.post(path='/', data=json.dumps({'documents': ['bar']}), content_type='application/json')
        assert res.content_type == 'application/json'

    def test_bad_request(self):
        res = self.app.get(path='/')
        assert res.status_code == 405

    def test_api_post_helper(self):
        res = self.api_post('/', {'documents': ['bar']})
        assert res.status_code == 200
        assert res.content_type == 'application/json'

class TestDocumentBasics(unittest.TestCase):
    def setUp(self):
        self.doc = Document(MR_LEE)

    def test_initialization(self):
        assert self.doc.raw_text == MR_LEE

    def test_paragraphs(self):
        assert len(self.doc.paragraphs()) == 18

    def test_paragraph_stripping(self):
        assert self.doc.paragraphs()[0][0] == "I"

    def test_ensure_no_empty_sentences(self):
        pgs = self.doc.paragraphs()
        last_pg = pgs[len(pgs)-1]
        assert last_pg != ''

    def test_sentences_by_paragraph_are_arrays(self):
        pgs = self.doc.sentences_by_paragraph()
        assert len(pgs) == 18

    def test_sentences_by_paragraph_are_arrays_of_arrays(self):
        pgs = self.doc.sentences_by_paragraph()
        for pg in pgs:
            assert pg.__class__ == [].__class__
            assert len(pg) > 0
    
    def test_paragraphs_are_word_tokenized(self):
        paragraph = self.doc.sentences_by_paragraph()[-1]
        tokenized_paragraph = Document.word_tokenize_paragraph(paragraph)
        assert len(tokenized_paragraph) == 4
        for sentence in tokenized_paragraph:
            assert sentence.__class__ == [].__class__
            assert len(sentence) > 0

    def test_tokenized_sentences_by_paragraph(self):
        tsbp = self.doc.tokenized_sentences_by_paragraph()
        assert len(tsbp) == 18
        iterable_to_len = lambda x: len(x)
        sentences_per_paragraph = map(iterable_to_len, tsbp)
        assert sentences_per_paragraph == [1, 1, 3, 1, 4, 5, 3, 4, 2, 1, 1, 6, 2, 2, 6, 6, 2, 4]
        known_sentence_lengths = [
            [22],
            [11],
            [5, 9, 21],
            [23],
            [10, 10, 8, 18],
            [6, 6, 15, 7, 6],
            [8, 13, 9],
            [6, 18, 20, 19],
            [11, 19],
            [12],
            [23],
            [12, 7, 15, 7, 6, 5],
            [6, 22],
            [37, 22],
            [10, 36, 8, 18, 8, 13],
            [10, 6, 3, 8, 9, 18],
            [26, 66],
            [26, 17, 5, 4]
            ]
        words_per_sentence = [map(iterable_to_len, sentence) for sentence in tsbp]
        assert words_per_sentence == known_sentence_lengths

    def test_paragraphs_are_tagged(self):
        tokenized_document = self.doc.tagged_document()
        word_count = 0
        for paragraph in tokenized_document:
            for sentence in paragraph:
                for word in sentence:
                    word_count += 1
                    assert len(word) == 2

        assert word_count == 765

class TestBasicAPI(FlaskrTestCase):
    def test_posting_valid_document(self):
        res = self.api_post('/', {'documents': [MR_LEE]})
        data = json.loads(res.data)
        new_doc = Document(MR_LEE).tagged_document()
        response_doc = data['documents'][0]
        assert len(response_doc) == 18
        assert json.dumps(new_doc) == json.dumps(response_doc)



if __name__ == '__main__':
    unittest.main()

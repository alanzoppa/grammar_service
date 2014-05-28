#import os #import flaskr
import unittest
from server import app
import json
from pudb import set_trace
from document import Document
from text import MR_LEE
#import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        #flaskr.init_db()

    def api_post(self, path, data):
        if data.__class__.__name__ != 'str':
            data = json.dumps(data)
        return self.app.post(path, data, content_type='application/vnd.api+json')

    #def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])

#class TestNothing(FlaskrTestCase):
    #def test_nothing(self):
        #r = self.app.get('/')
        #assert r.status_code == 200

    #def test_nothing_at_all(self):
        #r = self.app.get('/')
        #assert r.status_code == 200

class TestAPIPrimitives(FlaskrTestCase):
    def test_response_format(self):
        res = self.app.post(path='/', content_type='application/vnd.api+json')
        assert res.content_type == 'application/vnd.api+json'

    def test_bad_format(self):
        res = self.app.post(path='/')
        err = json.loads(res.data)
        assert err['error'] == 'use application/vnd.api+json'
        assert res.content_type == 'application/vnd.api+json'

    def test_bad_request(self):
        res = self.app.get(path='/')
        assert res.status_code == 405

    def test_api_post_helper(self):
        res = self.api_post('/', {})
        assert res.status_code == 200
        assert res.content_type == 'application/vnd.api+json'

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


#class TestParagraphDivision(FlaskrTestCase):
    #def test_paragraph_split(self):
        #pass



if __name__ == '__main__':
    unittest.main()

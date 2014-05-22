#import os #import flaskr
import unittest
from server import app
import json
from pudb import set_trace
#import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        #flaskr.init_db()

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



if __name__ == '__main__':
    unittest.main()

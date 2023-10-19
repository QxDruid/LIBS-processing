import unittest
from config import UnittestConfig
from web_app import db, create_app
from web_app.lines.models import Line

class LinesTestCase(unittest.TestCase):
    def setUp(self):

        self.app = create_app(UnittestConfig)
        with self.app.app_context():
            db.create_all()

        line = Line('Bi III', 202.0958, 202.09581, 140, 3000000, 'E', 20788.18, 70253.71, 
                '6s26p', '2P°', '3/2', '6s6p2(3P)', '4P', '1/2', 4, 2, ' ',
                 'T10236', 'L9843.L21488.L3331'
                )
        line2 = Line('O I', 500.1, 500.1, 1000, 3000000, 'E', 20788.18, 70253.71, 
                '6s26p', '2P°', '3/2', '6s6p2(3P)', '4P', '1/2', 4, 2, ' ',
                 'T10236', 'L9843.L21488.L3331'
                )
        line3 = Line('Bi III', 600, 600, 10, 3000, 'E', 2088.18, 7253.71, 
                '6s26p', '2P°', '3/2', '6s6p2(3P)', '4P', '1/2', 4, 2, ' ',
                 'T10236', 'L9843.L21488.L3331'
                )
        
        with self.app.app_context():
            db.session.add(line)
            db.session.add(line2)
            db.session.add(line3)
            db.session.commit()
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_status_code_200(self):
        rv = self.client.get('/lines/')
        self.assertEqual(rv.status_code, 200)
    
    def test_db_select(self):
        with self.app.app_context():
            self.assertEqual(Line.query.count(), 3)
            self.assertEqual(db.session.get(Line, 1).element, 'Bi')
            self.assertEqual(db.session.get(Line, 1).ion, 'III')
            #res = Line.query.filter(Line.rel_int > 100).all()
            stmt = db.select(Line).filter(Line.rel_int > 100)
            res = db.session.execute(stmt).all()
            print(f'-------------{res[0]}----------------')
            self.assertEqual(len(res), 2)
            self.assertGreater(res[0].Line.rel_int, 100)
            self.assertGreater(res[1].Line.rel_int, 100)

    def test_return_all_lines(self):
        rv = self.client.get('/lines/')
        self.assertEqual(rv.json[0]['wavelength'], 202.0958)
        self.assertEqual(rv.json[1]['element'], 'O')
        self.assertEqual(rv.json[1]['ion'], 'I')
    
    def test_return_element_lines(self):
        rv = self.client.get('/lines/element/Bi')
        for line in rv.json:
            self.assertEqual(line['element'], 'Bi')
    
    def test_return_line_by_id(self):
        rv = self.client.get('/lines/1')
        self.assertEqual(rv.json['wavelength'], 202.0958)
        self.assertEqual(rv.json['ion'], "III")
        self.assertEqual(rv.json['element'], "Bi")
        


if __name__ == '__main__':
    unittest.main()
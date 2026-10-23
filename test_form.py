
import unittest
from html.parser import HTMLParser
from pathlib import Path

class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.fields = {}
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if tag == "input":
            name = attrs.get("name")
            if name:
                self.fields[name] = attrs.get("type")

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True

class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html = Path("index.html").read_text(encoding="utf-8")
        cls.parser = FormParser()
        cls.parser.feed(html)

    def test_form_exists(self):
        self.assertTrue(self.parser.form_found)

    def test_name_field(self):
        self.assertEqual(self.parser.fields.get("name"), "text")

    def test_email_field(self):
        self.assertEqual(self.parser.fields.get("email"), "email")

    def test_contact_field(self):
        self.assertEqual(self.parser.fields.get("contact"), "tel")

    def test_submit_button(self):
        self.assertTrue(self.parser.submit_found)

if __name__ == "__main__":
    unittest.main(verbosity=2)

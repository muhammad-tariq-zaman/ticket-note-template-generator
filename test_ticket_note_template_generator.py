import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import render_note

def ticket(t="T-101", cat="network", summary="Wi-Fi drops every hour", agent="ali"):
    return {"ticket": t, "category": cat, "summary": summary, "agent": agent}

class TestTicketNote(unittest.TestCase):
    def test_known_category_step(self):
        note = render_note(ticket(cat="printer"))
        self.assertIn("print a test page", note)
    def test_unknown_category_generic_step(self):
        note = render_note(ticket(cat="voodoo"))
        self.assertIn("follow up with the requester", note)
    def test_all_fields_appear(self):
        note = render_note(ticket())
        self.assertIn("T-101", note)
        self.assertIn("Wi-Fi drops every hour", note)
        self.assertIn("ali", note)
    def test_missing_category_is_generic(self):
        note = render_note({"ticket": "T-9", "summary": "s", "agent": "a"})
        self.assertIn("follow up with the requester", note)
    def test_category_case_insensitive(self):
        note = render_note(ticket(cat="Printer"))
        self.assertIn("print a test page", note)

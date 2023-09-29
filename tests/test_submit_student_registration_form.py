import pytest
from selene import be, have
from selene.support.shared import browser

def test_submit_student_registration_form():
    browser.open('/automation-practice-form')
import pytest
from selene import be, have
from selene.support.shared import browser

def test_submit_student_registration_form():
    #open url
    browser.open('/automation-practice-form')
    # Fill name
    browser.element('#firstName').should(be.blank).click().type('Charles')
    browser.element('#lastName').should(be.blank).click().type('Leclerc')
    # Fill email
    browser.element('#userEmail').should(be.blank).click().type('CL16@test.com')
    # Fill gender
    browser.element('[for="gender-radio-1"]').click()
    # fill phone number
    browser.element('#userNumber').should(be.blank).click().type('22312862')
    # fill birthdate
    browser.element('#dateOfBirthInput').click()
    browser.element('[class = "react-datepicker__year-select"]').click()
    browser.element('[value = "1997"]').click()
    browser.element('[class = "react-datepicker__month-select"]').click()
    browser.element('[value = "9"]').click()
    browser.element('[class = "react-datepicker__day react-datepicker__day--016"]').click()
    # fill subjects
    browser.element('#subjectsInput').click().type('Arts').press_enter()
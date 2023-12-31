import os

from selene import be, have
from selene import command
from selene.support.shared import browser


def test_submit_student_registration_form():
    # open url
    browser.open('/automation-practice-form')
    # Fill name
    browser.element('#firstName').should(be.blank).click().type('Charles')
    browser.element('#lastName').should(be.blank).click().type('Leclerc')
    # Fill email
    browser.element('#userEmail').should(be.blank).click().type('CL16@test.com')
    # Fill gender
    browser.element('[for="gender-radio-1"]').click()
    # fill phone number
    browser.element('#userNumber').should(be.blank).click().type('7900900909')
    # fill birthdate
    browser.element('#dateOfBirthInput').click()
    browser.element('[class = "react-datepicker__year-select"]').click()
    browser.element('[value = "1997"]').click()
    browser.element('[class = "react-datepicker__month-select"]').click()
    browser.element('[value = "9"]').click()
    browser.element('[class = "react-datepicker__day react-datepicker__day--016"]').click()
    # fill subjects
    browser.element('#subjectsInput').click().type('arts').press_enter().type('his').press_enter()
    # fill hobbies
    browser.with_(timeout=browser.config.timeout * 2).element('[for="hobbies-checkbox-1"]').click()
    # scrolling to the state
    browser.element('#state').perform(command.js.scroll_into_view)
    # add picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/image.png'))
    # add address
    browser.element('#currentAddress').should(be.blank).click().type('Monaco, Avenue de la Costa')
    # add state and city
    browser.element('#react-select-3-input').type('ha').press_enter()
    browser.element('#react-select-4-input').type('pa').press_enter()
    # press submit
    browser.element('#submit').execute_script('element.click()')

    # checking
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
        'Charles Leclerc',
        'CL16@test.com',
        'Male',
        '7900900909',
        '16 October,1997',
        'Arts, History',
        'Sports',
        'image.png',
        'Monaco, Avenue de la Costa',
        'Haryana Panipat'
    ))

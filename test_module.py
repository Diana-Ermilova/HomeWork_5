import pytest
from time import sleep
from selene import browser, have
import os

def test_fill_form():
    browser.open('/automation-practice-form')

#паспортные данные
    browser.element('#firstName').type('Diana')
    browser.element('#lastName').type('Ermilova')
    browser.all('[for^=gender-radio]').element_by(have.text('Other')).click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker').element('[class$="month-select"]').click()
    browser.element('.react-datepicker').element('[class$="month-select"]').all('option').element_by(have.text('September')).click()
    browser.element('.react-datepicker').element('[class$="year-select"]').click()
    browser.element('.react-datepicker').element('[class$="year-select"]').all('option').element_by(have.text('1996')).click()
    browser.element('.react-datepicker').element('[class*="day--018"]').click()
#контактные данные
    browser.element('#userEmail').type('testmail@gmail.com')
    browser.element('#userNumber').type('8800123121')
    #sleep(200)
#интересы
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    #browser.element('[for=hobbies-checkbox-2]').click()
    #browser.element('[for=hobbies-checkbox-3]').click()
#аватар
    browser.element('#uploadPicture').send_keys(os.path.abspath('pigeon.jpg'))

#адрес
    browser.element('#currentAddress').type('London, county of Surrey, Privet Drive 4')
    browser.element('#state').click()
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Panipat')).click()

#отправка
    browser.element('#submit').click()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))

#проверка заполнения формы
    browser.element('.modal-content table').all('td:nth-child(2)').should(
        have.exact_texts(
            'Diana Ermilova',
            'testmail@gmail.com',
            'Other',
            '8800123121',
            '18 September,1996',
            'Physics',
            'Sports',
            'pigeon.jpg',
            'London, county of Surrey, Privet Drive 4',
            'Haryana Panipat',
        )
    )

from selene import browser, be, by, have, command

import os


def test_registration_form(browser_options):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('vlad')
    browser.element('#lastName').should(be.blank).type('biryukov')
    browser.element('#userEmail').should(be.blank).type('123@gmail.com')

    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('[id="dateOfBirthInput"]').perform(command.js.scroll_into_view).click()

    browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2001')).click()
    browser.element('.react-datepicker__day--027').click()

    browser.element('#subjectsInput').type('Maths').press_enter().type('Physics').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../test-pic/test_kartinka.jpg'))

    browser.element('#currentAddress').type('pushkina 1')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element('[class="modal-header"').should(have.text('Thanks for submitting the form'))

    browser.element('[class="table-responsive"]').should(have.text('vlad biryukov'))
    browser.element('[class="table-responsive"]').should(have.text('123@gmail.com'))
    browser.element('[class="table-responsive"]').should(have.text('Male'))
    browser.element('[class="table-responsive"]').should(have.text('1234567890'))
    browser.element('[class="table-responsive"]').should(have.text('27 January,2001'))
    browser.element('[class="table-responsive"]').should(have.text('Maths, Physics'))
    browser.element('[class="table-responsive"]').should(have.text('Sports'))
    browser.element('[class="table-responsive"]').should(have.text('test_kartinka.jpg'))
    browser.element('[class="table-responsive"]').should(have.text('pushkina 1'))
    browser.element('[class="table-responsive"]').should(have.text('NCR Delhi'))
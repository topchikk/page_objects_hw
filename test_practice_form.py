from demoqa_tests import resources
from selene import browser, be, by, have, command


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][if$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][if$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('[id="dateOfBirthInput"]').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def should_registered_user_info_with(self, first_name, last_name, user_mail, user_male, user_phone,
                                         user_date_of_birth, user_subject, user_hobbies, photo_name, user_address,
                                         user_city):
        browser.element('[class="modal-header"').should(have.text('Thanks for submitting the form'))

        browser.element('[class="table-responsive"]').should(have.text(f'{first_name} {last_name}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_mail}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_male}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_phone}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_date_of_birth}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_subject}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_hobbies}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{photo_name}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_address}'))
        browser.element('[class="table-responsive"]').should(have.text(f'{user_city}'))


# def fill_interests(self, hobbies, subjects):


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('vlad')

    browser.element('#lastName').should(be.blank).type('biryukov')
    browser.element('#userEmail').should(be.blank).type('123@gmail.com')

    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    registration_page.fill_date_of_birth('1999', 'May', '11')

    browser.element('#subjectsInput').type('Maths').press_enter().type('Physics').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

    # browser.element('#uploadPicture').send_keys(os.path.abspath('../test-pic/test_kartinka.jpg'))
    browser.element('#uploadPicture').set_value(resources.resource_path('photo.png'))

    browser.element('#currentAddress').type('pushkina 1')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').click()

    # THEN
    registration_page.should_registered_user_info_with('vlad', 'biryukov', '123@gmail.com', 'Male', '1234567890',
                                                       '27 January,2001', 'Maths, Physics', 'Sports', 'photo.png',
                                                       'pushkina 1', 'NCR Delhi')

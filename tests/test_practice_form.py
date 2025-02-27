from resource.users import new_user
from pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.remove_banner()
    registration_page.register(new_user)

    registration_page.should_registered_user_info_with(new_user.first_name, new_user.last_name, new_user.user_email,
                                                       new_user.gender, new_user.user_number, new_user.day,
                                                       new_user.month, new_user.year, new_user.subjects,
                                                       new_user.hobbies, new_user.images, new_user.current_address,
                                                       new_user.state,
                                                       new_user.city)

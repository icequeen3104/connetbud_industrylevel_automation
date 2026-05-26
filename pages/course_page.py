from pages.base_page import BasePage
from locators.course_locators import CourseLocators

class CoursePage(BasePage):

    def select_course_category(self):
        self.click(CourseLocators.LANGUAGE_CATEGORY)

    def select_english_course(self):
        self.click(CourseLocators.ENGLISH_COURSE)

    def apply_gender_filter(self):
        self.click(CourseLocators.GENDER_FILTER)
        self.click(CourseLocators.MALE_TUTOR)

    def verify_selected_tutor_visible(self):
        self.wait_for_element(CourseLocators.TUTOR_NAME)

    def choose_tutor(self):
        self.wait_for_element(CourseLocators.CHOOSE_TUTOR_BUTTON)
        self.click(CourseLocators.CHOOSE_TUTOR_BUTTON)

    def enter_number_of_classes(self, classes):
        self.fill(CourseLocators.CLASSES_INPUT, classes)

    def click_confirm_button(self):
        self.click(CourseLocators.CONFIRM_BUTTON)

    def complete_course_booking(self, classes):

        self.select_course_category()

        self.select_english_course()

        self.apply_gender_filter()

        self.verify_selected_tutor_visible()

        self.choose_tutor()

        self.enter_number_of_classes(classes)

        self.click_confirm_button()
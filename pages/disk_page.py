import time
import settings as s
from utils.base_ops import BaseOps


class DiskPage(BaseOps):
    def __init__(self, driver):
        super().__init__(driver)

    def create_folder(self):
        self.click_on(s.CREATE_BTN)
        self.wait_for_element(s.BIG_CREATE_BTN)
        self.click_on(s.BIG_CREATE_BTN)
        self.wait_for_text(s.CREATE_MODAL, s.CREATE_MODAL_TEXT)
        time.sleep(0.5) # С этой особенностью Яндекса я боролся часа 4, победил только так
        self.input_text(s.FOLDER_NAME_FIELD, s.FOLDER_NAME)
        self.click_on(s.CONFIRM_BTN)

    def open_folder(self):
        self.wait_for_element(s.FOLDER_ICON)
        self.double_click(s.FOLDER_ICON)

    def add_file(self, path_to_file):
        self.input_text(s.DOWNLOAD_FIELD, path_to_file)
        self.wait_for_text(s.UPLOAD_SUCCESS, s.UPLOAD_SUCCESS_TEXT)

    def get_filename(self):
        self.click_on(s.FILE_ICON)
        self.wait_for_element(s.CHANGE_NAME)
        self.click_on(s.CHANGE_NAME)
        return self.get_value(s.VALUE, s.MODAL_FILENAME)

import settings as s
from pages.disk_page import DiskPage


def test_folder(login, word_example):
    user = DiskPage(login.driver)
    user.create_folder()
    user.open_folder()
    user.add_file(word_example)
    assert user.get_filename() == s.FILE_NAME

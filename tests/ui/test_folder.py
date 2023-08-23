import settings as s
from pages.disk_page import DiskPage


def test_folder(login):
    user = DiskPage(login.driver)
    user.create_folder()
    user.open_folder()
    user.add_file()
    assert user.get_filename() == s.FILE_NAME

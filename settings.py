# URL's

API_URL = "https://cloud-api.yandex.net/v1/disk/resources"
UI_URL = "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fdisk.yandex.ru"
DISK_URL = "https://disk.yandex.ru/client/disk"

# User data
TEST_LOGIN = "stestgora"
TEST_PSWD = "SR1986etyyt3"
FOLDER_NAME = 'TEST_UI'
FILE_NAME = "Файл для копирования.docx"
N_F_NAME = "Новая папкаTEST_UI"
NEW_FOLDER_TEXT = "Новая папка"
CREATE_MODAL_TEXT = "Укажите название папки"
UPLOAD_SUCCESS_TEXT = "Все файлы загружены"
CHANGE_NAME_TEXT = "Переименовать"
PATH_TO_FILE = "G:/Cano/it-23/simbir-a/Файл для копирования.docx"
# ATRIBUTE
TEXT = 'text'
VALUE = 'value'

# HEADERS
AUTH_HEADER = {'Authorization': 'OAuth y0_AgAAAABwNmyjAApdYwAAAADqvF4vK-gato3NQGWeYkDv29agR78nCEw'}
# Prefix
CREATE_P = '?path=%2FTest_API'
DELETE_P = '?path=%2FTest_API&permanently=true'

# METHOD's
PUT = "PUT"
DELETE = "DELETE"
GET = "GET"

# Status_code
CODE_200 = 200
CODE_201 = 201
CODE_204 = 204
CODE_400 = 400
CODE_404 = 404

# Locators
# Login page Locators

LOGIN_BTN = "//button[@id='passp:sign-in']"

LOGIN_FIELD = "//input[@id='passp-field-login']"
PSWD_NAME_FIELD = "//span[@class='CurrentAccount-displayName']"
PSWD_FIELD = "//input[@id='passp-field-passwd']"

# Disk page Locators
ACC_ICON = "//div/a[1]//img[@class='user-pic__image']"
USERNAME = "//div[@id='app']//div[@class='legouser__menu-header']//span[@class='user-account__name']"
CREATE_PLACEHOLDER = "//input[@text='Новая папка']"
CREATE_MODAL = "//h2[@class='dialog__title']"
UPLOAD_SUCCESS = "//h3[@class='uploader-progress__progress-primary']"

LOGOUT_BTN = "//div[@id='app']//ul[@role='group']/li[6]/a[@role='link']/span[@class='menu__text']"
BIG_CREATE_BTN = "//button[@aria-label='Папку']"
CREATE_BTN = "//div[@id='app']//button[@class='Button2 Button2_view_raised Button2_size_m Button2_width_max']"
CONFIRM_BTN = "//div[@class='confirmation-dialog__footer']/button[@type='button']"

FOLDER_NAME_FIELD = "//form[@class='rename-dialog__rename-form']//input"
FOLDER_NAME_FIELD_Cl = "//form[@class='rename-dialog__rename-form']"
FOLDER_NAME_FIELD2 = '.rename-dialog__rename-form  .Textinput-Control'
FOLDER_ICON = "//div[@aria-label='TEST_UI']"
DOWNLOAD_FIELD = "//input[@type='file']"

# Folder page Locators
FILE_ICON = "//div[@aria-label='Файл для копирования.docx']"
CHANGE_NAME = "//div[@class='groupable-buttons__visible-buttons']/span[2]/div/button[@type='button']"
MODAL_FILENAME = "//div[@role='dialog']//form[@class='rename-dialog__rename-form']//input"

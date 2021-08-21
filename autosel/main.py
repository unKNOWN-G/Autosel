from time import sleep
from gtts import gTTS

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# Text to Audio Converter using gTTs
def txt_to_audio_converter(msg: str, file_name: str, audio_saving_dir: str = './') -> None:
    """
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
       |                                                                               |
       |  Description:                                                                 |
       |  ¯¯¯¯¯¯¯¯¯¯¯                                                                  |
       |  Converts the text into audio and saves in audio_saving_dir/<filename>.mp3.   |
       |  This is can be used to send the typed text as audio to the recipient.        |
       |                                                                               |
       |  Parameters:                                                                  |
       |  ¯¯¯¯¯¯¯¯¯¯                                                                   |
       |  :param msg: str, Message that is to be converted into audio format.          |
       |  :param file_name: str, Name of file.                                         |
       |  :param audio_saving_dir: str, Audio Saving Directory.                        |
       |                                                                               |
       |  Return:                                                                      |
       |  ¯¯¯¯¯¯¯                                                                      |
       |  :return: None                                                                |
       |                                                                               |
       ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
    """
    language = 'en'
    output = gTTS(text=msg, lang=language, slow=False)
    output.save(audio_saving_dir + "/" + file_name + ".mp3")


class Whatsapp:
    def __init__(self, driver_address: str, usage_data_directory: str):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                              |
           |  To initialize the the chrome driver and to login got whatsapp.                                           |
           |  The usage_data_directory is used to store the QR code information to avoid multiple scanning.            |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯¯                                                                                               |
           |  :param driver_address: str, Address of Chrome Driver.                                                    |
           |  :param usage_data_directory: str, Stores data to help logging multiple times seamless by passing QR code.|
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        self.__driver_address = driver_address
        self.__usage_data_directory = usage_data_directory
        self.__driver = self.__whatsapp_initializer()

    def send_document(self, name: list, files_address: list, select: bool = True) -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                              |
           |  This method is used to Automatically send files as documents to the recipient.                           |
           |  Multiple Documents can also be sent to the recipient by adding the files address in `file_address` list. |
           |  This same set of documents can be even sent to multiple people by adding names into the `name` list.     |
           |  Accepts all formats.                                                                                     |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯                                                                                                |
           |  :param files_address: list, Contains strings of address of files to be sent stored in list.              |
           |  :param name: list, List of all contacts to which it should be send in string format.                     |
           |  :param select: bool, Confirm if a particular command should be there on not.                             |
           |                                                                                                           |
           |  Return:                                                                                                  |
           |  ¯¯¯¯¯¯¯                                                                                                  |
           |  :return: None                                                                                            |
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        if select:
            for j in range(len(name)):
                # Selects the chat from the given list of names
                self.__chat_selector(name[j])
                for i in files_address:
                    self.__sender(xpath='//input[@accept="*"]', file_name=i)

    def send_image(self, name: list, files_address: list, select: bool = True) -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                              |
           |  This method is used to Automatically send image or video to the recipient.                               |
           |  Multiple Images, Videos can be sent by adding the file address with extension in the `file_address` list |
           |  The same set of images, videos can be even sent to multiple people by adding names into the `name` list  |
           |  Accepts all formats of image and videos.                                                                 |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯¯                                                                                               |
           |  :param name: list, List of all contacts to which it should be send in string format.                     |
           |  :param files_address: list, Contains strings of address of files to be sent stored in list.              |
           |  :param select: bool, Confirm if a particular command should be there on not.                             |
           |                                                                                                           |
           |  Return:                                                                                                  |
           |  ¯¯¯¯¯¯¯                                                                                                  |
           |  :return: None                                                                                            |
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        if select:
            for j in range(len(name)):
                # Selects the chat from the given list of names
                self.__chat_selector(name[j])
                for i in files_address:
                    self.__sender(xpath='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]', file_name=i)

    def send_text(self, name: list, msg: list, select: bool = True) -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                              |
           |   This method is used to Automatically send messages to the recipient.                                    |
           |   Multiple messages can be sent by adding messages into the `msg` list.                                   |
           |   The same set of images, videos can be even sent to multiple people by adding names into the `name` list |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯¯                                                                                               |
           |  :param name: list, List of all contacts to which it should be send in string format.                     |
           |  :param msg: str, Message to be sent.                                                                     |
           |  :param select: bool, Confirm if a particular command should be there on not.                             |
           |                                                                                                           |
           |  Return:                                                                                                  |
           |  ¯¯¯¯¯¯¯                                                                                                  |
           |  :return: None                                                                                            |
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        for j in range(len(name)):
            self.__chat_selector(name[j])
            for i in range(len(msg)):
                self.__message_writer(msg[i], select=select)

    def send_audio(self, name: list, msg: str, file_name: str, file_dir: str, select: bool = True) -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                             |
           |  Description:                                                                               |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                |
           |  This method converts the given message into a audio recording and send to the recipient.   |
           |  The audio file can be sent to multiple recipients by adding recipients into `name` list.   |
           |                                                                                             |
           |  Parameters:                                                                                |
           |  ¯¯¯¯¯¯¯¯¯¯                                                                                 |
           |  :param name: list, List of all contacts to which it should be send in string format.       |
           |  :param msg: str, Stores the message in string format.                                      |
           |  :param file_name: list, Name of the Audio File.                                            |
           |  :param file_dir: str, name of file directory.                                              |
           |  :param select: bool, Confirm if a particular command should be there on not.               |
           |                                                                                             |
           |  Return:                                                                                    |
           |  ¯¯¯¯¯¯¯                                                                                    |
           |  :return: None.                                                                             |
           |                                                                                             |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        if select:
            txt_to_audio_converter(msg=msg, file_name=file_name, audio_saving_dir=file_dir)
            for j in name:
                self.__chat_selector(person_name=j)
                self.__sender(xpath='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]',
                              file_name=file_dir + "/" + file_name + ".mp3")

            sleep(0.5)

    def create_group(self, group_list: list, group_name: str, text_dir: str = './group_names.txt') -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                              |
           |  This method is used to create a whatsapp group.                                                          |
           |  Using the contact names given in `group_list` and group name in `group_name` the whatsapp group is made. |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯                                                                                                |
           |   :param group_list: list, Stores the list of names(str) to be added in group in a list.                  |
           |   :param group_name: str, Name of the group.                                                              |
           |   :param text_dir: str, This is an alternate way of giving the list of group members and the group name   |
           |                          by storing in a .txt file.                                                       |
           |                                                                                                           |
           |  Return:                                                                                                  |
           |  ¯¯¯¯¯¯¯                                                                                                  |
           |  :return: None.                                                                                           |
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        if len(group_list) > 0:
            people_name = group_list
        else:
            try:
                people_name = open(text_dir, "r").read().split("\n")
            except FileNotFoundError:
                people_name = []
                pass
        WebDriverWait(self.__driver, 30).until(ec.presence_of_element_located((By.XPATH, '//span[@data-icon="menu"]'
                                                                                         ''))).click()

        WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//div[contains( text(), "New group")]'))).click()

        for i in range(0, len(people_name)):
            contact_searcher = WebDriverWait(self.__driver, 30).until(
                ec.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
            contact_searcher.click()
            contact_searcher.send_keys(people_name[i])

            contact_clicker = WebDriverWait(self.__driver, 30).until(
                ec.presence_of_element_located((By.XPATH, '//span[@title="{}"]'.format(people_name[i]))))
            contact_clicker.click()

        WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//span[@data-icon="arrow-forward"]'))).click()

        grp_name = WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"]')))
        grp_name.click()
        grp_name.send_keys(group_name)

        WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//span[@data-icon="checkmark-medium"]'))).click()
        x = 1

        while x == 1:
            try:
                WebDriverWait(self.__driver, 30).until(
                    ec.presence_of_element_located((By.XPATH, '//div[text()="Invite to group"]'))).click()
                sleep(1)
                self.__send_clicker()
                sleep(0.5)
            except:
                x = 0
                pass

        sleep(7)

    def spam_bot(self, name: list, msg: str, count: int) -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                          |
           |  Description:                                                                            |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                             |
           |  This method is used to send repeated texts (Spam) to the same person.                   |
           |  Messages can be sent to multiple recipients also by the contact names in `name` list.   |
           |                                                                                          |
           |  Parameters:                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯                                                                              |
           |  :param name: list, Names of the person to whom these messages are to be sent.           |
           |  :param msg: str, Message.                                                               |
           |  :param count: int, Number of Messages.                                                  |
           |                                                                                          |
           |  Return:                                                                                 |
           |  ¯¯¯¯¯¯¯                                                                                 |
           |  :return: None                                                                           |
           |                                                                                          |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        for i in name:
            self.__chat_selector(i)
            for j in range(count):
                self.__message_writer(msg, select=True)
            sleep(1)

    def close_whatsapp(self) -> None:
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                            |
           |  Description:                                              |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                               |
           |  This method is used to close the running chrome driver.   |
           |                                                            |
           |  Parameters:                                               |
           |  ¯¯¯¯¯¯¯¯¯                                                 |
           |                                                            |
           |  Return:                                                   |
           |  ¯¯¯¯¯¯¯                                                   |
           |  :return: None.                                            |
           |                                                            |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        sleep(2)
        self.__driver.close()

    def __whatsapp_initializer(self):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                         |
           |  Description:                                                                                           |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                            |
           |  To initialize the chromedriver, and to store the whatsapp login info to avoid multiple QR code scans   |
           |  Adding Arguments to chrome browser so that it wont Crash                                               |
           |                                                                                                         |
           |  Parameters:                                                                                            |
           |  ¯¯¯¯¯¯¯¯¯                                                                                              |
           |                                                                                                         |
           |  Return:                                                                                                |
           |  ¯¯¯¯¯¯¯                                                                                                |
           |  :return: diver, Returns the initialized driver variable                                                |
           |                                                                                                         |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        options = Options()
        options.add_argument('--user-data-dir={}/User_Data'.format(self.__usage_data_directory))
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome("{0}".format(self.__driver_address), options=options)

        # Open Website
        driver.get('https://web.whatsapp.com/')
        try:
            element_present = ec.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div['
                                                                        '3]/div/span'))
            WebDriverWait(driver, 1000).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            pass
        driver.maximize_window()
        return driver

    def __sender(self, xpath: str, file_name: str):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                                              |
           |  A Helper Function which clicks on the attach button and selects the respective icon                      |
           |  (Image, audio, document)                                                                                 |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯                                                                                                |
           |  :param xpath: xpath of the icon(after click the attach)                                                  |
           |  :param file_name: File address                                                                           |
           |                                                                                                           |
           |  Return:                                                                                                  |
           |  ¯¯¯¯¯¯¯                                                                                                  |
           |  :return: None                                                                                            |
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        # To click the Paper clip
        element = WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//div[@title="Attach"]')))
        element.click()

        # To click on Icon
        icon = WebDriverWait(self.__driver, 30).until(ec.presence_of_element_located((By.XPATH, '{}'.format(xpath))))
        icon.send_keys(file_name)

        sleep(0.5)

        # To send the document
        self.__send_clicker()

    def __chat_selector(self, person_name: str):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                            |
           |  Description:                                                                              |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                               |
           |  This method is used to open new chat and select a particular contact from Whatsapp chat   |
           |                                                                                            |
           |  Parameters:                                                                               |
           |  ¯¯¯¯¯¯¯¯¯                                                                                 |
           |  :param person_name: str, Name of Receiver                                                 |
           |                                                                                            |
           |  Return:                                                                                   |
           |  ¯¯¯¯¯¯¯                                                                                   |
           |  :return: None                                                                             |
           |                                                                                            |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        # Opening New chat Option
        user = WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/'
                                                      'div[2]/div/span/div[2]/'
                                                      'div/span')))

        user.click()

        # Code to Find Element in the Search box
        search_box = WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="app"]/div'
                                                      '/div/div[2]/div[1]'
                                                      '/span/div/span/div'
                                                      '/div[1]/div/label'
                                                      '/div/div[2]')))

        search_box.click()
        search_box.send_keys(person_name)

        sleep(1)

        # Code to Click the Open first Chat box in Search Results
        opening_chat = WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//span[@title="{}"]'.format(person_name))))
        opening_chat.click()
        sleep(0.5)

    def __message_writer(self, msg: str, select: bool):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                |
           |  Description:                                                                  |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                                   |
           |  This method types the message in the text box                                 |
           |                                                                                |
           |  Parameters:                                                                   |
           |  ¯¯¯¯¯¯¯¯¯                                                                     |
           |  :param msg: str, The message to be sent to the receiver is stored under msg   |
           |  :param select: bool, Confirms if this message should be sent or not           |
           |                                                                                |
           |  Return:                                                                       |
           |  ¯¯¯¯¯¯¯                                                                       |
           |  :return:None                                                                  |
           |                                                                                |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        if select:
            # Code To send text message
            message_box = WebDriverWait(self.__driver, 30).until((ec.presence_of_element_located((By.XPATH, '//*[@id="m'
                                                                                                            'ain"]/foot'
                                                                                                            'er/div[1]/'
                                                                                                            'div[2]/div'
                                                                                                            '/div[1]/di'
                                                                                                            'v/div[2]'
                                                                                                            ''))))

            message_box.send_keys(msg)

            # Code to CLick Send Button
            message_sender = WebDriverWait(self.__driver, 30).until((ec.presence_of_element_located((By.XPATH, '//'
                                                                                                               'button'
                                                                                                               '[@class'
                                                                                                               '="_4sW'
                                                                                                               'nG"]')))
                                                                    )
            message_sender.click()

    def __send_clicker(self):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                    |
           |  Description                                                       |
           |  ¯¯¯¯¯¯¯¯¯¯¯                                                       |
           |  This method is used to click on send button while sending files   |
           |                                                                    |
           |  Parameters                                                        |
           |  ¯¯¯¯¯¯¯¯¯                                                         |
           |                                                                    |
           |  Return:                                                           |
           |  ¯¯¯¯¯¯¯                                                           |
           |  :return: None                                                     |
           |                                                                    |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """

        send_icon = WebDriverWait(self.__driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
        send_icon.click()

        sleep(0.5)


def bolder(driver: webdriver):
    """
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
       |                                                                                          |
       |  Description:                                                                            |
       |  ¯¯¯¯¯¯¯¯¯¯¯                                                                             |
       |  This method is used to activate and deactivate bolding functionality in the mail body   |
       |                                                                                          |
       |  Parameters:                                                                             |
       |  ¯¯¯¯¯¯¯¯¯¯                                                                              |
       |  :param driver: driver                                                                   |
       |                                                                                          |
       |  Return:                                                                                 |
       |  ¯¯¯¯¯¯¯                                                                                 |
       |  :return: None                                                                           |
       |                                                                                          |
       ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
    """
    try:
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.aaA.eN'))).click()
    except:
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.oc .J-Z-I'))).click()
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.aaA.eN'))).click()


def login(driver: webdriver, sender_email: str, sender_password: str) -> None:
    """
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
       |                                                      |
       |  Description                                         |
       |  ¯¯¯¯¯¯¯¯¯¯¯                                         |
       |  This function is used to login into Gmail account   |
       |                                                      |
       |  Parameters                                          |
       |  ¯¯¯¯¯¯¯¯¯¯                                          |
       |  :param driver: driver                               |
       |  :param sender_email: str, Email of Sender           |
       |  :param sender_password: str, Password of Sender     |
       |                                                      |
       |  Return:                                             |
       |  ¯¯¯¯¯¯¯                                             |
       |  :return: None                                       |
       |                                                      |
       ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
    """
    # Open Gmail Page
    driver.get("http://www.gmail.com")
    sleep(2)

    # Logging in
    ele = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
    ele.send_keys(sender_email)
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, '//span[contains( text(), "Next")]'))).click()
    sleep(3)
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//input[@name="password"]'
                                                                              ''))).send_keys(sender_password)
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, '//span[contains( text(), "Next")]'))).click()
    sleep(7)


def send_single_mail(driver: webdriver, email: str, email_subject: str, email_body: list) -> None:
    """
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
       |                                                          |
       |  Description                                             |
       |  ¯¯¯¯¯¯¯¯¯¯¯                                             |
       |  This method is used to send a mail to a single person   |
       |                                                          |
       |  Parameters                                              |
       |  ¯¯¯¯¯¯¯¯¯¯                                              |
       |  :param driver: driver                                   |
       |  :param email: Persons Email                             |
       |  :param email_subject: Subject of mail                   |
       |  :param email_body: Body of Mail                         |
       |                                                          |
       |                                                          |
       |  Return:                                                 |
       |  ¯¯¯¯¯¯¯                                                 |
       |  :return: None                                           |
       |                                                          |
       ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
    """
    # Compose button
    try:
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.z0>.L3'))).click()
    except IndexError:
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.z0>.L3::before'))).click()
    sleep(1)

    # Input Recipient
    ele = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".oj div textarea")))
    ele.send_keys(email)
    sleep(0.5)

    # Input Subject
    ele = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".aoD.az6 input")))
    ele.send_keys(email_subject)
    sleep(0.5)

    # Input Text
    if len(email_body) > 1:
        for i in range(len(email_body)):
            ele = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".Ar.Au div")))
            ele.send_keys(email_body[i])
            bolder(driver)
    else:
        ele = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".Ar.Au div")))
        ele.send_keys(email_body[0])
    sleep(0.5)

    # Send Button
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.T-I-atl."
                                                                                     "L3"))).click()
    sleep(0.5)

    print("Email Sent to " + email)


class Email:
    def __init__(self, sender_email: str, sender_password: str, mail_subject: str, mail_body: list):
        """
           _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           |                                                                                                           |
           |  Description:                                                                                             |
           |  ¯¯¯¯¯¯¯¯¯¯¯¯                                                                                             |
           |  This Class Automates the process of sending E-mails to multiple recipients                               |
           |  Using the sender_mail and sender_password credentials as input along with mail_subject and mail_body     |
           |  as input, Mails can be sent to multiple recipients individually.                                         |
           |                                                                                                           |
           |  There's an additional functionality of Boding the content in the body.                                   |
           |  This can be used by alternatively giving the text in the `mail_body` list with normal and bold texts     |
           |  [ "Normal text1", "Bold Text 1", "Normal text 2", "Bold Text 2" ......]                                  |
           |                                                                                                           |
           |  Note: 1) To input Multiple lines of string use triple quotes                                             |
           |        2) This Class might not work with regular gmail accounts. It is advised to use organisation        |
           |       specific sender_email that (or) gmails that arent created on this device                            |
           |                                                                                                           |
           |                                                                                                           |
           |  Parameters:                                                                                              |
           |  ¯¯¯¯¯¯¯¯¯¯                                                                                               |
           |  :param sender_email: str, Mail ID of the sender                                                          |
           |  :param sender_password: str, Password of the sender.                                                     |
           |  :param mail_subject: str, Subject of the Email                                                           |
           |  :param mail_body: list, List of Stings given alternatively with Normal and bolding texts.                |
           |                                                                                                           |
           ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯
        """
        self.__sender_email = sender_email
        self.__sender_password = sender_password
        self.__subject = mail_subject
        self.__body = mail_body

    def send_mails(self, driver_path: str, emails: list) -> None:
        """
            ____________________________________________________________________________________________________________
            |                                                                                                          |
            |  Description:                                                                                            |
            |  ¯¯¯¯¯¯¯¯¯¯¯¯                                                                                            |
            |  This method is used to Automatically send emails to the recipients.                                     |
            |  Mails can be sent to multiple recipients also individually by adding their names in the `emails` list.  |
            |                                                                                                          |
            |  Parameters:                                                                                             |
            |  ¯¯¯¯¯¯¯¯¯¯                                                                                              |
            |  :param driver_path: str, Chrome Driver Address.                                                         |
            |  :param emails: list, List of Emails to which emails are to be sent.                                     |
            |                                                                                                          |
            |  Return:                                                                                                 |
            |  ¯¯¯¯¯¯¯                                                                                                 |
            |  :return: None.                                                                                          |
            |                                                                                                          |
            ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        """
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        login(driver, self.__sender_email, self.__sender_password)
        for i in range(len(emails)):
            send_single_mail(driver, emails[i], self.__subject, self.__body)

        sleep(2)
        # Close Browser
        driver.close()

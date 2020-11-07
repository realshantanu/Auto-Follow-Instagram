from selenium import webdriver# pip install selenium
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[contains(@href,'accounts/login/')]")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)


    def follow(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button")
                like_button().click()
               
                for second in reversed(range(0, random.randint(60,62))):
                    print_same_line("#" + hashtag + ': unique users left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1

if __name__ == "__main__":

    username = "***USERNAME***"
    password = "***PASSWORD***"

    nm = InstagramBot(username, password)
    nm.login()

    hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
                'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            nm.follow(tag)
            
        except Exception:
            nm.closeBrowser()
            time.sleep(60)
            nm = InstagramBot(username, password)
            nm.login()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        email=bot.find_element_by_name('username')
        password=bot.find_element_by_name('password')

        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_post(self,hashtag):
        count=0
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            posts = bot.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]

            for link in links:
                count=count+1
                if(count<45):
                    bot.get(link)
                    try:
                        
                    
                        div=bot.find_elements_by_class_name('dCJp8')
                   
                        lov = [el.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click() for el in div]
                        
                        time.sleep(7)
                    except Exception as ex:
                        time.sleep(60)
                else:
                    bot.close() 

obj = InstagramBot('indirarealdeal','thankunext13')
obj.login()
obj.like_post('brushlettering')


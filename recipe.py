#contains all the functions(methods) that makes the bot work    
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="food"
)

mycursor=db.cursor()

import selenium
import recipe.constants as const
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

mycursor.execute("CREATE TABLE IF NOT EXISTS recipenames(id int PRIMARY KEY AUTO_INCREMENT, title VARCHAR(200) NOT NULL)")
#mycursor.execute("DROP TABLE recs")

#for x in mycursor:
    #print(x)

class Recipe(webdriver.Chrome):
    def __init__(self,driver_path="C:\Program Files (x86)\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        #this creates an instance of the class 
        super(Recipe,self).__init__()
        #self.implicitly_wait(10)
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        time.sleep(10)
        
    def check_menu(self,option=None):
        menu = self.find_element("id","comp-l3a05w62")
        menu.click()
        time.sleep(4)
        close_menu = self.find_element("id","comp-l3a8k0ec2")
        close_menu.click()
        
        #recipe = self.find_elements("id","comp-l3a8jo5x")
        #for types in recipe:
            #print(types.text)
        
        #youtube channel
        #ytb = self.find_element("css selector",'a[href="https://www.youtube.com/c/JoshuaWeissman"]')
        #ytb.click()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        
    def search_recipe(self,item):
        search_bar = self.find_element("id","input_comp-l3h18pte7")
        #search_bar.clear()
        search_bar.send_keys(item)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(5)
        
    def list_recipe(self):
        recipe = self.find_elements("css selector",'h2[class="font_2"]')
        recipes = []
        for types in recipe:
            print(types.text)
            recipes.append(types.text) 
        print("\n")
        print(recipes)
        
        query = "INSERT INTO recipenames (title) VALUES (%s)"
        #for x in range(len(recipes)):
        value = [(val,) for val in recipes]
        mycursor.executemany(query,value)
        db.commit()
        
    def view_recipe(self):
        view_recipe = self.find_element("link text","VIEW RECIPE")
        view_recipe.click()
        time.sleep(10)
        
        #for rec in view_recipe:
            #print(rec)
        
        #heading = self.find_elements("tag name","strong")
        new = self.find_element("tag name","ul")
        #print(heading.text)
        recs = []
        print(new.text)
        recs.append(new.text)
        print(recs)
            
            #print("\n")
            #print(ing.text)  
        self.back()
        


        
        
        
        

        


        
        
            
    
        
            
        
        
        
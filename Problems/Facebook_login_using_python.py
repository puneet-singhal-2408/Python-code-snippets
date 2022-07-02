from selenium import webdriver # importing webdriver from seleninum library
from time import sleep # need to provide time for page to load
#taking user input id and password 
usr=input('Enter Email Id:')
pwd=input('Enter Password:')

# opening chrome using chromedriver / path need to be specified. 
driver = webdriver.Chrome('C:/Users/PUNEET SINGHAL/Downloads/myfold')
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(2) 

username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(2) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished")


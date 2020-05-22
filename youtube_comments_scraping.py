import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Change working directory
os.chdir("ADD YOUR DIRECTORY HERE")

# Change chrome path
chrome_path = "CHANGE YOUR PATH HERE"
# Add video link
webpage_url = "ADD YOUR LINK HERE"  


driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(webpage_url)
time.sleep(0.5)

# Get the video title
title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
print(title)

# Load comments
SCROLL_PAUSE_TIME = 2
CYCLES = 7


html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)  
html.send_keys(Keys.PAGE_DOWN)  
time.sleep(SCROLL_PAUSE_TIME * 3)
for i in range(CYCLES):
    html.send_keys(Keys.END)
    time.sleep(SCROLL_PAUSE_TIME)


comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
youtube_comments = [elem.text for elem in comment_elems]

# Output
with open('comments.json', 'w') as f:
    json.dump(youtube_comments, f)



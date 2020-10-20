from selenium import webdriver
import bs4, sys


driver = webdriver.Chrome()
site = input('Which website would you like to use, reddit or instagram?')

if site == 'reddit':
    driver.get('https://www.reddit.com/')
elif site == 'instagram':
    raise Exception('instagram use has not yet been implemented')        # User-generated error message
    #driver.quit()
    # sys.exit()
else:
    #print('Wrong website has been entered')
    raise Exception('Wrong website has been entered')         # User-generated error message


searchElem = driver.find_element_by_id('header-search-bar')

subreddit = input('Which subreddit would you like to see?')
subreddit = str('r/' + subreddit)
searchElem.send_keys(subreddit)
searchElem.submit()

subredditElem = drive





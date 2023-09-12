# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip as pc

PATH = "/Users/ranganray/Desktop/Twitter-scrape/chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

subject = '"third party logistics"'
# searching (#WarehouseManagement) gives tweets with hashtag


# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("99_testing")  # enter Username
next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

sleep(4)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("R@ng@nr@y123")  # enter Passwork
log_in = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(5)
search_box = driver.find_element(
    By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"
)
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(4)
top = driver.find_element(By.XPATH, "//span[contains(text(),'Top')]")
top.click()


Flags = []
UserTags = []
TimeStamps = []
Tweets = []
Replys = []
reTweets = []
Likes = []
Urls = []
tweet_links = []
Limit = 30  # no of scrolls.
y = 1000

for t in range(0, Limit, 1):
    articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

    for article in articles:
        TimeStamp = driver.find_element(By.XPATH, ".//time").get_attribute("datetime")

        if TimeStamp not in Flags:
            UserTag = driver.find_element(
                By.XPATH, ".//div[@data-testid='User-Name']"
            ).text
            UserTags.append(UserTag)

            TimeStamp = driver.find_element(By.XPATH, ".//time").get_attribute(
                "datetime"
            )
            TimeStamps.append(TimeStamp)
            Flags.append(TimeStamp)

            Tweet = driver.find_element(
                By.XPATH, ".//div[@data-testid='tweetText']"
            ).text
            Tweets.append(Tweet)

            Reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
            Replys.append(Reply)

            reTweet = driver.find_element(
                By.XPATH, ".//div[@data-testid='retweet']"
            ).text
            reTweets.append(reTweet)

            Like = driver.find_element(By.XPATH, ".//div[@data-testid='like']").text
            Likes.append(Like)

            link = article.find_element(By.XPATH, ".//time/..").get_attribute("href")
            tweet_links.append(link)

    driver.execute_script("window.scrollTo(0, " + str(y) + ")")
    y += 1000
    sleep(2)

for link in tweet_links:
    driver.execute_script(f"window.open('{link}', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    Urls.append(driver.current_url)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(2)


print(
    len(UserTags),
    len(TimeStamps),
    len(Tweets),
    len(Urls),
    len(Replys),
    len(reTweets),
    len(Likes),
)

import pandas as pd

df = pd.DataFrame(
    zip(UserTags, TimeStamps, Tweets, Urls, Replys, reTweets, Likes),
    columns=["UserTags", "TimeStamps", "Tweets", "Urls", "Replys", "reTweets", "Likes"],
)
df.head()
df.to_csv(
    r"/Users/ranganray/Desktop/Twitter-scrape/12th_September_Top_3PL.csv",
    index=False,
)


# to click on a profile
# profile = driver.find_element(
#    By.XPATH,
#    "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]",
# )
# profile.click()


# UserTag = driver.find_element(By.XPATH, "//div[@data-testid='User-Name']").text
# TimeStamp = driver.find_element(By.XPATH, "//time").get_attribute("datetime")
# Tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweetText']").text
# Reply = driver.find_element(By.XPATH, "//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH, "//div[@data-testid='retweet']").text
# Like = driver.find_element(By.XPATH, "//div[@data-testid='like']").text

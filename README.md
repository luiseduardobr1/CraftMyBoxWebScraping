# CraftMyBox - Best Price - Web Scraping
Extract the lowest price on a computer components (like gpu) from [CraftMyBox](https://craftmybox.com/) website and save in a CSV file. 

# Requirements
* [Selenium](https://selenium-python.readthedocs.io/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Pandas](https://pandas.pydata.org/)
* [Chromedriver](https://chromedriver.chromium.org/downloads)

# Motivation
CraftMyBox is a similar brazilian version of [PCPartPicker](https://pcpartpicker.com/) which helps to build a PC with good components prices and compatibility. This code searches for video cards (gpu) on the website, gets their prices, saves them in a CSV file which can be manipulated to analyse the best day to make the purchase. After small modifications on the code, it's possible to search for different components like processors, monitors and others. 

# How to use it
1) Install all necessary libraries in *Requirements*. 

2) Download the compatible [Chromedriver](https://chromedriver.chromium.org/downloads) version to your system. 

3) Change the video card name in:
```python
...
# Search
...
searchbox.send_keys("rtx 2080")
...
```

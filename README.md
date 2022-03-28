# Getty Images Webscraper

Webscrapes Getty Images

## Requirements:
1. Selenium 
2. urlib.request
3. time
4. os
5. ChromeDriver (update the path to your downloaded chromedriver in the code)
Before this, download Chromedriver at: https://sites.google.com/chromium.org/driver/ by selecting the appropriate driver based on your chrome version.

## Usage
This Webscraper tool is designed to extract images from the Getty website (https://www.gettyimages.in/), by finding the image elements using the xpath locator and clicking on the next button via a pagination loop to extract images from every page.

In this xpath element locator, we traverse through the whole html tree and locate the image class 'MosaicAsset-module__thumb___epLhd' for all images. For the css element locator we locate and click on the next button '.PaginationRow-module__nextButton___PYo5w' to get the images from each page.

## How to use it:

1. Go to https://www.gettyimages.in/ and key in the object you are searching for in the search bar 
2. Copy the url link (e.g. https://www.gettyimages.com/search/2/image?family=creative&phrase=bag)
3. Scroll down webpage end to view feasible number of pages that can be downloaded (do not exceed this number as looping and duplicates will occur)
4. Create a destination path for scraped images to reside
5. Run the code and input the information above


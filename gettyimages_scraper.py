from selenium import webdriver
import urllib.request
import time
import os


def download_image(image_searchname, src, seq, dir):
    try:
        filename = image_searchname + "_" + str(seq) + '.jpg' # i.e: "bags_0.jpg"
        image_path = os.path.abspath(os.path.join(os.getcwd(), dir, filename)) # /home/user/Desktop/dirname
        urllib.request.urlretrieve(src, image_path) # download image
    
    except Exception:
        pass


def browse_page(image_searchname, pages, dir):
    seq = 0 #initialize the file number. 
    for i in range(pages): # Loop for the number of pages you want to scrape.
        try:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # Scroll to the end of page.
            time.sleep(2) # Wait for all the images to load correctly.
            images = driver.find_elements_by_xpath("//img[contains(@class, 'gallery-asset__thumb gallery-mosaic-asset__thumb')]") # Find all images.
        except:
            continue

        for image in images: # For each image in one page:
              try:
                src = image.get_attribute('src') # Get the link
                download_image(image_searchname, src, seq, dir) # And download it to directory
              except:
                pass
              seq += 1
        try:
          nextpage = driver.find_element_by_css_selector('.search-pagination__button-icon--next').click() # Move to next page
        except:
          pass
        time.sleep(2)
  
if __name__ == '__main__':
    image_searchname = input("Please Provide The name used to search for your images: \n") 
    url = '' #input('Please Provide The Page URL: \n')
    dir = "scraped_images/ships/"
    pages = 1    #int(input('Please Provide How Many Pages You Want To Be Scrapped: \n'))
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome() # IF YOU ARE USING CHROME.	
    driver.maximize_window()
    driver.get(url)
    if not os.path.isdir(dir): # If the folder does not exist in working directory, create a new one.
        os.makedirs(dir)
    browse_page(image_searchname, pages, dir)

			
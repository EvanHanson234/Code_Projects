# EXAMPLE!!! This is an example of a scraper that I made for a project. It is not the final version of the scraper.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import os
import time

# Variables --
# First Tab Variables
print("Location Format: City, State Zip, Country. ex: Cincinnati, OH 45202, USA")
location = input("Enter a Location: ") #format: "City, State Zip, Country". ex: "Cincinnati, OH 45202, USA"
#location = "Spring, TX 77386, USA" #format: "City, State Zip, Country". ex: "Cincinnati, OH 45202, USA"
url = "https://lost.petcolove.org/"
print("You are scraping: https://lost.petcolove.org/")
i_lost_a_pet_XPATH = "//*[@id='homepage-hero1']/div[1]/div/div/div[3]/div/div[1]/button/span/span[contains(text(), 'I Lost a Pet')]"
continue_button_XPATH = "//*[@id='app']/div[3]/div/div/div[2]/button/span[contains(text(), 'Continue')]"
search_all_pets_button_XPATH = "//*[@id='app']/div[4]/div/div/div[2]/div/div/p/a[contains(text(), 'Search All Pets')]"
card_XPATH = "//*[@id='app']/div[3]/main/div/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]"
# Second Tab Variables
pet_information_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div"
load_more_button_XPATH = "//*[@id='app']/div[3]/main/div/div/div[1]/div[3]/div[2]/div[2]/button"
animal_id_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/p[2]"
gender_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[3]/p[2]"
kennel_number_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[4]/p[2]"
microchip_number_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[5]/p[2]"
found_location_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[6]/p[2]"
found_date_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[7]/p[2]"
shelter_name_XPATH ="//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/p[2]"
email_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[2]/p[2]/a"
address_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]/p[2]"
phone_XPATH = "//*[@id='app']/div/main/div/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[4]/p[2]/a"

# Get start time for script
start_time = time.time()

# Initialize a Chrome driver
# Create options object with incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)
action_chains = ActionChains(driver)


# CRAWLING ***************************************************************

# Navigate to the lost pets website
driver.get(url)

# Wait for the "I Lost a Pet" button to load
element = wait.until(EC.presence_of_element_located((By.XPATH, i_lost_a_pet_XPATH)))

# Print the title of the page
print(driver.title)

# Find the "I Lost a Pet button" and click it
lost_button = driver.find_element(By.XPATH, i_lost_a_pet_XPATH)
lost_button.click()

# Print the text of the button
print(lost_button.text)

# Navigate to the input field for the location and enter the location -- comment this out when location is cached in browser
location_input = driver.find_element(By.CSS_SELECTOR, "input[data-cy='location-text-geolocation']")
time.sleep(2)
location_input.clear()
print("location input cleared")
location_input.send_keys(location)
location_input.send_keys(Keys.RETURN)
time.sleep(2)

# Find the "Continue" button and click it
continue_button = driver.find_element(By.XPATH, continue_button_XPATH)
continue_button.click()
time.sleep(.5)
continue_button.click() # For some reason, the button needs to be clicked twice

# Wait for the page to load
element = wait.until(EC.presence_of_element_located((By.XPATH, search_all_pets_button_XPATH)))

# Navigate to the Search All Pets button
search_button = driver.find_element(By.XPATH, search_all_pets_button_XPATH)

# Wait until the button is clickable, click it
element = wait.until(EC.element_to_be_clickable((By.XPATH, search_all_pets_button_XPATH)))
time.sleep(1)
search_button.click()


# SCRAPING ***************************************************************

# Wait for the page to load
element = wait.until(EC.presence_of_element_located((By.XPATH, card_XPATH)))

# Find and click the "Load More Results" button ------------------- I AM TURNING THIS OFF FOR NOW TO POPULATE THE DATABASE
# ***IDEA = To make this better, I can use a try/except block to check if the button is there, and if it is, click it. If it isn't, then I can move on to the next step.***
#load_more_button = driver.find_element(By.XPATH, load_more_button_XPATH)
#load_more_button.click()
#time.sleep(1)
#load_more_button = driver.find_element(By.XPATH, load_more_button_XPATH)
#load_more_button.click()
#time.sleep(1)
#load_more_button = driver.find_element(By.XPATH, load_more_button_XPATH)
#load_more_button.click()
# Scroll to the top of the page
#driver.execute_script("window.scrollTo(0, 0)")
# ----------------------------------------------------------------- I AM TURNING THIS OFF FOR NOW TO POPULATE THE DATABASE

# Loop through and find all of the cards and click on them
# First, get the height of the browser window
page_height = driver.execute_script("return window.innerHeight")
cards = driver.find_elements(By.CSS_SELECTOR, " div.v-card__actions")
time.sleep(2)

# Pet Counter
i = 1

# Scraping Function
for card in cards:
    # Pet Counter
    print(i)
    i += 1

    # This was originally used before I split the card text into a list
    #print(card.text)

    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, " div.v-card__actions")))
        card.click()
    except ElementClickInterceptedException:
        print("ElementClickInterceptedException")
        # Try to click on the "X" to close the card, Move the mouse to the desired location and click
        time.sleep(3)
        action_chains.move_by_offset(10, 10).click().perform()
        pass

    # Split the card text into a list
    cardSplit = card.text.split('\n')

    category = cardSplit[0]
    last_seen = cardSplit[1]
    distance = cardSplit[2]

    print("Category: " + category)
    print("Last Seen: " + last_seen)
    print("Distance: " + distance)

    # Then, scroll down by that amount
    #i = -1
    #if i % 2 == 0:
    #    driver.execute_script(f"window.scrollBy(0, {page_height})")

    # Get the new url and print it
    new_url = driver.current_url
    print("Pet URL: " + new_url)

    # Click on the "X" to close the card, Move the mouse to the desired location and click
    action_chains.move_by_offset(5, 5).click().perform()

    # Reset the actions and move the mouse back to its original position
    # maybe needs to be --> action_chains.reset_actions().preform()
    action_chains.reset_actions()

    # Open the new url in a new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(new_url)

    # Wait for the page to load
    #time.sleep(.1)

    # Print the pet information ***************************************************************
    #pet_information = driver.find_element(By.XPATH, pet_information_XPATH)
    #print(pet_information.text)

    # Create a list of lists to store the data
    data = []

    # Print the Anaimal ID
    try:
        animal_id = driver.find_element(By.XPATH, animal_id_XPATH)
        print("Animal ID: " + animal_id.text)
    except NoSuchElementException:
        print("No Animal ID")
        pass

    # Print the Gender
    try:
        gender = driver.find_element(By.XPATH, gender_XPATH)
        print("Gender: " + gender.text)
    except NoSuchElementException:
        print("No Gender")
        pass

    # Print the Kennel Number
    try:
        kennel_number = driver.find_element(By.XPATH, kennel_number_XPATH)
        print("Kennel #: " + kennel_number.text)
    except NoSuchElementException:
        print("No Kennel Number")
        pass

    # Print the Microchip Number
    try:
        microchip_number = driver.find_element(By.XPATH, microchip_number_XPATH)
        print("Microchip #: " + microchip_number.text)
    except NoSuchElementException:
        print("No Microchip Number")
        pass

    # Print the Found Location
    try:
        found_location = driver.find_element(By.XPATH, found_location_XPATH)
        print("Found Location: " + found_location.text)
    except NoSuchElementException:
        print("No Found Location")
        pass

    # Print the Found Date
    try:
        found_date = driver.find_element(By.XPATH, found_date_XPATH)
        print("Found Date: " + found_date.text)
    except NoSuchElementException:
        print("No Found Date")
        pass

    # Print the Shelter Name
    try:
        shelter_name = driver.find_element(By.XPATH, shelter_name_XPATH)
        print("Shelter Name: " + shelter_name.text)
    except NoSuchElementException:
        print("No Shelter Name")
        pass

    # Print the Email
    try:
        email = driver.find_element(By.XPATH, email_XPATH)
        print("Email: " + email.text)
    except NoSuchElementException:
        print("No Email")
        pass

    #Print the Address
    try:
        address = driver.find_element(By.XPATH, address_XPATH)
        print("Address: " + address.text)
    except NoSuchElementException:
        print("No Address")
        pass

    # Print the Phone Number
    try:
        phone = driver.find_element(By.XPATH, phone_XPATH)
        print("Phone #: " + phone.text)
    except NoSuchElementException:
        print("No Phone Number")
        pass

    print("")

    # Append the row to the data list
    data.append([
        animal_id.text,
        new_url,
        category,
        last_seen,
        distance,
        gender.text,
        kennel_number.text,
        microchip_number.text,
        found_location.text,
        found_date.text,
        shelter_name.text,
        email.text,
        address.text,
        phone.text,
    ])

    # Check if the file is empty
    if os.stat("output.csv").st_size == 0:
        # Open a new CSV file
        with open('output.csv', 'w', newline='') as csvfile:
            # Create a writer object
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow([
                'animal_id',
                'pet_url',
                'category',
                'last_seen',
                'distance',
                'gender',
                'kennel_number',
                'microchip_number',
                'found_location',
                'found_date',
                'shelter_name',
                'email',
                'address',
                'phone_number',
            ])

    # Open the CSV file in append mode
    with open('output.csv', 'a', newline='') as csvfile:
        # Create a writer object
        writer = csv.writer(csvfile)

        # Loop through the data and write each row to the CSV file
        for row in data:
            writer.writerow(row)

    # Close the second tab and switch to the first tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Finished with the driver, close it
driver.quit()

# Print the time it took to run the script
print("--- %s seconds ---" % (time.time() - start_time))
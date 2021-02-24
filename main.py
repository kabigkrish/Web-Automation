from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from xl_to_dataclass import member_class
from selenium.webdriver.common.keys import Keys
from dataclasses import asdict
from selenium.webdriver.support.ui import Select
import time
import os
for i in range(0,len(member_class)):

    def enable_download_headless(browser,download_dir):
        browser.command_executor._commands["send_command"]=("POST",'/session/$sessionId/chromium/send_command')
        params={'cmd':'Page.setDownloadBehavior','params':{'behavior':'allow','downloadPath':download_dir}}
        browser.execute("send_command",params)

    chrome_options = Options()
    ## to run everything background
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('prefs',  {
        "download.default_directory": "/home/Desktop",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        'profile.default_content_setting_values.automatic_downloads': 1
        }
    )

    browser = webdriver.Chrome(options = chrome_options)
    driver = webdriver.Chrome(options = chrome_options)
    download_dir="/home/kabigkrish/1_my_drive/engineering/selinium project/"
    enable_download_headless(driver,download_dir)

    a=asdict(member_class[i])

    driver.maximize_window()
    driver.get('https://enrollmentdemo.solartis.net/')
    quote_buy_button=driver.find_element_by_xpath('//*[@id="frontpage"]/a/img')
    quote_buy_button.click()
    plan=driver.find_element_by_id("MO250")
    plan.click()
    i_want_to_purchase_button=driver.find_element_by_xpath('//*[@id="quoteSummaryDiv"]/table/tbody/tr/td/table/tbody/tr/td/a/img')
    i_want_to_purchase_button.click()

    #info page details
    member_number_box=driver.find_element_by_xpath('//*[@id="EAANumber"]')
    member_number_box.send_keys(a.get('member_number'))
    ##
    first_name_box=driver.find_element_by_xpath('//*[@id="firstName"]')
    first_name_box.send_keys(a.get('first_name'))
    ##
    last_name_box=driver.find_element_by_xpath('//*[@id="lastName"]')
    last_name_box.send_keys(a.get('last_name'))
    ##
    date_of_birth_box=driver.find_element_by_xpath('//*[@id="insuredDateOfBirth"]')
    date_of_birth_box.send_keys(a.get('date_of_birth'))
    ##
    address_1_box=driver.find_element_by_xpath('//*[@id="address1"]')
    address_1_box.send_keys(a.get('address_1'))
    ##
    city_box=driver.find_element_by_xpath('//*[@id="city"]')
    city_box.send_keys(a.get('city'))
    ##
    zip_code_box=driver.find_element_by_xpath('//*[@id="autocompleteNomeIdInput"]')
    zip_code_box.send_keys(a.get('zip_code'))
    ##
    email_address_box=driver.find_element_by_xpath('//*[@id="email"]')
    email_address_box.send_keys(a.get('email_address'))
    ##
    contact_number_box=driver.find_element_by_id('phone')
    contact_number_box.send_keys(a.get('contact_number'))
    ##
    state_box=Select(driver.find_element_by_xpath('//*[@id="state"]'))
    state_box.select_by_visible_text(a.get('state'))
    ##
    continue_button=driver.find_element_by_xpath('//*[@id="submitCertReq2"]')
    continue_button.click()
    ###
    time.sleep(10)
    add_beneficiary_button=driver.find_element_by_xpath('//*[@id="j_idt53"]')
    add_beneficiary_button.click()
    time.sleep(2)
    beneficiary_first_name_box=driver.find_element_by_xpath('//*[@id="beneficiaryFirstName"]')
    beneficiary_first_name_box.send_keys(a.get('beneficiary_first_name'))
    beneficiary_last_name_box=driver.find_element_by_xpath('//*[@id="beneficiaryLastName"]')
    beneficiary_last_name_box.send_keys(a.get('beneficiary_last_name'))
    relationship_box=driver.find_element_by_xpath('//*[@id="relationship"]')
    relationship_box.send_keys(a.get('relationship'))
    percentage_of_benefit_box=driver.find_element_by_xpath('//*[@id="Beneficiarypercentage"]')
    percentage_of_benefit_box.clear()
    percentage_of_benefit_box.send_keys(a.get('percentage_of_benefit'))
    save_button=driver.find_element_by_xpath('//*[@id="j_idt127"]')
    save_button.click()
    continue_2_button=driver.find_element_by_xpath('//*[@id="j_idt55"]')
    continue_2_button.click()
    time.sleep(5)
    card_type_box=Select(driver.find_element_by_xpath('//*[@id="cardType"]'))
    card_type_box.select_by_visible_text('MasterCard')
    card_number_box=driver.find_element_by_xpath('//*[@id="cardNumber"]')
    card_number_box.send_keys('5555555555554444')
    ##
    """
    expiry_month_box=select(driver.find_element_by_xpath('//*[@id="ExpiryMonth"]'))
    expiry_month_box.select_by_visible_text('')
    expiry_year_box=select(driver.find_element_by_xpath('//*[@id="ExpiryYear"]'))
    expiry_year_box.select_by_visible_text('')
    """
    cvv_box=driver.find_element_by_xpath('//*[@id="cvvNumber"]')
    cvv_box.send_keys('123')
    confirm_email_box=driver.find_element_by_xpath('//*[@id="confirmEmailAddress"]')
    confirm_email_box.send_keys(a.get('email_address'))
    continue_3_button=driver.find_element_by_xpath('//*[@id="j_idt109"]')
    continue_3_button.click()
    time.sleep(5)
    terms_condition_click=driver.find_element_by_xpath('//*[@id="agree"]')
    terms_condition_click.click()
    time.sleep(2)
    purchase_button=driver.find_element_by_xpath('//*[@id="pay"]')
    purchase_button.click()
    time.sleep(5)
    reciept_pdf=driver.find_element_by_xpath('//*[@id="ReceiptPDF"]')
    reciept_pdf.click()
    coi_pdf=driver.find_element_by_xpath('//*[@id="COIPDF"]')
    coi_pdf.click()

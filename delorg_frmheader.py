from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost:8888")
driver.implicitly_wait(12)
driver.maximize_window()
#login into the page
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("manager")
driver.find_element_by_id("submitButton").click()
driver.find_element_by_link_text("Organizations").click()
driver.find_element_by_xpath("//img[contains(@title,'Create Organization')]").click()
#create organisation using organisation name
driver.find_element_by_name("accountname").send_keys("samsung010")
driver.find_element_by_xpath("//input[contains(@onclick,'return copyAddressLeft(EditView)')]").click()
driver.find_element_by_name("button").click()

wb=driver.find_element_by_xpath("//span[@class='dvHeaderText']")
act_mesg=wb.text
print(act_mesg)
assert act_mesg,True
False
#delete the organisation in header section by selecting multiple check boxes
driver.find_element_by_link_text("Organizations").click()
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//input[@class='crmbutton small delete']").click()
# if we want delete for particular organisation name  use these xpath
#driver.find_element_by_xpath("//a[@title='Organizations' and text()='samsung0011']/../..//input").click()
#using alert class accept the pop up
alt=driver.switch_to.alert
alt.accept()
list_01=driver.find_elements_by_xpath("//a[@title='Organizations']")
for i in list_01:
    print(i.text)
    assert i=="samsung01010",False
    True





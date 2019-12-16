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
driver.find_element_by_name("accountname").send_keys("samsung01010")
driver.find_element_by_name("button").click()
wb=driver.find_element_by_xpath("//span[@class='dvHeaderText']")
act_mesg=wb.text
expec_mesg=act_mesg
print(act_mesg)
assert act_mesg == expec_mesg,True
False
#delete the organisation in Action section by select the del option
driver.find_element_by_link_text("Organizations").click()
driver.find_element_by_xpath("//a[text()='del']").click()
#using alert class dismiss the pop up
alt=driver.switch_to.alert
alt.dismiss()
driver.refresh()
list_01=driver.find_elements_by_xpath("//a[@title='Organizations']")
for i in list_01:
    print(i.text)
    assert i=="samsung01010",False
    True
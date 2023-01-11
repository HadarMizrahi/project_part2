from function_frontend_testing import driver_conn, get_frontend_test, element_test

#The functions contact the FRONTEND server to check the element in the browser
driver = driver_conn("C:\\Users\Hadar_Mi\Downloads\chromedriver_win32\chromedriver")
get_frontend_test(driver,"http://127.0.0.1:5001/users/get_user_data/1")
web_element=element_test(driver)
print(web_element)
driver.quit()


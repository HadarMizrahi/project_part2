from function_backend_testing import post_test, get_backend_test, check_username_test
from function_frontend_testing import driver_conn, get_frontend_test, element_test

#The functions contact the BACKEND server to insert a user into the database with a POST request type,
#receiving the data that the user appears in the table with a GET type request
#and checking that the user exists in the database
post_test('http://127.0.0.1:5000/users/3', 'Or')
get_backend_test('http://127.0.0.1:5000/users/3')
check_username_test(3, 'Or')

#-----------------------------------------------------------------------------------------------------
#The functions contact the FRONTEND server to check the element in the browser
driver = driver_conn("C:\\Users\Hadar_Mi\Downloads\chromedriver_win32\chromedriver")
get_frontend_test(driver,"http://127.0.0.1:5001/users/get_user_data/3")
element_test(driver)
driver.quit()
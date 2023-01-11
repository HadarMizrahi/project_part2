from function_backend_testing import post_test, get_backend_test, check_username_test

#The functions contact the BACKEND server to insert a user into the database with a POST request type,
#receiving the data that the user appears in the table with a GET type request
#and checking that the user exists in the database
post_test('http://127.0.0.1:5000/users/2', 'Hadar')
get_backend_test('http://127.0.0.1:5000/users/2')
check_username_test(2, 'Hadar')


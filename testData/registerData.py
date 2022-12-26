import random
import string

# first name and last name
firstName = "Rezwan"
lastName = "Haque"

# date of birth : day, month, year
date = random.randint(1, 31)
month = "April"
year = random.randint(1900, 2000)

# Email Field
email = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@yahoo.com"

# Company field
company = "Robi Axiata"

# password
password = "Robi@123"

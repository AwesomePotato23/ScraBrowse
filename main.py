import time
import os

os.system("clear")

print("Please make sure to capitalize correct parts of the username :)")

while True:
  searchThis = input("What user would you like to search? ")
  print()
  print("User data:")
  from ScraGet import ScraGet
  user = ScraGet.get_user()
  user.updateScratch(searchThis)
  print("Name: " + user.username)
  print("ID: " + str(user.id))
  print("Joined: " + str(user.join_date))
  print("Country: " + str(user.country))
  print()

# Planning on updating if ScraGet ever has new features.
# Also going to add Studio searching lol, maybe DB things too xD
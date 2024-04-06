guest_List = ["Ayesha", "Safa", "Muqeema", "Fatima"]
host = "Ayesha"
for guests in guest_List:
    print("Dear {0}, \nI would like to invite you for a dinner. \nYours sincerely, \n{1}".format(guests, host))

print("\n################")

print("{0}\tCan't make it to the dinner".format(guest_List[0]))
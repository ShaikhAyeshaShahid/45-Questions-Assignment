guest_List = ["Ayesha", "Safa", "Muqeema", "Fatima"]
host = "Ayesha"
for guests in guest_List:
    print("Dear {0}, \nI would like to invite you for a dinner. \nYours sincerely, \n{1}".format(guests, host))

print("\n################")

print("Updated Guest List")

print("\n################")


remove_guest = "Ayesha"
add_guest = "Sarah"
guest_List.remove(remove_guest)
guest_List.append(add_guest)

for updatedGuest in guest_List:
    print("Dear {0}, \nI would like to invite you for a dinner. \nYours sincerely, \n{1}".format(updatedGuest, host))

print("\n################")

print("Found a bigger table for dinner")
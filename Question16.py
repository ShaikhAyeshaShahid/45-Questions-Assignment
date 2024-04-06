guest_List = ["Ayesha", "Safa", "Muqeema", "Fatima"]
host = "Ayesha"
# for guests in guest_List:
#     print("Dear {0}, \nI would like to invite you for a dinner. \nYours sincerely, \n{1}".format(guests, host))

print("\n################")

print("Updated Guest List")

print("\n################")


add_guest1 = "Sarah"
add_guest2 = "Isra"
add_guest3 = "Sabaun"
guest_List.insert(0,add_guest1)
guest_List.insert(3, add_guest2)
guest_List.append(add_guest3)

for updatedGuest in guest_List:
    print("Dear {0}, \nI would like to invite you for a dinner. \nYours sincerely, \n{1}".format(updatedGuest, host))


print("\n We are sorry to inform you that the table we have booked doesn't make on time so we are inviting only 2 person for a dinner")
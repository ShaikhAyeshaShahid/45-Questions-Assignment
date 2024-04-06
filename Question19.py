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

while len(guest_List) > 2:
    remove_guest = guest_List.pop()
    print(f"Sorry {remove_guest}, the dinner table won't arrive in time, and I can only invite two guests.")

print ("invitations to the two remaining guests")

print("\n*** Remaining Invitations ***")
for remaining_guest in guest_List:
    print(f"Dear {remaining_guest},\nYou're still invited to dinner. Looking forward to seeing you!\n\nSincerely,{host}")

print("Empty the list")
guest_List.clear()

# Print to make sure the list is empty
print("\n*** Empty Guest List ***")
print(guest_List)

num_guest= len(guest_List)
print(num_guest)
print ("Places to visit array")
places_to_visit = ["Macca", "Madina", "Iraq", "Sydney", "Rome"]

print ("####Original order####")
print("Original Order:", places_to_visit)

print ("####Alphabetical order without modifying the actual list####")
print("Alphabetical Order:", sorted(places_to_visit))

print ("####The array is still in its original order####")
print("Original Order (still):", places_to_visit)

print ("####Reverse alphabetical order without changing the original list####")
print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))

print ("####The array is still in its original order####")
print("Original Order (still):", places_to_visit)

print("####Reverse the order of the list####")
places_to_visit.reverse()
print("Reversed Order:", places_to_visit)

print("####Reverse the order again to get back to the original order####")
places_to_visit.reverse()
print("Back to Original Order:", places_to_visit)

print("####Sort the array in alphabetical order####")
places_to_visit.sort()
print("Sorted in Alphabetical Order:", places_to_visit)

print("####Sort the array in reverse alphabetical order####")
places_to_visit.sort(reverse=True)
print("Sorted in Reverse Alphabetical Order:", places_to_visit)

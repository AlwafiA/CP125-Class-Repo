# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type =="Electric":
        rate = 2.00
    elif vehicle_type == "Hybrid":
        if hour_24 >= 6 and hour_24 <=22 : 
            rate =  2.00
        else :
           rate =  5.00 
    else :
        rate = 5.00
    return rate
 

#Merge remote-tracking branch 'upstream/main'
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
#~                                                                                                                                                              ~                                                                                                                                                              ~                                                                                                                                                              ~                                                                                                                                                              ~                                                                                                                                                              .git/MERGE_MSG [unix] (07:59 01/01/1970)                                                                                                                6,1 All
#E211: File ".git/MERGE_MSG" no longer available   
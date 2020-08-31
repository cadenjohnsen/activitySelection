#!/bin/env python3
from random import randint  # import the random integer function

# function for the last to start activity selection algorithm
def activity_selection(taskNum, activities):
    i, j = 0, 0
    activitiesSelected = []
    activityCounter = 0
    startLength = activities[0][2]  # get the starting position of the first data point

    while  (j < taskNum) and (activities[j][1] < startLength):  # loop through the start times while they are less than the first one
        if (activities[j][1] > activities[i][1]) and (activities[j][1] < activities[i][2]): # if the start time of a later one is less than a start time of the current latest, then replace
            i = j   # replace previous latest start with current values
        j += 1  # move on to the next starting value
    activitiesSelected.append(i + 1)    # the final value gets added to the activitiesSelected array
    activityCounter += 1    # increment how many activities have been selected
    j = i + 1   # start next loop after starting location
    for j in range(taskNum):    # loop through the rest of the activities
        if (activities[j][1] >= activities[i][2]):  # check if the current activity starts after the previous one ends
            activitiesSelected.append(j + 1)    # add the value to the array
            activityCounter += 1    # count how many activities have been selected
            i = j   # change previous index to point to the current
    print ("Number of Activities Selected =", activityCounter)     # prints the number of activities chosen from algorithm
    print ("Activities:", *activitiesSelected, sep = " ") # prints the activities selected array

# function to create a randomized array of containing the activity number, starting point, and ending point of each individual activity
def createRandomArray():
    i, j, k, l = 0, 0, 0, 0
    m = randint(2,5)    # select a random starting point for the first data
    activities = []      # define empty activities
    taskNum = randint(1,10)    # number of sets in activities
    activityValueNum = 3   # number of values per set in activities
    rows, cols = (activityValueNum, taskNum) # set rows and cols values

    for i in range(cols):   # loop through activities adding random values
        temp = []    # declare temp array initially empty
        for j in range(rows):
            if (j == 0):    # check if at the first variable of the data
                k += 1          # count the number of activities present
                temp.append(k)  # add the new k value into the temp array
            elif (j == 1):  # check if at the second variable of the data
                l = randint(1, m - 1)   # choose a nonzero number that is before the upper limit of the data
                temp.append(l)  # add the new l value into the temp array
            else:   # if at third variable of the data
                temp.append(m)  # add the new upper limit into the temp array
                m += randint(0, m)  # increment m by a random number that is in not extremely large
        l = 0   # reset l to 0
        activities.append(temp)  # add the new number onto the final activities

    return taskNum, activities  # send the new array and size of the array to be used by the other functions

# function to call and execute other functions
def main():
    taskNum, activities = createRandomArray()
    print ("Number of Activities =", taskNum)     # prints the number of tasks
    print ("Activities Array:", activities) # prints the entire activities array
    activity_selection(taskNum, activities) # executes the activity selection algorithm and prints out the answers

# beginning of the program to call main and start execution
if __name__ == "__main__":
	main()

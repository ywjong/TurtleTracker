# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: John Fay (john.fay@duke.edu)
# Created on: Sept, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
#fileObj = open(fileName, 'r')
fileObj = open('C:/Users/yj107/Documents/GitHub/TurtleTracker/SaraNoHeader.txt', 'r')

# Read in all lines in the text file into a list variable
lineList = fileObj.readlines()

# Closes the file object (now that we have all we need)
fileObj.close()

# Iterate through all the lines in the lineList
for lineString in lineList:

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    # Print information to the user
    print ("Record {0} indicates Sara was seen at {1}N and {2}W on {3}".format(recordID, obsLat,obsLat,obsDate))
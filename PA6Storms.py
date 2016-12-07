# Programmers:  Holly and Deb
# Course:  CS201.01, Dr. Olsen
# Date: November 30, 2016
# Programming Assignment:  PA6
# Problem Statement:
# Data In: input file name, output file name,
# Data Out:  specified storm information based on user input
# Other files needed: Stormdata_2000_shortened.csv,Stormdata_2001_shortened.csv,Stormdata_2002_shortened.csv,Stormdata_2003_shortened.csv
#Stormdata_2004_shortened.csv,Stormdata_2009_shortened.csv,Stormdata_2011_shortened.csv,Stormdata_2012_shortened.csv,Stormdata_2013_shortened.csv
# Credits: None

# Purpose: Ask the user for a filename
# Parameters: none
# Return: filename

import os
def inputFile():
    filename = input("Please input a file to read from.")
    # create a loop to error check
    while not os.path.exists(filename):
        filename = input("Error. That is not a valid file name. Please try again.")
    return filename  # return the given file name


#Purpose: read from the file
#Paramaters:filename
#Return:list

def read_file(filename):
    storms_list1 = []
    try:
        inputfile=open(filename,"r")
        for line in inputfile:
            storms_list1.append(line.split(","))
        inputfile.close()
    except FileNotFoundError:
        print("Sorry this file is not Found")
        SystemExit(1)
    return storms_list1


#Function Name:storm_graph
#Purpose:To generate a graph for the storms per month
#Parameters:storm list
#Return:graph

def storm_dict(storms_list1,graph_output_file): #Shoud be dictionary******
    import pylab
    output_file = open(graph_output_file)
    graph_dict = {}
    for graph_dict in storms_list1:
        if storms_list1[0][4:5] not in graph_dict:
            graph_dict = 1
        else:
            graph_dict += 1
    print(graph_dict,file=output_file)

# Function Name:storm_graph
# Purpose:To generate a graph for the storms per month
# Parameters:storm list
# Return:graph
def storm_graph(output_file):
    fp = open(output_file)
    x,y = [],[]
    for line in fp:
        line_list = line.strip().split()
        x.append(int(line_list[0]))
        y.append(int(line_list[1]))
    fp.close()

    pylab.ploy(x,y)
    pylab.ylabel("Number of Storms")
    pylab.xlabel("Month")
    pylab.title("Number of Storms per month")
    pylab.savefig(output_file)


#Function Name:storm_years
#Purpose:Do more storms happen in some years than others
#Parameters:storm list
#Return:none

def storm_years(storm_list1,given_storm):
      storm_dict={}
      for storm_dict in storm_list1:
          if storm_list1[7]==given_storm:
              if storm_list1[0][0:3] not in storm_dict:
                storm_dict[storm_list1[0][0:3]]=1
              else:
                storm_dict[storm_list1[0][0:3]]+=1
      return storm_dict



def storm_years_secondfile(storm_list2,given_storm):
    file2=input("Please enter another file you would like to input and compare to the orginal file")
    read_file(file2)
    storm_dict={}
    for storm_dict in storm_list2:
        if storm_list2[7] == given_storm:
            if storm_list2[0][0:3] not in storm_dict:
                storm_dict[storm_list2[0][0:3]] = 1
            else:
                storm_dict[storm_list2[0][0:3]] += 1
    return storm_dict



# Function Name:comparison_of_years
# Purpose:
# Parameters:
# Return:

def comparison_of_years(outfile_name,stormfile1,stormfile2):
    outputfile=open (outfile_name,"w")
    for line in stormfile1 and stormfile2:
            if stormfile1[0][0:3]== stormfile2[0][0:3]:
                print(line[0][0:3], file =outputfile)
    outputfile.close()




# Function Name:common_storm
# Purpose:What is the most common storm for a particular state?  **Line is not the variable - find out what you're looking for
# Parameters:storm_list, given_state **** If everything else works, make print(line) and see what comes out
# Return:storm_dict
def common_storm(storm_list1,given_state):
    storm_dict = {}
    for storm_dict in storm_list1:
        if storm_list1[5] == given_state:
            if storm_list1[7] not in storm_dict:
                storm_dict[storm_list1[7]] = 1
            else:
                storm_dict[storm_list1[7]] += 1
    return storm_dict

# Function Name:common_storm_max
# Purpose:Find the max value in a dictionary  #Should use a loop in the dictionary - same way as lists****** Do thiis
# Parameters:storm_dict
# Return:max_value
def common_storm_max(storm_dict):
    for line in storm_dict:
        if value > biggest_value:
            biggest_value = value
    return biggest_value.key


# Function Name:injuries_state
# Purpose:How many injuries in a specific state
# Parameters:storm_list, given_state2
# Return:how many injuries
def injuries_in_a_state(given_state2, storm_list1):
    total_injuries = 0
    if given_state2 == storm_list1[6]:
        for i in storm_list1:
            total_injuries += storm_list1[i][8]
    return total_injuries


def menu():
    print("The choices you have to choose from to learn more about storms are most  common storms that happened in a certain year,"+
          " how many injuries from storms in a specific state,most common storms that happened in a particular state ")
    choice = input("What would you like to know about storms?")
    return choice

def main():
    filename =inputFile()
    new_file =read_file(filename)
    print(new_file)
    choice = menu()
    if choice ==

main()
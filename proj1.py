# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:09:52 2021

@author: ashbu
"""

# Your name: Luis Solano
# Your student id: 06415334
# Your email: solanol@umich.edu
# List who you have worked with on this project:

import io
import sys
import csv
import unittest
          

def read_csv(file):
    '''
    Function to read in a CSV

    Parameters
    ----------
    file : string
        the name of the file you're reading in

    Returns
    -------
    data_dict : dict
        the double-nested dictionary that holds the data from the csv.

    '''
    '''
    how the double nested dict SHOULD look like 
    double nested dictionary  = {
        state: {'demographic1': 'exam takers/people', 'demographic2': 'exam takers/people', ...}
        state: {'demographic2': 'exam takers/people', }
        state: {}
        state: {}
        ......
        key: {value} aka key: {key:value, key:value, ...}
    }
    '''
    # write your code here that does things
    # it should read in the lines of data
    # it should also seperate the first row as header information
    # at the same time, it should grab the first item as the state information
    # the end result of the data should be formated like so
    # ex: (ap_dict) {“Alabama”: {“AMERICAN INDIAN/ALASKA NATIVE”: 1, “ASIAN”: 61,...},...}
    data_dict = {}
    row_count =  1
    data_file = open(file, "r")     # r here or Read in rownext line
    info = data_file.readlines()
    #lecture 10/4 @49.14 
    '''
     double nested dictionary  = {
        state: {'demographic1': 'exam takers/people', 'demographic2': 'exam takers/people', ...}
        state: {'demographic2': 'exam takers/people', }
    '''
    #header_info  
    line = 0
    first_line = info[0] # this a string
    header_list = first_line.strip("\n").split(',') # turns header string to list (11 items in list) 
    
    #State, AMERICAN INDIAN/ALASKA NATIVE, ASIAN,BLACK, HISPANIC/LATINO, NATIVE HAWAIIAN/OTH PACF ISL,WHITE,TWO OR MORE RACES,OTHER,NO RESPONSE,State Totals
    for line in info[1:]:
        #row = line.strip(“\n”).split(,) 
        #Line.strip(“\n”).split(“,”)
        row = line.strip("\n").split(",")
        state = row[0] 
        data_dict[state] = { }
        #value = row[]
         # to ignore "State" in header_list?
        for x in range(1,len(header_list)):
            demographic = header_list[x] # for each state, loop for each demographic ignoring "State
            value = int(row[x])
            data_dict[state][demographic] = value # assigns value to demographic in inner dictionary per state 
    return data_dict


def pct_calc(data_dict):
    '''
    Function to compute demographic percentages
    Parameters
    ----------
    data_dict : dict
        the dictionary you're passing in. Should be the data dict from the 
        census or AP data. 

    Returns
    -------
    pct_dict: dict
        the dictionary that represents the data in terms of percentage share 
        for each demographic for each state in the data set.
    '''
    '''
     double nested dictionary  = {
        state: {'demographic1': 'exam takers/people', 'demographic2': 'exam takers/people', ...}
        state: {'demographic2': 'exam takers/people', }
    '''
    # declaring dict to hold pct vals
    pct_dict = {}
    # write in code here
    # it should take the number for each demographic for each state and divide it by the state total column
    # ex: value = census_data["Alabama"]["WHITE]/census_data["Alabama]["State Totals"]
    # ex: round(value * 100, 2)) 
    #print(data_dict)
    for state in data_dict:     #iterate through outer dict
        pct_dict.setdefault(state, {} ) #
        for column in data_dict[state]: #iterate through inner dictionary 
            state_total = data_dict[state]['State Totals'] 
            if column != "State Totals": # dont want to do "State Totals column"
                value_1 = data_dict[state][column]  #get the value per demographic
                 #get state total numbers
                percentage = (value_1 / state_total) * 100 #computes proprotion in %
                percentage_rounded = round(percentage, 2)
            pct_dict[state].setdefault(column, percentage_rounded) #add percentage to pct_dict
    
    # example_dict['key1']['key2'] to get inner dictionary values
    # returns inner dictionary key values demographic value / state population        
    # get() returns value of item with specified key-> dictionaryname.get(key, value)
    #pass
    #print(data_dict)   commented this out OCT 19 10:11pm EST !!!!!!!!!!!!!!!!!!!!!!!
    return(pct_dict)


def pct_dif(data_dict1, data_dict2):
    '''
    Function to compute the difference between the demographic percentages

    Parameters
    ----------
    data_dict1 : dict
        the first data_dict you pass in. In this case, the ap_data
    data_dict2 : dict
        the second data_dict you pass in. In this case, the census_data

    Returns
    -------
    pct_dif_dict: dict
        the dictionary of the percent differences.
    '''
    #pass
    # creating the dictionary to hold the pct diferences for each "cell"
    pct_dif_dict = {}

    for state in data_dict1: # iterates through each state in outer dict
        pct_dif_dict.setdefault(state, {} ) # fill in state for each key in new outer dict
         # iterates through 2nd outer dict
        for column in data_dict1[state]:   #iterate through inner dict for both 1st and 2nd dict
                # get value of demographic in both dicts per state
            if column != "State Totals" and column != "NO RESPONSE": 
                        #value_1 = data_dict[state][column] how last fucntion got value
                first_value = data_dict1[state][column] #to get value in 1st dict
                second_value = data_dict2[state][column] #to get value in 2nd dict
                absolute_difference = abs(round((first_value - second_value), 2)) #compute absolute diff and rounds
                    #pct_dict[state].setdefault(column, percentage_rounded) how last function added values to inner dict
            pct_dif_dict[state].setdefault(column, absolute_difference) #add new values to new dictionary 
    # write code here
    # it should subtract the % val of each val in the 2nd dict from the 1st dict
    # it should take the absolute value of that difference and round it to 2 decimal places
    # ex: value = ap_data["Alabama"]["WHITE] - census_data["Alabama"]["WHITE] 
    # ex: abs(round(value, 2))
    # hint: you want to have a way to deal with the difference in naming conventions
    # ex: "North Carolina" vs "North-Carolina" string.replace is your friend
    #pass
    return(pct_dif_dict)


def csv_out(data_dict, file_name):
    '''
    Function to write output to a file    

    Parameters
    ----------
    data_dict : dict
        the data dictionary you are writing to the file. In this case, 
        the result from pct_dif_dict
        
    file_name : str
        the name of the file you are writing.

    Returns
    -------
    None. (Doesn't return anything)
    '''
    
    with open(file_name, "w", newline="") as fileout: # opens file allowing to write 
        #writer = csv.writer(file_name)  

        header = ["State"] + list(data_dict["Alabama"].keys()) #what does this do ???
        #Header_row = ["State", "AMERICAN INDIAN/ALASKA NATIVE", "ASIAN", "BLACK", "HISPANIC LATINO", "NATIVE HAWAIIAN/OTH PACF ISL", "WHITE", "TWO OR MORE RACES", "OTHER", ""]
        #   ^ ERROR bc file may have different headers and number of categories 
        #use columns??
        #first row/line should be header
        #1st column: states
        #2nd column: data (numbers) until the end 

        # how to get label to be the first line ? iterate through outer dict key and then inner dict keys
        header = ','.join(header)
        fileout.write(header + '\n')

        for info in data_dict:
            row = list(data_dict[info].values())
            row = str(row)[1:-1]
            fileout.write(info + ',' + row + '\n')
'''
        for state in data_dict:  # "for every in state in outer dict"
            #name_of_state = data_dict[state]  
            # we want to put in index 0 for every line
            for column in data_dict[state]: # iterating through inner dict
                updated_list = [data_dict[state]] # get name of state into index 0 of list
                updated_list.append(data_dict[state][column]) 

'''
                # writer.writerow(row_dict)         example online 
        # you'll want to write the rest of the code here
        # you want to write the header info as the first row 

        # you want to then write each subsequent row of data 
        # the rows will look like this
        # ex: Alabama,0.2,18.32,21.16,2.17,0.05,3.58,1.98,1.45
        # ex: dict = { 
        #       state: {demo: value }... 
        #       }
  


def max_min_mutate(data_dict, col_list):
    # Do not change the code in this function
    '''
    function to mutate the data to simplify sorting

    Parameters
    ----------
    data_dict : dict
        dictionary of data passed in. In this case, it's the 
    col_list : list
        list of columns to mutate to.

    Returns
    -------
    demo_vals: dict
        DESCRIPTION.

    '''
    # Do not change the code in this function
    demo_vals = {}
    
    for demo in col_list:
        demo_vals.setdefault(demo, {})
        
        for state in data_dict:
            demo_vals[demo].setdefault(state, data_dict[state][demo])
        
    return(demo_vals)


def max_min(data_dict):
    '''
    function to find the 5 max and min states & vals for each demographic

    Parameters
    ----------
    data_dict : dict
        the data_dictionary you're passing in. In this case, the mutated dict

    Returns
    -------
    max_min: 
        a triple nested dict with the this basic format
        {"max":{demographic:{"state":value}}}
    '''
    max_min = {"max":{},"min":{}}
    
    maximum_demographic = {}   #creating empty dictionary 
    minimum_demographic = {}   #creating empty dictionary

    for ethnicity in data_dict.keys():
        maximum_demographic.setdefault(ethnicity, {})     #passing ethnicities to max dict 
        minimum_demographic.setdefault(ethnicity, {})     #passing ethnicities to min dict

        for group in max_min["max"]:
            maximum_list = sorted(data_dict[group].items(), key = lambda x: x[1], reverse = True)
            five_max = maximum_list[:5]
            maximum = dict(five_max)
        maximum_demographic[group] = maximum

        for group in max_min["min"]:
            minimum = sorted(data_dict[group].items(), key = lambda x: x[1])
            five_min = maximum_list[:5]
            minimum = dict(five_min)
        maximum_demographic[group] = minimum

    max_min = {"max": maximum_demographic, "min":minimum_demographic}



    # fill out the code in between here
    # you'll want to make code to fill the dictionary

    # the second inner layer will look like {"max":{demographic:{}}
    # the innermost layer will look like {demographic:{"state":value}}
    
    # printing and returning the data
    #print(max_min)
    return(max_min)


def nat_pct(data_dict, col_list):
    '''
    EXTRA CREDIT
    function to calculate the percentages for each demographic on natl. level    

    Parameters
    ----------
    data_dict : dict
        the data dictionary you are passing in. Either AP or Census data
    col_list : list
        list of the columns to loop through. helps filter out state totals cols

    Returns
    -------
    data_dict_totals
        dictionary of the national demographic percentages

    '''
    data_dict_totals = {}
    
    # fill out code here
    # you'll want to add the demographics as the outerdict keys
    # then you'll want to cycle through the states in the data dict
    # while you're doing that, you'll be accumulating the totals for each demographic
    # you'll then convert each value to a demographic percentage
    # finally, you'll return the dictionary
    pass                                           
    return(data_dict_totals)
        

def nat_dif(data_dict1, data_dict2):
    '''
    EXTRA CREDIT
    function to calculate the difference on the national level

    Parameters
    ----------
    data_dict1 : dict
        the first data dict you are passing in
    data_dict2 : dict
        the 2nd data dict you are passing in.

    Returns
    nat_dif: dict
        the dictionary consisting of the demographic difference on natl. level
    
    '''
    nat_dif = {}
    
    # fill out code here
    # you'll want to remove the state totals 
    # then you'll want to loop through both dicts and find the differences
    # finally, you'll want to return those differences
     
    return(nat_dif)
             

def main():
    # reading in the data
    ap_data = read_csv("ap_cleaned.csv")
    census_data = read_csv("census_cleaned.csv")
    
    # computing demographic percentages
    ap_pct = pct_calc(ap_data)
    census_pct = pct_calc(census_data)
    
    # computing the difference between test taker and state demographics
    pct_dif_dict = pct_dif(ap_pct, census_pct)
    
    # outputing the csv
    csv_out(pct_dif_dict, "HW5V1.csv")
        
    # creating a list from the keys of inner dict
    col_list = list(pct_dif_dict["Alabama"].keys())
    
    # mutating the data
    mutated = max_min_mutate(pct_dif_dict, col_list)
    
    # finding the max and min vals
    max_min_vals = max_min(mutated)
        
    # extra credit
    # providing a list of col vals to cycle through
    col_list = census_data["Alabama"].keys()
    
    # computing the national percentages
    ap_nat_pct = nat_pct(ap_data, col_list)
    census_nat_pct = nat_pct(census_data, col_list)    
    
    print(ap_nat_pct)
    print(census_nat_pct)
    
    # computing the difference between them
    dif = nat_dif(ap_nat_pct, census_nat_pct)
        
    print("Difference between AP Comp Sci A and national demographics:\n",
          dif)
        
main()


# unit testing
# Don't touch anything below here
class HWTest(unittest.TestCase):
    
    def setUp(self):
        # surpressing output on unit testing
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 
        
        # setting up the data we'll need here
        # basically, redoing all the stuff we did in the main function
        self.ap_data = read_csv("ap_cleaned.csv")
        self.census_data = read_csv("census_cleaned.csv")
        
        self.ap_pct = pct_calc(self.ap_data)
        self.census_pct = pct_calc(self.census_data)
        
        self.pct_dif_dict = pct_dif(self.ap_pct, self.census_pct)
        
        self.col_list = list(self.pct_dif_dict["Alabama"].keys())

        self.mutated = max_min_mutate(self.pct_dif_dict, self.col_list)
        
        self.max_min_val = max_min(self.mutated)
        
        # extra credit
        # providing a list of col vals to cycle through
        self.col_list = self.census_data["Alabama"].keys()
        
        # computing the national percentages
        self.ap_nat_pct = nat_pct(self.ap_data, self.col_list)
        self.census_nat_pct = nat_pct(self.census_data, self.col_list)    
        
        self.dif = nat_dif(self.ap_nat_pct, self.census_nat_pct)
        
    # testing the csv reading func is working properly
    def test_read_csv(self):
         test = read_csv("ap_cleaned.csv")
        
         self.assertEqual(test["Alabama"]["ASIAN"], 61)
         
    # testing the pct_calc function
    def test_pct_calc(self):
        self.assertEqual(pct_calc({"state":{"demo":5,"State Totals":10}}), 
                         {"state":{"demo": 50.0}})

    # second test on the pct_calc function
    # fails because my value is wrong (doh!)
    def test2_pct_calc(self):
        self.assertEqual(
            self.ap_pct["Alabama"]["ASIAN"], 
            19.68)

    # testing the pct_dif function
    def test_pct_dif(self):
        self.assertEqual(
            pct_dif({"state":{"demo":50.0}},{"state":{"demo":50.0}}),
            {'state': {'demo': 0.0}}           
            )
        
    # second test on the pct_dif function
    # needs a valid value though brah
    def test2_pct_dif(self):
        self.assertEqual(
            self.pct_dif_dict["Alabama"]["AMERICAN INDIAN/ALASKA NATIVE"],
            0.2)
    
    # testing the max_min function
    def test_max_min(self):
        self.assertEqual(
            max_min({"demo":{"a":1,"b":2,"c":3,"d":4,"e":5}})
            ,
            {'max': {'demo': {'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1}},
             'min': {'demo': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}}}
            )
        
    # second test on the max_min function
    def test2_max_min(self):
        self.assertEqual(
            self.max_min_val["max"]["BLACK"]["District-of-Columbia"],
            23.92)
    
    # testing the nat_pct extra credit function
    def test_nat_pct(self):
       self.assertEqual(
       nat_pct({"state":{"demo":5,"State Totals":10}},["demo", "State Totals"]),
       {"demo":50.0, "State Totals":10})
        
    # second test for the nat_pct extra credit function
    def test2_nat_pct(self):
        self.assertEqual(
            self.ap_nat_pct["AMERICAN INDIAN/ALASKA NATIVE"], 
            0.29)
    
    # testing the nat_dif extra credit function
    def test_nat_dif(self):
        self.assertEqual(
            nat_dif({"demo":0.53, "State Totals": 1},{"demo":0.5, "State Totals": 1}),
            {"demo":0.03}
            )
     
    # second test for the nat_dif extra credit function
    def test2_nat_dif(self):
        self.assertEqual(
            self.dif["ASIAN"],
            27.93)

if __name__ == '__main__':
    unittest.main(verbosity=2)






        


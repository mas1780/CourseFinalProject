# write your Python code here according to the instructions

## import the csv module
import csv
import re

def get_csv_data(filepath):
    """
    Opens the file at filepath, reads the data using the csv module's DictReader, 
    converts that data to a regular list containing a dictionary for each row of data in the CSV file
    and returns that list.

    :param filepath: The file path of the CSV data file to open
    :returns: A list of dictionaries, where each dictionary represents one row from the file
    """

    userList = [] 

    with open (filepath, 'r') as file: 
        input_file = csv.DictReader(file)
        for rows in input_file: 
            userList.append(rows)
    return(userList)

def remove_rows_with_blank_fields(data):
    """
    Removes any rows with one or more blank fields from the data set.

    :param data: The data, as a list of dictionaries
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    userList = data
    nFile = [] 
    for row in userList: 
        if row["id"] == None or row["handle"] == None or row["first_name"] == None or row["last_name"] == None or row["email"] == None or row["street"] == None or row["city"] == None or row["state"] == None or row["state_animal"] == None or row["real_food_affinity_category_id"] == None or row["luxury_brand_affinity_category_id"] == None or row["tech_gadget_affinity_category_id"] == None or row["travel_affinity_category_id"] == None : 
            continue
        else: 
            nFile.append(row)
    return nFile

def remove_rows_with_state(data, state):
    """
    Removes any rows with the given value in the 'state' field.

    :param data: The data, as a list of dictionaries
    :param state: The state value of interest, e.g 'United Kingdom' 
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    userList = data
    nFile = [] 
    for row in userList: 
        if row["state"] == state:
            continue 
        else: 
            nFile.append(row)
    return nFile
    
def remove_rows_under_affinity_id_level(data, affinity_type, threshold):
    """
    Removes any rows with a value in a given affinity category id field lower than the supplied threshold.

    :param data: The data, as a list of dictionaries
    :param affinity_type: The type of affinity category id of interest...
    :param threshold: The maximum acceptable value for this affinity type... records with lower values will be removed.
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    userList= data 
    nFile = []
    for row in userList: 
        tempINT = row[affinity_type]
        for word in tempINT.split():
            if word.isdigit():
                c = int(word)
        if c< threshold :
            continue
        else: 
            nFile.append(row)
    return nFile


def replace_email_domain(data, old_domain, new_domain):
    """
    Updates any rows where the 'email' ends in the old domain.  Updates to the new domain.

    :param data: The data, as a list of dictionaries
    :param old_domain: The old domain to remove, e.g. '@dmoz.org'
    :param new_domain: The new domain to replace the old_domain with, e.g. '@dmoz.com'
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    userList = data 
    nFile = []
    reqSTR = old_domain
    for row in userList : 
        if reqSTR in row["email"]:
            newSTR = row["email"]
            validSTR = (newSTR.replace("@dmoz.org", "@dmoz.com"))
        
            row["email"] = validSTR
            nFile.append(row)
        else:
            nFile.append(row) 
    return nFile


def save_csv_data(data, filepath):
    """
    Saves the data into the specified file.  Include the field headers as the first row.

    :param data: The data, as a list of dictionaries
    :param filepath: The file path of the CSV data file to save to
    """
    ## place your code here to complete this method according to the instructions above
    headers = ['id', 'handle', 'first_name', 'last_name', 'email', 'street', 'city', 'state', 'state_animal', 'real_food_affinity_category_id', 'luxury_brand_affinity_category_id', 'tech_gadget_affinity_category_id', 'travel_affinity_category_id']

    with open(filepath, 'w', newline='')  as csvfile:
        writer = csv.DictWriter(csvfile, headers)
        writer.writeheader()
        writer.writerows(data)
         
def get_average_affinity_id(data, affinity_type):
    """
    Calculates the average affinity category id of all records in the data set.

    :param data: The data, as a list of dictionaries
    :param affinity_type: The type of affinity category id of interest...
    :returns: The average cost per impression of all records in the data set
    """
    ## place your code here to complete this method according to the instructions above
    userList= data 
    count = 0 
    running_sum = 0
    for row in userList: 
        tempINT = row[affinity_type]
        
        for word in tempINT.split():
            if word.isdigit():
                c = int(word)
        running_sum= running_sum + c 
        count= count+1
    ave_aff = running_sum/count
    return ave_aff



#################################################
## Do not modify the code below this line      ##
## except to comment out any function calls    ##
## that you do not wish to test at the moment  ##
#################################################

def main():
    ## use the functions defined above to complete munging of the data file

    # get the data from the file
    data = get_csv_data('data/users.csv')
    
    # munge it
    data = remove_rows_with_blank_fields(data)
    data = remove_rows_with_state(data, 'United Kingdom')
    data = remove_rows_under_affinity_id_level(data, 'real_food_affinity_category_id', 2)
    data = replace_email_domain(data, '@dmoz.org', '@dmoz.com')


    # dave to the new csv file
    save_csv_data(data, 'data/users_clean.csv')

    # print the average cost per impression from the data in the file
    avg = get_average_affinity_id(data, 'real_food_affinity_category_id')
    print( 'The average affinity id for real food is: {}.'.format(avg) ) # format string nicely

if __name__ == "__main__":
    main()

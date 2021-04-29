# Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
# The ticket number should be generated as airline:src:dest:number
# where :
# 1. Consider AI as the value for airline
# 2. src and dest should be the first three characters of the source and destination cities.
# 3. number should be auto-generated starting from 101
# The program should return the list of ticket numbers of last five passengers.
# Note: If passenger count is less than 5, return the list of all generated ticket numbers.

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list = []
    i = 0
    if no_of_passengers < 5:
        while no_of_passengers != 0:
            ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(101+i))
            i = i+1
            no_of_passengers = no_of_passengers - 1
    else:
        for i in range(5):
            ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100+no_of_passengers))
            i = i+1
            no_of_passengers = no_of_passengers - 1
        ticket_number_list = ticket_number_list[::-1]

    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))

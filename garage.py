# Create a parking garage class

class ParkingGarage():

    """
    Provides a parking ticket and parking space to the user.

    num_tickets_spaces should always be equal, as the number of tickets should 
    always be the same as the number of spaces - expects an integer.
    """

    def __init__(self, num_tickets_spaces):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTicket = {}

        for i in range(1, num_tickets_spaces + 1):
            self.tickets.append('ticket')
            self.parkingSpaces.append('freeSpace')


    def takeTicket(self):
        # decrease the amount of tickets available by 1
        # decrease the amount of parkingSpaces available by 1
        del self.tickets[0]
        del self.parkingSpaces[0]
        self.currentTicket['Paid'] = False        

    def payForParking(self):
        # user input that stores amount in a variable
        # if payment != empty, display message to the user that their ticket has 
        #   been paid and they have 15 minutes to leave
        # this should update currentTicket dictionary key 'paid' to True
        while True:
            amount = input('Enter your payment amount: ')

            if amount != '':
                print('Payment recieved. You have 15 minutes to exit the garage.')
                self.currentTicket['Paid'] = True
                break
            else:
                break

    def leaveGarage(self):
        # if ticket == paid, display "thank you, have a nice day"
        # else display input prompt for payment
        # once paid, display thank you message
        # update parking spaces list + 1
        # update tickets list + 1
        if self.currentTicket['Paid'] == True:
            print('Thank you. Have a nice day.')
        else:
            amount = input('Ticket has not been paid. Please enter your payment amount: ')

            if amount != '':
                print('Payment recieved.')
                self.currentTicket['Paid'] = True
                self.tickets.append('ticket')
                self.parkingSpaces.append('freeSpace')


garage = ParkingGarage(10)

def run():
    while True:
        enter = input('Would you like to enter the Parking Garage? ')

        if enter.lower() == 'yes':
            garage.takeTicket()

            while True:
                leave = input('Would you like to pay for your ticket and leave the Garage? ')

                if leave.lower() == 'yes':
                    garage.payForParking()
                    garage.leaveGarage()
                    break
        else:
            print('Have a nice day.')
            break

run()
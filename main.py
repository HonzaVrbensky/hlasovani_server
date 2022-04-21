radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
my_serial = control.device_serial_number()

name= "vote"
value= 0
list_of_votes= [0,0,0,0]

def voting():
    global list_of_votes
    radio.send_value("vote", 1)
    list_of_votes[0] +=1
    basic.show_string("A")
    print(list_of_votes)
input.on_button_pressed(Button.A, voting)

def voting_B():
    global list_of_votes
    radio.send_value("vote", 2)
    list_of_votes[1] +=1
    basic.show_string("B")
    print(list_of_votes)
input.on_button_pressed(Button.B, voting_B)

def voting_C():
    global list_of_votes
    radio.send_value("vote", 3)
    list_of_votes[2] +=1
    basic.show_string("C")
    print(list_of_votes)
input.on_logo_event(TouchButtonEvent.PRESSED, voting_C)

def voting_D():
    global list_of_votes
    radio.send_value("vote", 4)
    list_of_votes[3] +=1
    basic.show_string("D")
    print(list_of_votes)
input.on_pin_pressed(TouchPin.P2, voting_D)
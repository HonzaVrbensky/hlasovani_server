radio.setGroup(69)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
let my_serial = control.deviceSerialNumber()
let name = "vote"
let value = 0
let list_of_votes = [0, 0, 0, 0]
input.onButtonPressed(Button.A, function voting() {
    
    radio.sendValue("vote", 1)
    list_of_votes[0] += 1
    basic.showString("A")
    console.log(list_of_votes)
})
input.onButtonPressed(Button.B, function voting_B() {
    
    radio.sendValue("vote", 2)
    list_of_votes[1] += 1
    basic.showString("B")
    console.log(list_of_votes)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function voting_C() {
    
    radio.sendValue("vote", 3)
    list_of_votes[2] += 1
    basic.showString("C")
    console.log(list_of_votes)
})
input.onPinPressed(TouchPin.P2, function voting_D() {
    
    radio.sendValue("vote", 4)
    list_of_votes[3] += 1
    basic.showString("D")
    console.log(list_of_votes)
})

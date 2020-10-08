
def short_circuit():
    age = int(input("how old are you?"))
    statement = input("what do you say?")
    if age<16 or "Flaglegroop" >statement:
        print("you are still young enough to be fun")
    else:
        print("you are so old!")


def younger_sibling():
    statement = "Yeet it now"
    what_did_you_say = ""
    number_of_asks = 0
    while what_did_you_say.lower() != statement.lower() and number_of_asks < 10:
        what_did_you_say = input("Say it Jordan and Talia!")
        location = what_did_you_say.find("yeet")
        if location:
            what_did_you_say = what_did_you_say[location:location+11]

        number_of_asks = number_of_asks +1

    if number_of_asks >= 10:
        print("uuugghh you are so boring and don't want to play")
    else:
        print("Horay!! you said it")

#short_circuit()
younger_sibling()
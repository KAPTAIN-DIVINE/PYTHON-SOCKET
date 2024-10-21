First_name = input("Enter your First Name: ")
Second_name = input("Enter your Second Name: ")
weight = float(input("Enter your actual weight: "))
Valid_inputs = ["k(g)", "l(bs)"]
user_input = input("k(g), l(bs)?")
while user_input not in Valid_inputs:
    print("Enter a valid input type")
    user_input = input("k(g) or l(bs)?")
if user_input == "k(g)":
    Calculated_weight = float(weight/2.20462)
else:
    Calculated_weight = float(weight * 2.20462)
    unit = "l(bs)"
print(str("Dear " + First_name + " " + Second_name + ", your calculated weight is " + str(Calculated_weight) + user_input))

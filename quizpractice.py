
num_widgets = 0
while True:
    choice = input("Would you like to buy a widget? (y/n): ")
    if choice.lower() == "y":
        num_widgets += 1
    else:
        break
print("You bought", num_widgets , "widget(s) today.")
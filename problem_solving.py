###You're writing code to control your town's traffic lights.
You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.

Test Case 1
Input
Green
Output
Yellow

Test Case 2
Input
Red
Output
Green


##
color=input("enter the traffic signal light color:")
lst_1=['green','yellow','red']
for i in lst_1:
    if i=='red':
        print("the color of light to:",lst_1[0])
    elif color==i:
        s=lst_1.index(i)+1
        print("the color of light to:",lst_1[s])
        break



##output:
enter the traffic signal light color:green
the color of light to: yellow

================ RESTART: C:/Users/gk22204/Desktop/enumarate.py ================
enter the traffic signal light color:red
the color of light to: green










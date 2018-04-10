#setting the name

playerName = input("whats your name? > ")
print(playerName)

print ("your name is {}.".format(playerName))

stop = input("this word will stop the loop > ")
stop_prompt = "Entering the word * " + stop + " *will stop the game"
y = 1
x = 1
run = True
while run:
    print(x)
    x += y
    
    ans = input(stop_prompt + "\n prompt:" )
    if ans == stop:
        run = False
# if

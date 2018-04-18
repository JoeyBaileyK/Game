#if then game.

beginning = "welcome to the text based adventure. for help, type 'hint/' for clues, type'check/.' type 'start' to begin.\n"
unknown_input = "sorry but this system is too dumb to read your expertly crafted sentence. try being more concise or type hint/."
s = input(beginning)
s = s.strip().lower()
if 'start' in s:
    s = input("a loud sound wakes you up in the middle of the night. it sounds like it came from outside.\n")


    if s.find('outside/'): 
        s = input("you walk to the door to find it locked. you remember you left your key on the night stand.\n")
    elif 'hint' in s:
        s = input("go outside, and be sure to put / after whatever you say.\n")
    elif 'check/' in s:
        s = input("looking outside you see something glowing. better check it out.\n")
    elif 'hint/' in s:
        s = input("go outside, and be sure to put / after whatever you say.\n")
    else:
        s = input(unknown_input +"/n")

print("end of my program")

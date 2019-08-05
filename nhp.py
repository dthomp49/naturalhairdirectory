print ("Welcome to the Natural Hair Directory!")

name = input("What's your name?")
print ("Hello! Nice to meet you,", name)

print ("The purpose of this program is to help you determine the best products for your hair type.")
print ("Natural hair is extremely diverse, so not everyone will have the same needs.  Let's get started!")

hair = input("Now what is your curl type: 2, 3, or 4?")
hair = int(hair)
if hair == 3:
    print ("You might want to try a light moisture milk.")
elif hair > 3:
    print ("You have a tighter curl pattern.  Try some whipped shea butter.")
elif hair < 3:
    print ("Your hair is probably wavy.  Lighter oils would be best for you.")

porosity = input("What is your porosity: low, medium, or high?")
if porosity == "high":
    print ("Try protein to strengthen your strands.")
elif porosity == "low":
    print ("Low porosity needs heat to absorb moisture.")
elif porosity == "medium":
    print ("You won the hair lottery! Alternate between heat and protein regularly.")

print ("Let's figure out what your wash day routine should look like.")

washday = input("What was your curl type?")
washday = int(washday)
if washday == 3:
    print ("Use a wide-toothed comb to detangle your curls on wash day.")
elif hair > 3:
    print ("Use your fingers to detangle on wash day to avoid breakage.  Tighter hair is more fragile than you think.")
elif hair < 3:
    print ("Avoid using heavy products and oils on your fine tresses on wash day.  It may weight your hair down.")

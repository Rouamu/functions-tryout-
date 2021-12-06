fibo_seq = int(input("How many sequences do you want to print? "))

# First two terms  
fibo_1 = 0
fibo_2 = 1
count = 0


if fibo_seq <= 0:
    print("Please enter a number that's not 0. Smh")

elif fibo_seq == 1:
    print("This sequence only goes once.. Here it is I guess -_-.", fibo_seq, ": ")
    print(fibo_1)

else:
    print("The fibonacci sequence of the numbers is:")
    while count < fibo_seq:
        print(fibo_1)
        fibonacci = fibo_1 + fibo_2
        fibo_1 = fibo_2
        fibo_2 = fibonacci
        count += 1
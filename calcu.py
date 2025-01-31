if choice == 'a':
    print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
elif choice == 's':
    print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
elif choice == 'm':
    print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
elif choice == 'd':
    print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
else:
    print("Invalid input")

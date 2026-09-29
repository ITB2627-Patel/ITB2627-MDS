while True:
    user_input = input("Enter a number or code: ")
    if user_input.strip() == "67":
        print("Secret code entered. Exiting loop...")
        break
    print(f"You entered: {user_input}")
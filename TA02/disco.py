# Nightclub Access Verification System

try:
    age = int(input("Please enter your age: "))

    if 18 <= age <= 65:
        print("\n--- Dress Code Requirements ---")
        print("Style required: Ibiza Casual / Chic (e.g., smart summer wear, elegant white attire).")
        print("Not allowed: Athletic wear, flip-flops, or swimwear.")
        
        dress_code_check = input("\nAre you complying with the Ibiza dress code? (yes/no): ").strip().lower()

        if dress_code_check in ["yes", "y"]:
            print("\nAccess granted. Welcome to the venue.")
        else:
            print("\nAccess denied. Please adjust your attire to meet our dress code policy.")

    elif age < 18:
        print("\nAccess denied. You must be at least 18 years old to enter.")
    else:
        print("\nAccess denied. Maximum allowed entry age is 65 years.")

except ValueError:
    print("\nInvalid entry. Please enter a valid numerical age.")
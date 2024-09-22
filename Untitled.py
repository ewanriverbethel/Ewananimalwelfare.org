# Simple donation input and response script in Pyto

def donation_system():
    print("Welcome to Ewan Animal Welfare Donation Page")
    print("Please enter your donation details below:")
    
    # Get user details
    name = input("Enter your name: ")
    amount = input("Enter donation amount (USD): ")
    
    # Simple confirmation message
    print(f"\nThank you, {name}!")
    print(f"Your donation of ${amount} will help us save endangered animals and reverse climate change.")
    
    # Add your logic for payment processing here (you'll need a server or platform like Stripe)
    
    print("\nVisit us again!")
    
# Run the donation system
donation_system()
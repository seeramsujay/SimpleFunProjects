import random

def calculate_love_percentage(name1, name2):
    """
    Calculates a consistent love percentage between two names.
    """
    combined_names = (name1.lower().strip() + name2.lower().strip()).replace(" ", "")
    
    score = 0
    for char in combined_names:
        score += ord(char)
        
    # Use the score to seed the random number generator
    # This ensures the same names always get the same percentage
    random.seed(score)
    percentage = random.randint(1, 100)
    
    return percentage

def main():
    print("-" * 40)
    print("💖 LOVE PERCENTAGE CALCULATOR 💖")
    print("-" * 40)
    
    name1 = input("Enter the first person's name: ")
    name2 = input("Enter the second person's name: ")
    
    if not name1 or not name2:
        print("Please enter valid names!")
        return
        
    score = calculate_love_percentage(name1, name2)
    
    print("\nCalculating...")
    print(f"The Love Percentage between {name1} and {name2} is: {score}%")
    
    if score >= 80:
        print("Status: Wow! A match made in heaven! 💖🌟")
    elif score >= 50:
        print("Status: Looks like there's a strong connection! 💕")
    elif score >= 30:
        print("Status: There is some potential here. 🤞")
    else:
        print("Status: Might be better as friends! 💔")
        
    print("-" * 40)

if __name__ == "__main__":
    main()

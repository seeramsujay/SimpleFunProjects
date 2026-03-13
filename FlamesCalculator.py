def play_flames(name1, name2):
    # Normalize strings (lowercase and remove spaces)
    name1 = list(name1.lower().replace(" ", ""))
    name2 = list(name2.lower().replace(" ", ""))

    # Step 1: Remove common characters
    for char in name1[:]:
        if char in name2:
            name1.remove(char)
            name2.remove(char)

    count = len(name1) + len(name2)
    
    # The FLAMES categories
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Step 2: The elimination process
    while len(flames) > 1:
        # Calculate index to remove using modulo
        # (count - 1) because list indices start at 0
        split_index = (count % len(flames)) - 1
        
        if split_index >= 0:
            # Re-slice the list so the count starts from the next item
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            # If index is -1, it means we remove the last item
            flames.pop()

    return flames[0]

# --- Quick Test ---
p1 = input("Enter Name 1: ")
p2 = input("Enter Name 2: ")
result = play_flames(p1, p2)

print(f"\nRelationship Result: {result}")
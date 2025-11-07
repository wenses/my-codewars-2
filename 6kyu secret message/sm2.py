def find_secret_words(message):
    # Split the message into words
    words = message.split()
    # Keep track of seen words and secret (duplicate) words
    seen = set()
    secret_words = []
    
    # Iterate through words
    for word in words:
        # If word is already seen, it's a duplicate
        if word.lower() in seen:
            # Only add if not already in secret_words
            if word.lower() not in secret_words:
                secret_words.append(word)
        else:
            # Add to seen words
            seen.add(word.lower())
    
    return secret_words

# Example usage
message = "There is a secret message in the first six sentences of this kata description. Have you ever felt like there was something more being said? Was it hard to figure out that unspoken meaning? Never again! Never will a secret go undiscovered. Find all duplicates from our message!"
result = find_secret_words(message)
print(result)  # Output: ['jumps', 'quick']
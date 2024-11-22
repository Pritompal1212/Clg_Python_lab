def greet(name="Guest", greeting="Hello"):
    """
    Greets a user with a specified greeting. Defaults to "Guest" and "Hello".
    """
    print(f"{greeting}, {name}!")

# Example usage
greet()                          # Uses default arguments
greet("Alice")                   # Uses default greeting, custom name
greet("Bob", "Welcome")          # Custom name and custom greeting
greet(greeting="Hi", name="Eve") # Custom greeting and name (keyword arguments)

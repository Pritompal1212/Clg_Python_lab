def is_substring_present(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# Example usage
main_string = "Hello, World!"
substring = "pritom"

if is_substring_present(main_string, substring):
    print(f"'{substring}' is present in '{main_string}'.")
else:
    print(f"'{substring}' is NOT present in '{main_string}'.")

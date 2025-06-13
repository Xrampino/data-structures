# Create a function that reverses a string
# eg: "I love eggs!" -> "!sgge evol I"

def string_reverse(input_string: str) -> str:
    if type(input_string) != str:
        return None

    output = ""
    for i in range(len(input_string)):
        output += input_string[len(input_string)-1-i]
    return output

def string_reverse_slice(input_string: str) -> str:
    return input_string[::-1]

print(string_reverse("I love eggs!"))
print(string_reverse_slice("I love eggs!"))
print(string_reverse(34))
print(string_reverse("A"))
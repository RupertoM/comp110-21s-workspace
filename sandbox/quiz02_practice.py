


def reverse(string:str) -> str:
    reverse_string = ""
    i=0
    while i < len(string):
        reverse_string += string[(len(string) - (i+1))]
        i += 1
    
    return reverse_string

print(reverse("hello"))
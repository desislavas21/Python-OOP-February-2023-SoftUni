# Create a generator function called reverse_text that receives a string and yields
# all string characters on one line in reversed order.
def reverse_text(text: str):
    text = text[::-1]
    for char in text:
        yield char


for char in reverse_text("step"):
    print(char, end='')
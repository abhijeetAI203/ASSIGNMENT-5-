data = input("Enter text to write: ")
with open('output.txt', 'w') as f:
    f.write(data + '\n')

more_data = input("Enter text to append: ")
with open('output.txt', 'a') as f:
    f.write(more_data + '\n')

print("\nFile content of output.txt:")
with open('output.txt') as f:
    print(f.read())
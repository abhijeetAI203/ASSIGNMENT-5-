try:
    with open('sample.txt') as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print("Error: File 'sample.txt' not found")
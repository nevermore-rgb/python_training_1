with open('output/test.txt', 'w') as f:
    while True:
        i = input("Enter")
        if not i == "stop":
            f.write(f"{i}\n") 
        else:
            break
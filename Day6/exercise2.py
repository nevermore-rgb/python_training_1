with open('output/test.txt', 'a') as f:
    while True:
        i = input("Enter")
        if not i == "stop":
            f.write(f"{i}\n") 
        else:
            break

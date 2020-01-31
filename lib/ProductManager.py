
if __name__=="__main__":
    start()

def start(items):
    current_items = items
    exit = False
    while not exit:
        choice = int(input("1 Show items\n2. Add items\n3. Sale items\n4. Show sold items\n0. Exit\n===> "))
        if choice == 1:
            show_items(current_items)
        elif choice == 0:
            exit = True

def show_items(current_items):
    print("Show items")
    print(current_items)
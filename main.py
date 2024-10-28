#Kieran Uptagrafft
#10//28/24
#Recursive is for everything


def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num-1)
    print(f"Returning; num = {num}")
    return





def while_substitute(num):
    count = num + 1
    while count != 1:
        count -= 1
        print(f"Recursing; num = {count}")
    count = num
    print("\nBASE CASE REACHED\n")
    count = 0
    while count != num:
        count += 1
        print(f"Recursing; num = {count}")


def main():
    sample(5)
    print("\nWhile while_substitute\n")
    while_substitute(5)

if __name__ == "__main__":
    main()
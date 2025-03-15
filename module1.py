


def square(num):
    print(num**2)


# If we want to give option to use the module as a script we can write this.
def main():
    for i in range (1,11):
        square(i)


# If we want to keep any code private we can use __name__ == "__main__" while giving access to the module.
if __name__ == "__main__":
    main()
# Main program starts here
def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)


# Write your functions here

if __name__ == "__main__":
    main()

import random
import string
import webbrowser

# Dictionary to store URL mappings
url_database = {}

# Generate unique short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if short_code not in url_database:
            return short_code


# Shorten URL
def shorten_url(long_url):
    short_code = generate_short_code()
    url_database[short_code] = long_url
    return short_code


# Retrieve original URL
def get_original_url(short_code):
    return url_database.get(short_code)


# Display all URLs
def display_urls():
    if not url_database:
        print("\nNo URLs Found!")
        return

    print("\n================ STORED URLS ================")
    print("{:<15} {}".format("SHORT CODE", "ORIGINAL URL"))
    print("-" * 70)

    for code, url in url_database.items():
        print("{:<15} {}".format(code, url))

    print("-" * 70)


# Delete URL
def delete_url(short_code):
    if short_code in url_database:
        del url_database[short_code]
        print("URL Deleted Successfully.")
    else:
        print("Short Code Not Found.")


# Open URL
def open_url(short_code):
    original = get_original_url(short_code)

    if original:
        print("Opening:", original)
        webbrowser.open(original)
    else:
        print("Short Code Not Found.")


# Main Menu
def main():

    while True:

        print("\n===================================")
        print("     PYTHON URL SHORTENER")
        print("===================================")
        print("1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. Display All URLs")
        print("4. Open URL in Browser")
        print("5. Delete URL")
        print("6. Exit")
        print("===================================")

        choice = input("Enter Your Choice: ")

        if choice == "1":

            long_url = input("\nEnter Long URL: ")

            if long_url == "":
                print("URL Cannot Be Empty")
                continue

            short_code = shorten_url(long_url)

            print("\nOriginal URL :", long_url)
            print("Short Code   :", short_code)
            print("Short URL    :", "http://short.ly/" + short_code)

        elif choice == "2":

            code = input("Enter Short Code: ")

            original = get_original_url(code)

            if original:
                print("\nOriginal URL :", original)
            else:
                print("URL Not Found.")

        elif choice == "3":

            display_urls()

        elif choice == "4":

            code = input("Enter Short Code: ")
            open_url(code)

        elif choice == "5":

            code = input("Enter Short Code: ")
            delete_url(code)

        elif choice == "6":

            print("\nThank You!")
            print("Python URL Shortener Closed Successfully.")
            break

        else:

            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()
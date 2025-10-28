def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return wrapper


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

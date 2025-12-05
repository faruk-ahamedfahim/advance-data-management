#This project is by Faruk Ahamed Fahim
#License
#This project is open-source. You are free to modify and distribute it under the terms of your chosen license. But please inform me before modifying or distribute it and you should inform others that this is a open source project of 
#----------------------------
#Name     : Faruk Ahamed Fahim
#From     : Bangladesh
#github   : https://github.com/faruk-ahamedfahim
#facebook : https://www.facebook.com/originalfounderofnosa
#----------------------------
import os
import json

def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def encode_data(text):
    """Encodes the text with a simple Caesar cipher (shift by 3)."""
    return "".join(chr(ord(char) + 3) for char in text)

def decode_data(text):
    """Decodes the text by reversing the Caesar cipher (shift by 3)."""
    return "".join(chr(ord(char) - 3) for char in text)

def get_text_files():
    """Returns a list of text files (excluding 'settings' directory)."""
    return [f for f in os.listdir() if f.endswith(".txt") and not f.startswith("settings/")]

def ensure_settings_folder():
    """Ensures that the settings folder exists."""
    if not os.path.exists("settings"):
        os.makedirs("settings")

def load_settings():
    """Loads user settings from the settings folder, creating defaults if they don't exist."""
    ensure_settings_folder()
    if not os.path.exists("settings/user_settings.json"):
        reset_settings()
    with open("settings/user_settings.json", "r") as f:
        return json.load(f)

def reset_settings():
    """Resets settings to the default values."""
    ensure_settings_folder()
    default_settings = {
        "font": "Default",
        "general_color": "white",
        "secondary_color": "blue",
        "extra_fields": [],
        "encoding": True
    }
    with open("settings/factory_settings.json", "w") as f:
        f.write(encode_data(json.dumps(default_settings)))
    with open("settings/user_settings.json", "w") as f:
        json.dump(default_settings, f, indent=4)

def apply_settings(settings):
    """Applies the settings (e.g., font and color changes)."""
    clear_screen()
    print(f"\033[1;32mSettings Applied\033[0m")

def settings_menu():
    """Menu for changing settings."""
    settings = load_settings()
    while True:
        clear_screen()
        print("\n\033[1;34mSettings Menu\033[0m")
        print("Restart the program for better")
        print("1. Change font (can't usuable)")
        print("2. Manage extra info fields")
        print("3. Toggle encoding (Current: " + ("On" if settings["encoding"] else "Off") + ")")
        print("4. Change colors(can't usuable)")
        print("5. Reset to factory settings")
        print("6. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            fonts = ["Default", "Bold", "Italic", "Monospace", "Serif", "Sans-Serif"]
            print("\nAvailable Fonts:")
            for i, font in enumerate(fonts, start=1):
                print(f"{i}. {font}")
            font_choice = input("Select font by number: ").strip()
            if font_choice.isdigit() and 1 <= int(font_choice) <= len(fonts):
                settings["font"] = fonts[int(font_choice) - 1]
        elif choice == "2":
            print("Current extra fields:", ", ".join(settings["extra_fields"]))
            new_fields = input("Enter extra info fields (comma-separated): ").strip()
            if new_fields:
                settings["extra_fields"] = new_fields.split(",")
        elif choice == "3":
            print("\nToggle Encoding:\n1. On (Default) - Data will be encoded for security.\n2. Off - Data will be stored in plain text.")
            toggle_choice = input("Select option (1 or 2): ").strip()
            settings["encoding"] = toggle_choice == "1"
        elif choice == "4":
            colors = ["White", "Blue", "Green", "Red", "Yellow"]
            print("\n1. General Color")
            print("2. Secondary Color")
            color_choice = input("Select option (1 or 2): ").strip()
            if color_choice in ["1", "2"]:
                print("\nAvailable Colors:")
                for i, color in enumerate(colors, start=1):
                    print(f"{i}. {color}")
                color_pick = input("Select color by number: ").strip()
                if color_pick.isdigit() and 1 <= int(color_pick) <= len(colors):
                    if color_choice == "1":
                        settings["general_color"] = colors[int(color_pick) - 1].lower()
                    else:
                        settings["secondary_color"] = colors[int(color_pick) - 1].lower()
        elif choice == "5":
            reset_settings()
            print("Factory settings restored.")
            return
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
        with open("settings/user_settings.json", "w") as f:
            json.dump(settings, f, indent=4)
        apply_settings(settings)

def save_data(filename, settings):
    """Saves name, score, and extra info into the selected file."""
    with open(filename, "a") as f:
        name = input("Enter name: ")
        score = input("Enter score: ")
        extra_info = ""
        if settings["extra_fields"]:
            for field in settings["extra_fields"]:
                field_value = input(f"Enter value for {field}: ")
                extra_info += f"{field}: {field_value}, "
        data = f"{name}:{score},{extra_info}"
        if settings["encoding"]:
            encoded_data = encode_data(data)
            f.write(encoded_data + "\n")
        else:
            f.write(data + "\n")
    print(f"Data saved to {filename}.")

def search_name(settings):
    """Searches for a name in the saved files and prints matching results."""
    search_term = input("Enter the name to search for: ")
    files = get_text_files()
    found = False
    for filename in files:
        with open(filename, "r") as f:
            data = f.readlines()
            for line in data:
                decoded_line = decode_data(line.strip()) if settings["encoding"] else line.strip()
                if search_term.lower() in decoded_line.lower():
                    print(f"Found '{search_term}' in file {filename}: {decoded_line}")
                    found = True
    if not found:
        print(f"No results found for '{search_term}'.")
    input("Press Enter to continue...")

def overwrite_file(filename, settings):
    """Overwrites the selected file with new data."""
    with open(filename, "w") as f:
        name = input("Enter name: ")
        score = input("Enter score: ")
        extra_info = ""
        if settings["extra_fields"]:
            for field in settings["extra_fields"]:
                field_value = input(f"Enter value for {field}: ")
                extra_info += f"{field}: {field_value}, "
        data = f"{name}:{score},{extra_info}"
        if settings["encoding"]:
            encoded_data = encode_data(data)
            f.write(encoded_data + "\n")
        else:
            f.write(data + "\n")
    print(f"Data overwritten in {filename}.")

def main():
    """Main program that runs the menu and handles user input."""
    settings = load_settings()
    filename = None  # Initialize filename variable
    while True:
        clear_screen()
        print("\n\033[1;36mAdvance Data management(Beta) by Faruk Ahamed Fahim\033[0m")
        print("0. Clear Screen")
        print("1. Create new file")
        print("2. Delete file")
        print("3. Overwrite existing file")
        print("4. Search data by name")
        print("5. Settings")
        print("6. Exit")
        print("This program will update")
        choice = input("\nEnter your choice (0-6): ").strip()

        if choice == "6":
            print("Exiting...")
            break
        elif choice == "5":
            settings_menu()
            settings = load_settings()
            input("Press Enter to continue...")
            continue
        elif choice == "4":
            search_name(settings)
            continue
        elif choice == "2":
            files = get_text_files()
            if not files:
                print("No text files found to delete.")
            else:
                print("Available files:")
                for idx, file in enumerate(files):
                    print(f"{idx + 1}. {file}")
                file_choice = input("Select file to delete by number: ").strip()
                if file_choice.isdigit() and 1 <= int(file_choice) <= len(files):
                    os.remove(files[int(file_choice) - 1])
                    print("File deleted.")
            input("Press Enter to continue...")
            continue
        elif choice == "3":
            files = get_text_files()
            if files:
                print("Available files to overwrite:")
                for idx, file in enumerate(files):
                    print(f"{idx + 1}. {file}")
                file_choice = input("Select file to overwrite by number: ").strip()
                if file_choice.isdigit() and 1 <= int(file_choice) <= len(files):
                    overwrite_file(files[int(file_choice) - 1], settings)
            input("Press Enter to continue...")
            continue
        elif choice == "1":
            filename = input("Enter new file name: ").strip() + ".txt"
            filepath = os.path.join(os.getcwd(), filename)
            open(filename, "w").close()
            print(f"Created file: {filepath}")
            save_data(filename, settings)
            input("Press Enter to continue...")
        elif choice == "0":
            clear_screen()
            input("Press Enter to clear the screen...")

if __name__ == "__main__":
    main()

print ('Thanks for using it anothet pkg is getting ready')
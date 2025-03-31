Title
----------
Advance Data Management by Faruk Ahamed Fahim (Beta edition)

Features
File Management
  - Create new text files
  - Delete existing text files
  - Overwrite existing files with new data
Data Management
  - Save name, score(by default), and additional user-defined fields
  - Search for data by name across multiple text files
Encoding
  - Optional encoding using a Caesar cipher (shift by 3) for simple security
  - Toggle encoding on/off in the settings menu (It will turned on by default)
Customization
  - Choose font and color preferences (limited usability)
  - Manage extra information fields
  - Reset settings to factory defaults
User Interface
  - Terminal-based menu navigation
  - Clear screen functionality for better readability
  
Installation
1. Ensure you have Python installed (Python 3.x recommended)
2. Clone the repository using:
   ‘’’code:sh
   copy it - git clone https://github.com/faruk-ahamedfahim/advance-data-management.git
   ‘’’
3. Navigate to the project directory:
   ‘’’code:sh
   copy it - cd advance-data-management
   ‘’’
4. Run the script using:
   ‘’’code:sh
   copy it - python script.py
   ‘’’

Usage
1. Run the script:  Start the program by executing `python script.py`
2. Navigate the menu: Use the terminal interface to select different options:
   - Create a new file and store data
   - Search for records using a name
   - Modify settings as needed
   - Delete or overwrite existing files
3. Modify settings: Adjust preferences such as encoding, color themes, and extra fields
4. Exit the program: Select the exit option from the main menu

File Structure
- script.py: Main program file that contains the entire logic
- settings/(won’t come by default.Will create automatically): Directory storing configuration files
- user_settings.json: Stores current user preferences
- factory_settings.json: Stores default settings in an encoded format
- txt files: Generated text files for storing user data

Encoding Mechanism
This project uses a simple Caesar cipher with a shift of 3 for encoding text data. When encoding is enabled:
- Each character in the text shifts forward by 3 positions in ASCII
- Decoding reverses this shift to restore the original data
- Users can toggle encoding on/off in the settings menu

Limitations (WILL ADD THESE IN FUTURE UPDATES)
- Font and color selection in the settings menu is non-functional in some environments
- Encoding is basic and should not be relied on for high-security needs
- This is a beta version and may contain bugs

Future Improvements
- Implement a more advanced encryption system
- Improve terminal UI for better navigation
- Expand customization options for fonts and themes
- Add a graphical interface 

License
This project is open-source. You are free to modify and distribute it under the terms of your chosen license. However, please inform me before making any modifications or distributing it. Additionally, you must notify others that this is an open-source project by:
----------------------------
Name     : Faruk Ahamed Fahim
From     : Bangladesh
github   : https://github.com/faruk-ahamedfahim
facebook : https://www.facebook.com/originalfounderofnosa
----------------------------

Disclaimer:
This project will update in future just ask which feature do you want. It is completely free and safe.
This software is in beta and may contain bugs or incomplete features. The changes will be applied to the folder containing the main program. Contributions and feedback are welcome!

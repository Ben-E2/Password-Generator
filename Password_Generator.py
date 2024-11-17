import os #Used for clearing the screen
import sys #Used for exiting the program
import random
from time import sleep

UserDefinedLength = 10
IncludeUppercase = True
IncludeNumbers = True
IncludeSpecialCharacters = True

LowercaseCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UppercaseCharacters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
NumberCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SpecialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", 
                     "{", "}", "|", "\\", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?", "`", "~"]

DefaultMessageDisplayTime = 1.5

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def DisplayMessage(message, displayTime = DefaultMessageDisplayTime):
    ClearScreen()

    print(message)

    sleep(DefaultMessageDisplayTime)

    ClearScreen()

# validRange is (inclusive, exclusive)
def GetValidInput(prompt, useRange = None, upperRange = 1):
    ClearScreen()

    while True:
        try:
            _userInput = int(input(prompt))
            
            if useRange and _userInput not in range(1, upperRange):
                DisplayMessage(f"Input must be between {1} and {upperRange - 1}.")
            else:
                return _userInput

        except ValueError:
            DisplayMessage(f"Your input was invalid.")

def ChangeLengthValue():
    global UserDefinedLength

    ClearScreen()

    _inputPrompt = f"""------------------------------------------------------------------
What do you want the new length to be? (1 - 32)

------------------------------------------------------------------
Type your answer here: """

    _newLength = 0
    while True:
        try:
            
            _newLength = int(input(_inputPrompt))

            if 1 <= _newLength <= 32:
                break
                
            else:
                DisplayMessage("Length is constrained to a minimum of 1 and a maximum of 32.")

        except ValueError:
            DisplayMessage(f"Your input was invalid.")

    UserDefinedLength = _newLength

    DisplayMessage(f"Password length changed to {_newLength}.", 2)

    SetGenerationParameters()

def SetGenerationParameters():
    global IncludeUppercase
    global IncludeNumbers
    global IncludeSpecialCharacters
    global UserDefinedLength

    ClearScreen()

    _inputPrompt = f"""---------------------------------
What would you like to do?
---------------------------------
1 - Toggle uppercase            ({IncludeUppercase} -> {not IncludeUppercase})

2 - Toggle numbers              ({IncludeNumbers} -> {not IncludeNumbers})

3 - Toggle special characters   ({IncludeSpecialCharacters} -> {not IncludeSpecialCharacters})

4 - Change password length      (Currently: {UserDefinedLength})

---------------------------------
5 - Save and go to menu
---------------------------------
Type your answer here: """

    _userChoice = GetValidInput(_inputPrompt, True, 6)       

    if _userChoice == 1:
        IncludeUppercase = not IncludeUppercase
        SetGenerationParameters()

    elif _userChoice == 2:
        IncludeNumbers = not IncludeNumbers
        SetGenerationParameters()

    elif _userChoice == 3:
        IncludeSpecialCharacters = not IncludeSpecialCharacters
        SetGenerationParameters()

    elif _userChoice == 4:
        ChangeLengthValue()

    elif _userChoice == 5:
        DisplayMenu()

    else:
        print(f"Error - input invalid: '{_userChoice}'.")

def DisplayMenu():
    global IncludeUppercase
    global IncludeNumbers
    global IncludeSpecialCharacters
    global UserDefinedLength

    ClearScreen()

    _inputPrompt = f"""---------------------------------
What would you like to do?
---------------------------------
1 - Generate a new password

2 - Change generation settings

3 - Exit program

---------------------------------
Current settings
---------------------------------
Use uppercase letters:      {IncludeUppercase}

Use numbers:                {IncludeNumbers}

Use special characters:     {IncludeSpecialCharacters}

Password length:            {UserDefinedLength}

---------------------------------
Type your answer here: """

    _userChoice = GetValidInput(_inputPrompt, True, 4)

    if _userChoice == 1:
        DisplayPassword(GeneratePassword())

    elif _userChoice == 2:
        SetGenerationParameters()

    elif _userChoice == 3:
        sys.exit(0)

    else:
        print(f"Error - input invalid: '{_userChoice}'.")

def GeneratePassword():
    global IncludeUppercase
    global IncludeNumbers
    global IncludeSpecialCharacters
    global UserDefinedLength

    _generatedPassword = ""
    _activeCharacterTypes = ["lower"]

    if IncludeUppercase:
        _activeCharacterTypes.append("upper")
    if IncludeNumbers:
        _activeCharacterTypes.append("number")
    if IncludeSpecialCharacters:
        _activeCharacterTypes.append("special")

    for i in range(UserDefinedLength):
        if len(_activeCharacterTypes) > 1:
            _randomNumber = random.randint(0,len(_activeCharacterTypes) - 1)
            _chosenCharacterType = _activeCharacterTypes[_randomNumber]

            if _chosenCharacterType == "lower":
                _randomNumber = random.randint(0,len(LowercaseCharacters) - 1)
                _generatedPassword += LowercaseCharacters[_randomNumber]

            elif _chosenCharacterType == "upper":
                _randomNumber = random.randint(0,len(UppercaseCharacters) - 1)
                _generatedPassword += UppercaseCharacters[_randomNumber]

            elif _chosenCharacterType == "number":
                _randomNumber = random.randint(0,len(NumberCharacters) - 1)
                _generatedPassword += NumberCharacters[_randomNumber]
            
            elif _chosenCharacterType == "special":
                _randomNumber = random.randint(0,len(SpecialCharacters) - 1)
                _generatedPassword += SpecialCharacters[_randomNumber]
        else:
            _randomNumber = random.randint(0,len(LowercaseCharacters) - 1)
            _generatedPassword += LowercaseCharacters[_randomNumber]

    return _generatedPassword

def DisplayPassword(password):
    ClearScreen()

    _inputPrompt = f"""---------------------------------------------------------------------------------------------------
This is your generated password. It will be deleted when returning to menu, please copy it.
---------------------------------------------------------------------------------------------------

{password}

---------------------------------------------------------------------------------------------------
1 - Regenerate password

2 - Back to menu

---------------------------------------------------------------------------------------------------
Type your answer here: """

    _userChoice = GetValidInput(_inputPrompt, True, 3)

    if _userChoice == 1:
        DisplayPassword(GeneratePassword())

    elif _userChoice == 2:
        DisplayMenu()

def Main():
    DisplayMenu()

Main()
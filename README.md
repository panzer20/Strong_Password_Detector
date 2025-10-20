Project name: Strong Password Detector

This is a simple Python script that checks whether a given password is strong, based on specific criteria. It was developed as part of my learning journey through the book "Automate the Boring Stuff with Python" (Polish edition, 2017) by Albert Sweigart.

## What It Does

The program prompts the user to enter a password, and then uses regular expressions (`re` module) to evaluate whether the password meets the following strong password criteria:

- Contains at least 8 characters
- Includes at least one lowercase letter
- Includes at least one uppercase letter
- Includes at least one digit

If all conditions are met, the program prints that the password is strong. Otherwise, it notifies the user that the password is not strong enough.

## Example

```
Enter a password: Passw0rd
Password is strong.

Enter a password: weakpass
Password isn't strong.
```

## Technologies Used

- Python 3
- re – Regular Expressions

## What I Learned

- How to use regular expressions to validate string patterns
- How to write simple input/output-based scripts in Python
- How to implement conditional logic based on pattern matching
- Good practices in writing small, single-responsibility functions

## Inspiration

This project is based on an exercise from the book:
"Automate the Boring Stuff with Python" (Polish edition, 2017) by Albert Sweigart  

The purpose of publishing this project is to demonstrate my understanding of regular expressions and basic input validation in Python.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:

```
git clone https://github.com/your-username/strong_password_detector.git
cd strong_password_detector
```

3. Run the script:

```
python3 strong_password_detector.py
```

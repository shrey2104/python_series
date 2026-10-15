"""A beginner-friendly, menu-driven Multi-Utility Toolkit."""
import datetime
import math
import random
import secrets
import string
import time
import uuid
from my_package import file_utils, math_utils


def ask_int(message, minimum=None):
    while True:
        try:
            value = int(input(message))
            if minimum is not None and value < minimum:
                print(f'Please enter a number of at least {minimum}.')
                continue
            return value
        except ValueError:
            print('Please enter a valid whole number.')


def ask_float(message, minimum=None):
    while True:
        try:
            value = float(input(message))
            if not math.isfinite(value):
                raise ValueError
            if minimum is not None and value < minimum:
                print(f'Please enter a number of at least {minimum}.')
                continue
            return value
        except ValueError:
            print('Please enter a valid number.')


def date_time_menu():
    while True:
        print('\n--- Date and Time Operations ---')
        print('1. Current date and time\n2. Difference between dates\n3. Custom date format')
        print('4. Stopwatch\n5. Countdown timer\n6. Back')
        choice = input('Choose: ').strip()
        if choice == '1':
            print('Now:', datetime.datetime.now().strftime('%d %B %Y, %I:%M:%S %p'))
        elif choice == '2':
            try:
                first = datetime.datetime.strptime(input('First date (YYYY-MM-DD): '), '%Y-%m-%d')
                second = datetime.datetime.strptime(input('Second date (YYYY-MM-DD): '), '%Y-%m-%d')
                print('Difference:', abs((second - first).days), 'days')
            except ValueError:
                print('Invalid date. Please use YYYY-MM-DD.')
        elif choice == '3':
            now = datetime.datetime.now()
            print('Day/Month/Year:', now.strftime('%d/%m/%Y'))
            print('Full date:', now.strftime('%A, %d %B %Y'))
            print('Time:', now.strftime('%I:%M %p'))
        elif choice == '4':
            input('Press Enter to start the stopwatch...')
            start = time.perf_counter()
            input('Press Enter to stop...')
            print(f'Elapsed time: {time.perf_counter() - start:.2f} seconds')
        elif choice == '5':
            seconds = ask_int('Countdown seconds (0-60): ', 0)
            if seconds > 60:
                print('Please choose 60 seconds or less for this demo.')
                continue
            for remaining in range(seconds, 0, -1):
                print(remaining, 'seconds remaining')
                time.sleep(1)
            print('Time is up!')
        elif choice == '6':
            return
        else:
            print('Invalid option.')


def math_menu():
    while True:
        print('\n--- Mathematical Operations ---')
        print('1. Arithmetic\n2. Factorial\n3. Trigonometry\n4. Logarithm')
        print('5. Compound interest\n6. Area of shapes\n7. Back')
        choice = input('Choose: ').strip()
        if choice == '1':
            a = ask_float('First number: ')
            b = ask_float('Second number: ')
            print('Addition:', a + b, '| Subtraction:', a - b)
            print('Multiplication:', a * b)
            print('Division:', a / b if b != 0 else 'Not possible (division by zero)')
        elif choice == '2':
            n = ask_int('Enter a non-negative whole number (0-1000): ', 0)
            print('Factorial:', math.factorial(n) if n <= 1000 else 'Please use 1000 or less.')
        elif choice == '3':
            degrees = ask_float('Angle in degrees: ')
            radians = math.radians(degrees)
            print(f'sin = {math.sin(radians):.4f}, cos = {math.cos(radians):.4f}, tan = {math.tan(radians):.4f}')
        elif choice == '4':
            n = ask_float('Positive number: ')
            print('Natural log:', math.log(n), '| Log base 10:', math.log10(n)) if n > 0 else print('Log needs a positive number.')
        elif choice == '5':
            principal = ask_float('Principal amount: ', 0)
            rate = ask_float('Annual interest rate (%): ', 0)
            years = ask_float('Number of years: ', 0)
            amount = math_utils.compound_amount(principal, rate, years)
            print(f'Final amount: {amount:.2f}; Interest earned: {amount - principal:.2f}')
        elif choice == '6':
            print('1. Circle  2. Rectangle  3. Square')
            shape = input('Choose: ').strip()
            if shape == '1':
                print('Area:', round(math_utils.circle_area(ask_float('Radius: ', 0)), 2))
            elif shape == '2':
                length = ask_float('Length: ', 0)
                width = ask_float('Width: ', 0)
                print('Area:', math_utils.rectangle_area(length, width))
            elif shape == '3':
                print('Area:', math_utils.square_area(ask_float('Side: ', 0)))
            else:
                print('Invalid shape.')
        elif choice == '7':
            return
        else:
            print('Invalid option.')


def random_menu():
    while True:
        print('\n--- Random Data Generation ---')
        print('1. Random number\n2. Random list\n3. Password\n4. Sample a dataset')
        print('5. One-time password (OTP)\n6. Dice game\n7. Back')
        choice = input('Choose: ').strip()
        if choice == '1':
            print('Random number:', random.randint(1, 100))
        elif choice == '2':
            print('Random list:', [random.randint(1, 50) for _ in range(5)])
        elif choice == '3':
            length = ask_int('Password length (4-128): ', 4)
            if length > 128:
                print('Please choose 128 or less.')
            else:
                alphabet = string.ascii_letters + string.digits + '!@#$%'
                print('Generated password:', ''.join(secrets.choice(alphabet) for _ in range(length)))
        elif choice == '4':
            data = ['Sales', 'Finance', 'Marketing', 'HR', 'Operations', 'IT']
            print('Sample:', random.sample(data, 3))
        elif choice == '5':
            print('Demo OTP:', ''.join(str(secrets.randbelow(10)) for _ in range(6)))
        elif choice == '6':
            user_roll = random.randint(1, 6)
            computer_roll = random.randint(1, 6)
            print('Your dice:', user_roll, '| Computer dice:', computer_roll)
            print('You win!' if user_roll > computer_roll else 'Computer wins!' if user_roll < computer_roll else 'It is a tie!')
        elif choice == '7':
            return
        else:
            print('Invalid option.')


def file_menu():
    while True:
        print('\n--- File Operations ---')
        print('1. Write (replace) notes\n2. Read notes\n3. Add to notes\n4. Back')
        choice = input('Choose: ').strip()
        if choice == '1':
            path = file_utils.write_text(input('Write a note: '))
            print('Saved to:', path)
        elif choice == '2':
            print(file_utils.read_text())
        elif choice == '3':
            path = file_utils.append_text(input('Add a note: '))
            print('Updated:', path)
        elif choice == '4':
            return
        else:
            print('Invalid option.')


def explore_modules():
    modules = {'datetime': datetime, 'time': time, 'math': math, 'random': random,
               'uuid': uuid, 'file_utils': file_utils, 'math_utils': math_utils}
    print('\nAvailable modules:', ', '.join(modules))
    name = input('Module name: ').strip().lower()
    module = modules.get(name)
    if module is None:
        print('Unknown module.')
    else:
        print('Available attributes:')
        print(', '.join(item for item in dir(module) if not item.startswith('_')))


def main():
    while True:
        print('\n' + '=' * 40)
        print('Welcome to Multi-Utility Toolkit')
        print('=' * 40)
        print('1. Datetime and Time Operations')
        print('2. Mathematical Operations')
        print('3. Random Data Generation')
        print('4. Generate Unique Identifier (UUID)')
        print('5. File Operations (Custom Module)')
        print('6. Explore Module Attributes (dir())')
        print('7. Exit')
        choice = input('Enter your choice (1-7): ').strip()
        if choice == '1':
            date_time_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            print('Your new UUID:', uuid.uuid4())
        elif choice == '5':
            file_menu()
        elif choice == '6':
            explore_modules()
        elif choice == '7':
            print('Thank you for using Multi-Utility Toolkit!')
            break
        else:
            print('Please choose a number from 1 to 7.')


if __name__ == '__main__':
    main()

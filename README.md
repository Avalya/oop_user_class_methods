# User Management System (OOP)

This project implements a user management system using Object-Oriented Programming (OOP) principles. It includes classes for User, UserService, and UserUtil.

## Project Structure
## Classes

### `User`

Represents a user with attributes like user ID, name, email, and birthday.

**Attributes:**

* `user_id` (int): Unique identifier.
* `name` (str): First name.
* `surname` (str): Last name.
* `email` (str): Email address.
* `password` (str): Password.
* `birthday` (datetime): Birthday.

**Methods:**

* `__init__(self, user_id, name, surname, email, password, birthday)`: Initializes a new User object.
* `get_details(self)`: Returns a formatted string with user details.
* `get_age(self)`: Computes and returns the user's age.

### `UserService`

Manages user records.

**Class Attribute:**

* `users` (dict): Dictionary to store User objects.

**Class Methods:**

* `add_user(cls, user)`: Adds a User object to the users dictionary.
* `find_user(cls, user_id)`: Finds a user by user ID.
* `delete_user(cls, user_id)`: Removes a user by user ID.
* `update_user(cls, user_id, user_update)`: Updates user attributes.
* `get_number(cls)`: Returns the number of users.

### `UserUtil`

Provides utility functions for user management.

**Static Methods:**

* `generate_user_id()`: Generates a unique user ID.
* `generate_password()`: Generates a strong password.
* `is_strong_password(password)`: Checks password strength.
* `generate_email(name, surname, domain)`: Generates an email address.
* `validate_email(email)`: Validates an email address.

## How to Run

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd user-management-oop
    ```
2.  **Run Tests:**
    ```bash
    python -m unittest tests/test_user_management.py
    ```

## Sample Runs

Include sample runs (input and output) here. You can either use text examples or screenshots.

## UML Class Diagram

Include a UML class diagram here (e.g., as an image file).

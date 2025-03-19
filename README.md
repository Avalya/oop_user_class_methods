# User Management System

This project implements a user management system using object-oriented principles in Python. It includes classes for managing user data, services for user operations, and utility functions.

## Classes

### User

Represents a user with attributes like `user_id`, `name`, `surname`, `birthday`, `email`, and `password`.

* `__init__(self, user_id, name, surname, birthday)`: Initializes a new user.
* `get_details(self)`: Returns a formatted string with user details.
* `get_age(self)`: Calculates and returns the user's age.

### UserService

Manages a collection of `User` objects.

* `users (class attribute)`: A dictionary storing `User` objects with `user_id` as the key.
* `add_user(cls, user)`: Adds a `User` object to the `users` dictionary.
* `find_user(cls, user_id)`: Retrieves a `User` object by `user_id`.
* `delete_user(cls, user_id)`: Removes a `User` object by `user_id`.
* `update_user(cls, user_id, user_update)`: Updates a `User` object's attributes.
* `get_number(cls)`: Returns the number of users in the system.

### UserUtil

Provides utility functions for user management.

* `generate_user_id()`: Generates a unique 9-digit user ID.
* `generate_password()`: Generates a strong password.
* `is_strong_password(password)`: Checks if a password meets strength requirements.
* `generate_email(name, surname, domain)`: Generates an email address.
* `validate_email(email)`: Validates an email address format.

## UML Class Diagram

```mermaid
classDiagram
    class User{
        - int user_id
        - string name
        - string surname
        - datetime birthday
        - string email
        - string password
        + __init__(int user_id, string name, string surname, datetime birthday)
        + string get_details()
        + int get_age()
    }

    class UserService{
        + dict users
        + add_user(User user)
        + User find_user(int user_id)
        + delete_user(int user_id)
        + update_user(int user_id, User user_update)
        + int get_number()
    }

    class UserUtil{
        + static int generate_user_id()
        + static string generate_password()
        + static bool is_strong_password(string password)
        + static string generate_email(string name, string surname, string domain)
        + static bool validate_email(string email)
    }

    User "1" -- "*" UserService : uses

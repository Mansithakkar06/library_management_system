# library_management_system

This is a simple Library Management System written in Python. The system allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. It is a command-line application that uses a text-based menu for interaction.

## Features

- **Add Books**: Add new books to the library with unique identifiers (ISBN), title, author, and publication year.
- **Borrow Books**: Borrow a book by its isdn if it is available.
- **Return Books**: Return a borrowed book to the library.
- **View Available Books**: List all books that are currently available in the library.

## Requirements

- you must have Python 3.10 installed on your system

## Setup Instructions

1. **Clone the Repository**:

   git clone https://github.com/Mansithakkar06/library_management_system.git

## Run the Application:

- To start the application, run:
  python library.py

## Usage
1. Add a Book:

Choose option 1 from the menu.
Enter the ISBN, title, author, and publication year of the book.

2. Borrow a Book:

Choose option 2 from the menu.
Enter the ISBN of the book you want to borrow.

3.Return a Book:

Choose option 3 from the menu.
Enter the ISBN of the book you want to return.

4. View Available Books:

Choose option 4 from the menu to view a list of all books that are currently available.

5. Exit the Application:

Choose option 5 to exit the application.


## Running the Tests
- To run the test cases for the Library Management System, use the following command:

  python -m unittest test_library.py
  

## Project Structure

- **library.py**: Contains the Library and Book classes that implement the core functionality and main method which contains menu
- **test_library.py**: Contains unit tests for the Library Management System.
- **README.md**: This file.

## if you want to know about the things that are used

## What is unittes?

- unittest is a built-in Python module used for writing and running tests to ensure that your code works as expected. It provides a framework for creating test cases, grouping them into test suites, and running them with a test runner.

- **Key Features**:

1. **Test Cases**: Define individual tests in a class that inherits from unittest.TestCase.
2. **Assertions**: Use methods like assertEqual(), assertTrue(), etc., to check if your code behaves correctly.
3. **Setup and Teardown**: Use setUp() and tearDown() methods to prepare for and clean up after each test.
4. **Running Tests**: Automatically discover and run tests using unittest.main().

-**Benefits**:
1. Automates testing, ensuring code works as expected.
2. Supports Test-Driven Development (TDD).
3. Helps maintain high code quality by catching bugs early.

In short, unittest helps you write automated tests to verify that your Python code is correct and reliable.

## What is TDD?

- Test-Driven Development (TDD) is a software development approach where you write tests for a feature or functionality before writing the actual code. The TDD cycle consists of three steps:

1. **Red**: Write a test for a new feature. Run the test, and it will fail because the feature isn't implemented yet.
2. **Green**: Write the minimal amount of code necessary to make the test pass.
3. **Refactor**: Clean up the code while ensuring that all tests still pass.

**Benefits of TDD:**
1. **Improves Code Quality**: Ensures your code meets requirements and handles edge cases.
2. **Reduces Bugs**: Catches bugs early by testing before coding.
3. **Facilitates Refactoring**: Makes it safe to improve or change code since you have a safety net of tests.
4. **Encourages Simplicity**: Leads to writing only the necessary code to pass the tests.

- In short, TDD helps you build reliable, bug-free software by writing tests first and driving development through testing.
# AirBnB Clone - Command Interpreter

## Description

This project is a command-line interface (CLI) application that serves as the first step in creating a full AirBnB clone. The CLI acts as a console where users can manage various objects (like users, places, amenities, and more) in a persistent storage system.

## Features

* Create new objects (User, State, City, Place, Amenity, Review).
* Display object details using a string representation.
* Update object attributes.
* Delete objects.
* Save and reload all objects to/from a JSON file.

## How to Start the Console

1. Ensure you are in the project directory.
2. Run the console with the following command:

```bash
./console.py
```

## Usage Examples

```bash
(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) destroy User 1234-1234-1234
(hbnb) all User
(hbnb) update User 1234-1234-1234 name "John"
```

## Project Structure

```
alu-AirBnB_clone/
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   └── engine/
│       └── file_storage.py
└── tests/
    └── test_models/
        ├── test_base_model.py
        └── test_engine/
            └── test_file_storage.py
```

## Author

* Atete Mpeta Shina


# Pydantic

## Runtime Checking with pydantic

1. Define modeled classes, reducing the amount of validation logic you need to write, without sacrificing readability
1. Easily parse user-supplied data, providing guarantees about output data structures

## Dynamic Configuration

Build out types describing restaurants. Provide a way for a user to specify restaurants through configuration files. Here is a list of configurable fields (and their constraints) per restaurant:

- Name of the restaurant
    - For legacy reasons, the name must be less than 32 characters long, and only contain letters, numbers, quotation marks, and spaces (no Unicode, sorry).
- Owner's full name
- Address
- List of employees
    - There must be at least one chef and one server
    - Each employee has a name and position (chef, server, host, sous chef, or delivery driver)
    - Each employee either has a mailing address for a check or direct deposit details
- List of dishes
    - Each dish has a name, price, and description. The name is limited to 16 characters, and the description is limited to 80 characters. Optionally, there is a picture (in the form of a filename) with each dish.
    - Each dish must have a unique name
    - There must be at least three dishes on the menu
- Number of seats
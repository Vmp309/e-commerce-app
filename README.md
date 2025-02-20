# E-commerce project

## Project's goal:

The project aims to develop an e-commerce app that allows users to navigate, make orders and track the status of delivery. 


##  Functional requirements

- Main features:
    -   Register users and login
    -   Product listing
    -   Add products to cart
    -   Ordering
    -   Payment and emission of receipts
    -   Store management

- Secondary features:
    -   Password recovery
    -   Product reviews and ratings
    -   Order history

##  Non-Functional Requirements
- System must ensure password hashing
- Time response to requisition can't be bigger than 2 seconds


## Data models

Insert here diagram image

See more about data models and Django apps hierarchy in the documentation/backend folder 

## User flow

- Login and register flow
    
    - User access to register screen
    - Insert user data (name, email, etc.) 
    - Receives an e-mail of confirmation
    - Logs in and is directed to homepage

- Shopping cart flow

    - User adds products to shopping cart
    - User confirms order and choose payment method
    - User receives a confirmation of the order

See more about user flows in the documentation/frontend folder

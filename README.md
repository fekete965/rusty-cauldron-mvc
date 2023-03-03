# Rusty Cauldron (MVC)

#### CS50 final project

##### Description

The project is a multi page application using python with flask. (Libraries list can be found below the description block). The application's theme was insipred by the CS50 course itself. (Harry Potter) This application allows the users to search recipes. You can also register, login and post your own recipe. You are also able to list out your own recipes and modify them.

---

##### The project is using the following technologies and libraries:

- python
- flask
- flask-login
- flask-sqlalchemy
- werkzeug
- dateutil

---

##### Prerequisite:

1. ###### Secret generation

   In order to run the application, you will need to generate a secret key using the following command:\
   `bash python -c 'import secrets; print(secrets.token_hex())'`
   Make sure you save this key somewhere temporarily!

2. ###### Store the secret as an environment variable

   Then you need to assign that value to `RUSTY_CAULDRON_KEY` environment variable:\
   `Linux or Mac`
   Open one of the following files in your `HOME` directory:\
   `~/.bashrc", "~/.bash_profile", "~/.profile", "~/.zshrc"`
   Add the following statement in the end of the file, where `MY_GENERATED_SECRET` is the secret generated in one of the previous steps:\
   `RUSTY_CAULDRON_KEY=MY_GENERATED_SECRET`

3. ###### Database
   ###### Create the database:
   In order to create the database run the following command in the project folder:\
   `bash python ./prepare-database.py`
   ###### Delete the database:
   If you messed up the database, you can always delete it by running following command in the project folder:\
   To remove the database run the following command in the project folder:\
   `bash rm ./prepare-database.py`

---

##### How to run the application

###### Debug Mode:

To run the application in debug, run the following command in the project folder:\
`bash flask --debug run`

###### Live Mode:

To run the application, run the following command in the project folder:\
`bash flask run`

---

##### You can always use any of the following emails and passwords to login an play with the application:

| Email                                | Password       |
| ------------------------------------ | -------------- |
| alastor-moody@owl-postal.co.uk       | `Password123!` |
| albus-dumbledore@owl-postal.co.uk    | `Password123!` |
| argus-filch@owl-postal.co.uk         | `Password123!` |
| bellatrix-lestrange@owl-postal.co.uk | `Password123!` |
| dolores-umbridge@owl-postal.co.uk    | `Password123!` |
| dooby@owl-postal.co.uk               | `Password123!` |
| draco-malfoy@owl-postal.co.uk        | `Password123!` |
| dudley-dursley@owl-postal.co.uk      | `Password123!` |
| fleur-delacour@owl-postal.co.uk      | `Password123!` |
| gellert-grindewald@owl-postal.co.uk  | `Password123!` |
| ginny-weasley@owl-postal.co.uk       | `Password123!` |
| harry-potter@owl-postal.co.uk        | `Password123!` |
| hermione-granger@owl-postal.co.uk    | `Password123!` |
| james-potter@owl-postal.co.uk        | `Password123!` |
| lily-potter@owl-postal.co.uk         | `Password123!` |
| lucius-malfoy@owl-postal.co.uk       | `Password123!` |
| luna-lovegood@owl-postal.co.uk       | `Password123!` |
| minerva-mcgonagall@owl-postal.co.uk  | `Password123!` |
| neville-longbottom@owl-postal.co.uk  | `Password123!` |
| newt-scamander@owl-postal.co.uk      | `Password123!` |
| nymphadora-tonks@owl-postal.co.uk    | `Password123!` |
| peter-pettigrew@owl-postal.co.uk     | `Password123!` |
| rebeus-hagrid@owl-postal.co.uk       | `Password123!` |
| remus-lupin@owl-postal.co.uk         | `Password123!` |
| ron-weasley@owl-postal.co.uk         | `Password123!` |
| severus-snape@owl-postal.co.uk       | `Password123!` |
| sirius-black@owl-postal.co.uk        | `Password123!` |
| tom-riddle@owl-postal.co.uk          | `Password123!` |

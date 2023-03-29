# Rusty Cauldron (MVC)

#### CS50 final project

##### Video Url:

https://www.loom.com/share/2bc603e03dc04ace857fb567ed81daac

##### Description

The project is a multi page application using python with flask. (Libraries list can be found below the description block). The application's theme was inspired by the CS50 course itself. (Harry Potter) This application allows the users to search recipes. You can also register, login and post your own recipe. You are also able to list out your own recipes and modify them.

---

##### The project is using the following technologies and libraries:

- python
- flask
- flask-login
- flask-sqlalchemy
- werkzeug
- dateutil
- datetime

---

##### Folder structure

The project contains the following folder:

- `migrations`: It contains the sql migration files. They are used to prepare then pre-populate the database
- `static`: It contains the static assets for the html files eg.: css, js, images etc...
- `tables`: It contains the table + related class definition
- `templates`: It contains the template files
- `utils`: It contains a shared place for the utility functions related to this project

##### Files in the root folder

The root folder contains the following files:

- `app.py`: This file performs the necessary steps to setup the application
- `constants.py`: This file contains the constant variable
- `login_manager.py`: This file contains the `login_manager` and related decorator and utility function definitions
- `bootstrap_database.py`: This file create and pre-populate the Sqlite database
- `routes.py`: This file contains all of the route definitions
- `recipe_service.py`: This file contains the RecipeService class which is a helper class that can be use to perform recipe related actions
- `users_service.py`: This file contains the UserService class which is a helper class that can be use to perform user related actions

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
   `bash python ./bootstrap_database.py`
   ###### Delete the database:
   If you messed up the database, you can always delete it by running following command in the project folder:\
   To remove the database run the following command in the project folder:\
   `bash rm ./bootstrap_database.py`

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

| Id  | Email                                | Password       | Has Recipes |
| --- | ------------------------------------ | -------------- | ----------- |
| 25  | alastor-moody@owl-postal.co.uk       | `Password123!` | No          |
| 4   | albus-dumbledore@owl-postal.co.uk    | `Password123!` | Yes         |
| 27  | argus-filch@owl-postal.co.uk         | `Password123!` | No          |
| 12  | bellatrix-lestrange@owl-postal.co.uk | `Password123!` | No          |
| 16  | dolores-umbridge@owl-postal.co.uk    | `Password123!` | No          |
| 11  | dooby@owl-postal.co.uk               | `Password123!` | No          |
| 5   | draco-malfoy@owl-postal.co.uk        | `Password123!` | Yes         |
| 23  | dudley-dursley@owl-postal.co.uk      | `Password123!` | No          |
| 26  | fleur-delacour@owl-postal.co.uk      | `Password123!` | No          |
| 17  | gellert-grindewald@owl-postal.co.uk  | `Password123!` | No          |
| 18  | ginny-weasley@owl-postal.co.uk       | `Password123!` | No          |
| 1   | harry-potter@owl-postal.co.uk        | `Password123!` | Yes         |
| 2   | hermione-granger@owl-postal.co.uk    | `Password123!` | Yes         |
| 28  | james-potter@owl-postal.co.uk        | `Password123!` | No          |
| 21  | lily-potter@owl-postal.co.uk         | `Password123!` | No          |
| 22  | lucius-malfoy@owl-postal.co.uk       | `Password123!` | No          |
| 9   | luna-lovegood@owl-postal.co.uk       | `Password123!` | No          |
| 10  | minerva-mcgonagall@owl-postal.co.uk  | `Password123!` | No          |
| 14  | neville-longbottom@owl-postal.co.uk  | `Password123!` | No          |
| 20  | newt-scamander@owl-postal.co.uk      | `Password123!` | No          |
| 24  | nymphadora-tonks@owl-postal.co.uk    | `Password123!` | No          |
| 19  | peter-pettigrew@owl-postal.co.uk     | `Password123!` | No          |
| 7   | rebeus-hagrid@owl-postal.co.uk       | `Password123!` | No          |
| 15  | remus-lupin@owl-postal.co.uk         | `Password123!` | No          |
| 8   | ron-weasley@owl-postal.co.uk         | `Password123!` | No          |
| 6   | severus-snape@owl-postal.co.uk       | `Password123!` | No          |
| 13  | sirius-black@owl-postal.co.uk        | `Password123!` | No          |
| 3   | tom-riddle@owl-postal.co.uk          | `Password123!` | Yes         |

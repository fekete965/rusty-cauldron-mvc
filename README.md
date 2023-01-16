# rusty-cauldron-MVC

CS50 final project

The project is using the following technologies:

- python
- flask
- flask-login
- flask-sqlalchemy

In order to run the application, you will need to generate a secret key using the following command:
`bash python -c 'import secrets; print(secrets.token_hex())'`

Then you can assing that value to `RUSTY_CAULDRON_KEY` environment variable.

To run the application in debug, run the following command:
`bash flask --debug run`

To run the application, run the following command:
`bash flask run`

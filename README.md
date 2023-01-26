# rusty-cauldron-MVC

CS50 final project

The project is using the following technologies:

- python
- flask
- flask-login
- flask-sqlalchemy
- werkzeug

In order to run the application, you will need to generate a secret key using the following command:
`bash python -c 'import secrets; print(secrets.token_hex())'`

Then you can assing that value to `RUSTY_CAULDRON_KEY` environment variable.

To prepase the databse run the following command:
`bash python ./prepare-database.py`

To run the application in debug, run the following command:
`bash flask --debug run`

To run the application, run the following command:
`bash flask run`

The following emails can be used to login with the following password: `Password123!`

alastor-moody@owl-postal.co.uk
albus-dumbledore@owl-postal.co.uk
argus-filch@owl-postal.co.uk
bellatrix-lestrange@owl-postal.co.uk
dolores-umbridge@owl-postal.co.uk
dooby,@owl-postal.co.uk
draco-malfoy@owl-postal.co.uk
dudley-dursley@owl-postal.co.uk
fleur-delacour@owl-postal.co.uk
gellert-grindewald@owl-postal.co.uk
ginny-weasley@owl-postal.co.uk
harry-potter@owl-postal.co.uk
hermione-granger@owl-postal.co.uk
james-potter@owl-postal.co.uk
lily-potter@owl-postal.co.uk
lucius-malfoy@owl-postal.co.uk
luna-lovegood@owl-postal.co.uk
minerva-mcgonagall@owl-postal.co.uk
neville-longbottom@owl-postal.co.uk
newt-scamander@owl-postal.co.uk
nymphadora-tonks@owl-postal.co.uk
peter-pettigrew@owl-postal.co.uk
rebeus-hagrid@owl-postal.co.uk
remus-lupin@owl-postal.co.uk
ron-weasley@owl-postal.co.uk
severus-snape@owl-postal.co.uk
sirius-black@owl-postal.co.uk
tom-riddle@owl-postal.co.uk

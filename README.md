# Kerberos-based Authentication API

This is an authentication API that acts as a service for authenticating users of the pentesting tool I made.   

You can check the code for the pentesting tool project in this [Github Repository](https://github.com/YoussefJJ/pentesting-tool)  

# Prerequisites

Just like the pentesting tool, this API requires an already set Kerberos environment.  

Before running this app you must configure an environment variable ```KRB5_KTNAME``` needed to read the Keytab file.  

You can set the variable using the following command:  

```sh
$ export KRB5_KTNAME=/etc/krb5.keytab
```

You can clone this code using the ```git clone```command:  

```sh
$ git clone https://github.com/YoussefJJ/kerberos-api
```  

Then install the required packages with the the ```pip install``` command:

```sh
$ pip install -r requirements.txt
```

# How to run

You can run the Flask server with the following command:

```sh
$ python app.py
```  
or

```sh
$ flask run
```

# Contirbuting

As I mentioned in the pentesting app description, this project is part of a university project. Pull requests are welcome.  
For major changes, please open an issue first to discuss what you would like to change.

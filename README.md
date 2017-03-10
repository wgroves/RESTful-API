# RESTful-API

Simple API that takes GET and POST requests to add or return parent or children to a database

The application has 3 parts. The sqlalchemy_db file initializes the database and the relational objects for child and parent. The DBController class handles SQL queries, and takes input in order to add or return a parent or child. The app.py file initializes sqlalchemy_db (thereby creating the database) and runs the web server.

Here are the ways to add and request a child or parent
  GET:
    /child/<childid> --> returns a JSON object of the corresponding childid
    
    /parent/<parentid> --> returns a JSON object of the corresponding parent

  POST
    /addParent --> adds a Parent with a JSON request in the form of: {"name": name}
    
    /addChild --> adds a Child with a JSON request in the form of: {"name": name, "p_id": id}

Some potential scalability issues would be adding more fields to the child or parent tables. This would require me to change the DBController code and the app.py code.

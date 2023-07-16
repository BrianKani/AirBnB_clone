# AirBnB Clone

This project is comprised of multiple components that make up the overall application.

To date, we have explored the backend file storage component. Using Python, we have created a file storage engine which allows us to create, handle, store and manipulate data from and for our users. It forms the base for what is still to come. We specify a base model with public attributes and methods which we use in our other classes. We serialize the data and store it in a JSON file, deserializing it from JSON to recreate the instance based on the ID.

Tying it all together we have created a command line interface for testing and debugging that allows us to create, view, update and destroy any points of data.

### Usage:

To use the command interpreter follow the instructions below.

 - Starting the interpreter is as simple as running the file from the directory in which it is stored (or point to the directory in which it is stored).
   	 - `$ ./console.py`
 - There are multiple commands one can use with the interpreter. You can view all of the available commands by using `$ help`. If you need more information about a particular command, you can use `$ help {command}`.
   	 - `create` - Creates a new instance of BaseModel, saves it to the JSON file and prints the id. Example: `$ create BaseModel`
  	 - `show` - Prints the string representation of an instance based on the class name and id. Example: `$ show BaseModel 1234-1234-1234`
  	 - `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). Example: `$ destroy BaseModel 1234-1234-1234`
  	 - `all` - Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or `$ all`
  	 - `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Example: `$ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'`
  	 - 'quit` - Exits the console application when prompted by the user. Example: `$ quit`

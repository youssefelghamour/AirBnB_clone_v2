# AirBnB clone

## Description
This project is an Airbnb clone developed as part of the ALX Software Engineering program as a collaboration between Mahmoud Hammam and Youssef El Ghamour, aiming to replicate the functionality and user experience of the Airbnb platform.

The overall project incorporates Python, Object-Oriented Programming (OOP), SQL, and the SQLAlchemy ORM, integrates a static web page, populates it with data from the database using  Flask, and dynamically generates content displayed on the web page using Jina templates. The project also contains bash and puppet scripts to automate the deployment of static content to the web servers.

## Command Interpreter
The command interpreter allows users to interact with the AirBnB objects by performing various operations, including creating new objects, retrieving objects from files or databases, updating attributes, and more.

## How to start it:
* Clone this repository: `git clone "https://github.com/youssefelghamour/AirBnB_clone_v2.git"`
* Access the AirBnb directory: `cd AirBnB_clone_v2`
* Run hbnb (interactively): `./console` and enter command
* Run hbnb (non-interactively): `echo "<command>" | ./console.py`

### How to use it in:
#### Interactive mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Files and Directories
##### `console.py`
- Entry point for the command interpreter.
- Commands supported include EOF, quit, create, destroy, show, all, and update.

#### `models/`
- Directory containing classes for the project.

  ##### `base_model.py` - The base class for all the models:
  ##### `amenity.py` - Amenity class that inherits from BaseModel.
  ##### `city.py` - City class that inherits from BaseModel.
  ##### `place.py` - Place class that inherits from BaseModel.
  ##### `review.py` - Review class that inherits from BaseModel.
  ##### `state.py` - State class that inherits from BaseModel.
  ##### `user.py` - User class that inherits from BaseModel.

  #### `engine/`
  - Directory containing storage classes for the JSON serialization and deserialization.

    ##### `file_storage.py` - Serializes instances to a JSON file and deserializes JSON file to instances
    ##### `db_storage.py` - Engine for MySQL database: manages sessions, and provides methods for querying, adding, saving, deleting objects, and reloading.

#### `tests/`
- Directory for unit tests.

  ##### `test_models/`
  - Directory containting tests for all the classes/models:

    ##### `test_amenity.py` - unittest for the Amenity class.
    ##### `test_base_model.py` - unittest for the BaseModel class.
    ##### `test_city.py` - unittest for the city class.
    ##### `test_place.py` - unittest for the Place class.
    ##### `test_review.py` - unittest for the Review class.
    ##### `test_state.py` - unittest for the State class.
    ##### `test_user.py` - unittest for the User class.

    #### `test_engine/`
    - Directory containing for the storage class.

      ##### `test_file_storage.py` - unittest for the FileStorage class.

#### `versions`
- Directory containing archived versions of the web_static folder.

##### `0-setup_web_static.sh` - Shell script for setting up the web servers.
##### `1-pack_web_static.py` - Python script for creating a compressed archive of the web_static content.
##### `2-do_deploy_web_static.py` - Python script for deploying the compressed archive to the web servers.
##### `3-deploy_web_static.py` - Fabric script for automating the deployment process.
##### `100-clean_web_static.py` - Fabric script for deleting out-of-date archives.
##### `101-setup_web_static.pp` - Puppet script for configuring Nginx and creating directories and files.
##### `setup_mysql_dev.sql` - SQL script for setting up the development MySQL database.
##### `setup_mysql_test.sql` - SQL script for setting up the test MySQL database.

## Authors
* **Mahmoud Hammam** - [MahmoudHammam0](https://github.com/MahmoudHammam0)
* **Youssef El Ghamour** - [youssefelghamour](https://github.com/youssefelghamour)

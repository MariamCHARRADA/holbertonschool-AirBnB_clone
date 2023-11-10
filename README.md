# [AirBnB_clone](https://via.placeholder.com/10/00b48a?text=+)

<img align="center" src="https://i.ibb.co/d5N85Nh/hbnb.png">

# [AirBnB clone - The console](https://via.placeholder.com/10/00b48a?text=+)

### [description of the project](https://via.placeholder.com/10/00b48a?text=+)
# 

This project is the first step towards building a full web application: the AirBnB clone.
The console or command interpreter
 >create the data model and allows create

 >update 

 >destroy

 >store

 >persist objects to a file (JSON file).

  This console will be a tool to validate this storage engine.


"Structure of the project"

`Storage engine -> Json file.`
`Console -> cmd with python library cmd.Cmd`



# [Prerequisites](https://via.placeholder.com/10/00b48a?text=+)

Python3.4+ has to be installed if you desire to use the console:
```
sudo apt-get install python3
```

# [Installation](https://via.placeholder.com/10/00b48a?text=+)

To have access to the console use the following command:

```
git clone git@github.com:amaalyy/holbertonschool-AirBnB_clone.git; cd AirBnB_clone
```

# [Run](https://via.placeholder.com/10/00b48a?text=+)

If you want to execute the console use:

```
python3 console.py
```
or
```
./console.py
```

# [Testing](https://via.placeholder.com/10/00b48a?text=+)

If you want to personalize the classes and execute unit tests to confirm that your changes haven't modify the functionality use:

```
python3 -m unittest discover tests
```

# [Use](https://via.placeholder.com/10/00b48a?text=+)

## [Available commands](https://via.placeholder.com/10/00b48a?text=+)
|Command| Explanation |
|--|--|
| create | Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`  |
| show | Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234` |
| all | Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` |
| update | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"` |

## [Normal command input](https://via.placeholder.com/10/00b48a?text=+)

|Command| Example|
|--|--|
|create| create [class name] |
|show| show [class name] [id] |
|all| create [class name] [id]|
|update| create [class name] [id] [arg_name] [arg_value]|


## [Alternative command input](https://via.placeholder.com/10/00b48a?text=+)
|Command| Example|
|--|--|
|[class name].all()| User.all() |
|[class name].count()| User.count() |
|[class name].show()| User.show() |
|[class name].destroy()| User.destroy() |
|[class name].update[id], [attribute name], [attribute value].all()| User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John") |
|(class name).update([id], [dictionary representation])| User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89}) |

## [Available classes](https://via.placeholder.com/10/00b48a?text=+)
|Class name| Attributes|
|--|--|
| BaseModel | `id`, `created_at`, `updated_at`  |
| User| `email`, `password`, `first_name`, `last_name` |
| State| `name` `state_id`|
| City| `name`  |
| Amenity | `name` |
| Place | `city_id` `user_id` `name` `description` `number_rooms` `number_bathrooms` `max_guest` `price_by_night` `latitude``longitude` `amenity_ids` |
| Review| `place_id` `user_id` `text` |

* every model inherits attributes from BaseModel

## [How to start it](https://via.placeholder.com/10/00b48a?text=+)

### [Interactive Mode](https://via.placeholder.com/10/00b48a?text=+)
```
$ ./console.py
```

Now you are on interactive mode and you will see the prompt `(hbnb)`
input a command:

```
(hbnb) create User
```
the id of the created model will be visible in the standard output, if you do:

```
(hbnb) show User [id]
```

All the attributes of the created model will be in your screen.

use: 

```
(hbnb) help
```
For a list of usable commands, to exit press Ctrl+D or type the command quit.

### [Non-Interactive Mode](https://via.placeholder.com/10/00b48a?text=+)

The console can also be used in non-interactive mode:

```
$ echo "create User" | ./console.py
$ echo "help" | ./console.py
```

The program will create a file called: `file.json` whenever you create a new model, it'll be store in the top folder.


## [Authors](https://via.placeholder.com/10/00b48a?text=+)

- [@MariamCHARRADA](https://www.github.com/MariamCHARRADA)
- [@amaalyy](https://www.github.com/amaalyy)

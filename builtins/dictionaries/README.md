### Custom Dict
* Inherit from an appropriate abstract base class, such as MutableMapping
* Inherit from the Python built-in dict class directly
* Subclass UserDict from collections

### UserDict isn't the right solution all the time
* If you want to extend the standard dictionary without affecting its core structure, the it's totally okay to inherit from dict.
* If you want to change the core dictionary behavior by overriding its special methods, then UserDict is best alternative.


### Link
- [Custom Python Dictionaries: Inheriting From dict vs UserDict](https://realpython.com/inherit-python-dict/)
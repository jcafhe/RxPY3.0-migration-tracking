
### Now

|*ObservableBase*<br>typing.Observable|*AnonymousObservable*<br>ObservableBase|*BlockingObservable*<br>typing.Observable|*GroupedObservable*<br>ObservableBase|*ConnectableObservable*<br>ObservableBase| 
|---------------  |-------------------  |-------------------  |-----------------  |---------------------  | 
| \_\_await__     |                     |                     |                   |                       | 
| \_\_add__       |                     |                     |                   |                       | 
| \_\_iadd__      |                     |                     |                   |                       | 
| \_\_getitem__   |                     |                     |                   |                       | 
|                 |                     | \_\_iter__          |                   |                       | 
|                 |                     |                     |                   |                       | 
| _subscribe_core | _subscribe_core     |                     | _subscribe_core   | _subscribe_core       | 
| subscribe_      |                     | subscribe_          |                   |                       | 
| subscribe       |                     | subscribe           | subscribe         |                       | 
| pipe            |                     |                     |                   |                       | 
|                 |                     |                     |                   | connect               | 
|                 |                     |                     |                   | auto_connect          | 
|                 |                     |                     |                   |                       | 
|                 |                     | first               |                   |                       | 
|                 |                     | first_or_default    |                   |                       | 
|                 |                     | for_each            |                   |                       | 
|                 |                     | last                |                   |                       | 
|                 |                     | last_or_default     |                   |                       | 
|                 |                     | to_marbles_blocking |                   |                       | 
|                 |                     | to_iterable         |                   |                       | 

### After
- Remove first, firt_or_default, ... from BlockingObservable
- Subclass ObservableBase for BlockingObservable ?
- Create Observable class
- Transfer magic methods from ObservableBase to Observable


| *ObservableBase*<br>typing.Observable|*Observable*<br>ObservableBase|*AnonymousObservable*<br>ObservableBase|*BlockingObservable*<br>ObservableBase|*GroupedObservable*<br>ObservableBase|*ConnectableObservable*<br>ObservableBase| 
|-----------------|-------------|---------------------|--------------------|-------------------|-----------------------|
|                 | \_\_await__ |                     |                    |                   |                       |
|                 | \_\_add__   |                     |                    |                   |                       |
|                 | \_\_iadd__  |                     |                    |                   |                       |
|                 | \_\_getitem__ |                   |                    |                   |                       |
|                 |             |                     | \_\_iter__         |                   |                       |
|                 |             |                     |                    |                   |                       |
| _subscribe_core |             | _subscribe_core     |                    | _subscribe_core   | _subscribe_core       |
| subscribe_      |             |                     | subscribe_         |                   |                       |
| subscribe       |             |                     | subscribe          | subscribe         |                       |
| pipe            |             |                     |                    |                   |                       |
|                 |             |                     |                    |                   | connect               |
|                 |             |                     |                    |                   | auto_connect          |


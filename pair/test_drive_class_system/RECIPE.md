# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Car.                       │
│                            │
│ - TyreFL                   │
│ - TyreFR                   │
│ - TyreRL                   │
│ - TyreRR                   │
│ + ViewCar()                |
└───────────┬────────────────┘
            │
            │ car has 4x tyres
            ▼
┌────────────────────────────────────────────────────┐
│ Tyre                                               │
│ - [{"date" : x, "pressure" : y, "tread": z}]       │
| + ViewHistory()                                    |
| + Record({"date" : x, "pressure" : y, "tread": z}) |
└────────────────────────────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self, TyreFL, TyreFR, TyreRL, TyreRR):
        self.TyreFL = TyreFL
        self.TyreFR = TyreFR
        self.TyreRL = TyreRL
        self.TyreRR = TyreRR

    def view_tyres(self):
        # Parameters:
        #   none
        # Returns:
        #   Latest item in list of tyre history of all 4 tyres - a dictionary - with an added "position" key-value pair
        # Side-effects:
        #   none
        pass # No code here yet

class Tyre:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, initial_record):
        # Parameters:
        #   initial_record:  a dictionary, which has the date of the record, the pressure and tread of the tyre
        # Side-effects:
        #   Sets the tire's initial information
        pass # No code here yet

    def view_tyre(self):
        # Returns:
        #   all records of the tyre, sorted by date including pressure and tread of the tyre
        pass # No code here yet

    def record(record):
        # Parameters:
        #   record:  a dictionary, which has the date of the record, the pressure and tread of the tyre
        # Side-effects:
        #   Adds onto the tyre's record history list (appends to end of list)
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Can construct car without errors
"""
front_left_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
front_right_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
rear_left_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
rear_right_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})

my_car = Car(front_left_tyre, front_right_tyre, rear_left_tyre, rear_right_tyre)

my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})

my_car.TyreFL.view_tyre()

my_car.view_tyres()
```




## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

front_left_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
front_right_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
rear_left_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
rear_right_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})

my_car = Car(front_left_tyre, front_right_tyre, rear_left_tyre, rear_right_tyre)
"""
Check the car contains all of these tyres
"""
assert my_car.view_tyres() == [
    {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "FL"},
    {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "FR"},
    {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "RL"},
    {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "RR"}
]


"""
Check each tyre on the car can be induividually inspected
"""
assert my_car.TyreFL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]
assert my_car.TyreFR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]
assert my_car.TyreRL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]
assert my_car.TyreRR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]

"""
Record new tyre data for each tyre in the car and check it has updated
"""
my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})
my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})
my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})
my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})

assert my_car.TyreFL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
assert my_car.TyreFR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
assert my_car.TyreRL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
assert my_car.TyreRR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

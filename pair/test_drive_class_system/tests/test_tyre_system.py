import pytest
from lib.tyre_system import *

def test_tyre_system():
    front_left_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
    front_right_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
    rear_left_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})
    rear_right_tyre = Tyre({"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5})

    my_car = Car(front_left_tyre, front_right_tyre, rear_left_tyre, rear_right_tyre)

    assert my_car.view_tyres() == [
        {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "FL"},
        {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "FR"},
        {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "RL"},
        {"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5, "position" : "RR"}
    ]

    assert my_car.TyreFL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]
    assert my_car.TyreFR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]
    assert my_car.TyreRL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]
    assert my_car.TyreRR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}]

    my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})
    my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})
    my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})
    my_car.TyreRL.record({"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1})

    assert my_car.TyreFL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
    assert my_car.TyreFR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
    assert my_car.TyreRL.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
    assert my_car.TyreRR.view_tyre() == [{"date" : "28-07-2007", "pressure" : 24, "tread" : 1.5}, {"date" : "15-03-2014", "pressure" : 3, "tread" : 0.1}]
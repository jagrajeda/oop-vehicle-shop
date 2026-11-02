import pytest
from car_management import CarManager

@pytest.fixture(autouse=True)
def reset_car_class():
    CarManager.total_cars = 0
    CarManager.all_cars = []

def test_car_initialization_and_attributes():
    car = CarManager("Toyota", "Tacoma", 2021, 35000)
    
    assert car._id == 1
    assert car._make == "Toyota"
    assert car._model == "Tacoma"
    assert car._year == 2021
    assert car._mileage == 35000
    assert car._services == []

def test_class_attributes_tracking():
    car1 = CarManager("Ford", "F-150", 2020, 45000)
    car2 = CarManager("Subaru", "Outback", 2022, 18000)

    assert CarManager.total_cars == 2
    assert len(CarManager.all_cars) == 2
    assert car1._id == 1
    assert car2._id == 2
    assert CarManager.all_cars[0] == car1
    assert CarManager.all_cars[1] == car2

def test_add_service():
    car = CarManager("Honda", "Civic", 2019, 50000)
    car.add_service("Oil Change")
    car.add_service("Tire Rotation")

    assert len(car._services) == 2
    assert "Oil Change" in car._services
    assert "Tire Rotation" in car._services

def test_update_mileage_valid():
    car = CarManager("Mazda", "CX-50", 2023, 10000)
    car.update_mileage(12500)

    assert car._mileage == 12500

def test_update_mileage_invalid_does_not_decrease():
    car = CarManager("Mazda", "CX-50", 2023, 10000)
    car.update_mileage(8000)

    assert car._mileage == 10000

def test_get_total_cars_class_method():
    CarManager("Chevy", "Silverado", 2018, 80000)
    CarManager("Dodge", "Ram", 2020, 40000)

    assert CarManager.get_total_cars() == 2

def test_find_car_by_id_class_method():
    car1 = CarManager("Tesla", "Model 3", 2021, 20000)
    car2 = CarManager("Rivian", "R1T", 2023, 15000)

    found = CarManager.find_car_by_id(2)
    assert found == car2

    not_found = CarManager.find_car_by_id(99)
    assert not_found is None
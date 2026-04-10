car = {
    "Brand":"Ford",
    "model":"Mustang",
    "Year":2024
}

print(car["model"])
car["color"] = "Red"

print(car)

car.pop("Year")
print(car)

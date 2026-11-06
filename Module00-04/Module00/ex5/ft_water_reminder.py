def ft_water_reminder() -> None:
    water_days: int = int(input("Days since last watering: "))
    water_days_limit: int = 2
    if water_days > water_days_limit:
        print("Water the plants!")
    else:
        print("Plants are fine")

def ft_plant_age() -> None:
    days: int = int(input("Enter plant age in days: "))
    days_limit: int = 60
    if days > days_limit:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

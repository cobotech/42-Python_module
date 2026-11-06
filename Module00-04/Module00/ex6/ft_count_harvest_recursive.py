def count_day(day: int, last: int) -> None:
    if day > last:
        return
    print("Day", day)
    count_day(day + 1, last)


def ft_count_harvest_recursive() -> None:
    last: int = int(input("Days until harvest: "))
    count_day(1, last)
    print("Harvest time!")

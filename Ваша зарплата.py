def maximum_salary(cards):
    numbers = cards.split()
    numbers.sort(reverse=True)
    salary = ''.join(numbers)
    return salary

cards = input("Cards = ")
numbers = cards.split()

result = maximum_salary(cards)
print("Максимальная зарплата: " + result)

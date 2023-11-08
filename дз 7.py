def safe_calculate(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Помилка обчислення: {str(e)}"
    return wrapper

@safe_calculate
def calculate(expression):
    return eval(expression)

expression = "4 + 2"
result = calculate(expression)
print(result)

expression = "10 / 0"
result = calculate(expression)
print(result)
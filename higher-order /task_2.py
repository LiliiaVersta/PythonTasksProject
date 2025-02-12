make_adder = lambda add_value: lambda x: x + add_value

incrementer = make_adder(1)
print(incrementer(5))  # 6
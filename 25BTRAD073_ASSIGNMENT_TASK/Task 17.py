def convert_celsius_to_fahrenheit(celsius: float) -> float:
  return (celsius * 9 / 5) + 32
c_input = float(input("Enter temperature in Celsius: "))
f_result = convert_celsius_to_fahrenheit(c_input)
print(f"Temperature in Fahrenheit: {f_result:.2f}")

pi_input = input("Enter a value for π: ")

if "/" in pi_input:
    numerator, denominator = pi_input.split("/")
    pi = float(numerator) / float(denominator)
elif "." in pi_input:
    pi = float(pi_input)
else:
    pi = int(pi_input)

relative_error = abs(3.14159 - pi) / 3.14159
percentage = relative_error * 100

print("π can be approximated by " + str(pi) + " with a relative error of " + f"{relative_error:.4f}" +
      ". That is a " + f"{percentage:.2f}" + "% error.")
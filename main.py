#Tyler Ciuca tmc6093@psu.edu
#Dymea Schippers dxs5940@psu.edu
#Chetan Mitra czm5805@psu.edu
#Jian Hong Weng jpw6087@psu.edu


temperature = float(input("Enter temperature:"))
C_F = input("Enter unit in F/f or C/c:")
if C_F == "F" or "f":
  celsius = (temperature-32)*5/9
  print(f"{temperature}° in Fahrenheit is equivalent to {celsius}° Celsius.")
elif C_F == "C" or "c":
  farheinheit = (temperature*(9/5))+32
  print(f"{temperature}° in Celsius is equivalent to {farheinheit}° Fahrenheit.")
else:
  print(f"Invalid unit(bad).")



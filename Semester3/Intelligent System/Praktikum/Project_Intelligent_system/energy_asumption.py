temperature = int(input("Temperature: "))
energy = int(input("Energy Consumtion: "))

if temperature > 29 and energy > 900:
    print("Agent: Turn ON AC LOW")
elif temperature > 28:
    print("Agent: Turn ON AC HIGH")
else:
    print("Agent: AC OFF")
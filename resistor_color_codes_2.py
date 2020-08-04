def encode_resistor_colors(ohms_string):
    value, ohm = ohms_string.split(" ")
    codes = {
        0: "black",
        1: "brown",
        2: "red",
        3: "orange",
        4: "yellow",
        5: "green",
        6: "blue",
        7: "violet",
        8: "gray",
        9: "white"
    }
    if value[len(value)-1]=="k":
        number = int(float(value[:-1])*1000)
    elif value[len(value)-1]=="M":
        number = int(float(value[:-1])*1000000)
    else:
        number = int(float(value))
    return codes[int(str(number)[0])] + " " + codes[int(str(number)[1])] + " " + codes[len(str(number))-2] + " gold"
    




print(encode_resistor_colors("10 ohms"), "brown black black gold")
print(encode_resistor_colors("47 ohms"), "yellow violet black gold")
print(encode_resistor_colors("100 ohms"), "brown black brown gold")
print(encode_resistor_colors("220 ohms"), "red red brown gold")
print(encode_resistor_colors("330 ohms"), "orange orange brown gold")
print(encode_resistor_colors("470 ohms"), "yellow violet brown gold")
print(encode_resistor_colors("680 ohms"), "blue gray brown gold")
print(encode_resistor_colors("1k ohms"), "brown black red gold")
print(encode_resistor_colors("4.7k ohms"), "yellow violet red gold")
print(encode_resistor_colors("10k ohms"), "brown black orange gold")
print(encode_resistor_colors("22k ohms"), "red red orange gold")
print(encode_resistor_colors("47k ohms"), "yellow violet orange gold")
print(encode_resistor_colors("100k ohms"), "brown black yellow gold")
print(encode_resistor_colors("330k ohms"), "orange orange yellow gold")
print(encode_resistor_colors("1M ohms"), "brown black green gold")
print(encode_resistor_colors("2M ohms"), "red black green gold")
# F-string allows you to format selected parts of a string.

# To specify a string as an f-string, put an f in front of the string literal, like this:

value = 12345.6789
neg_value = -12345.6789
char_value = 65  # Unicode character

print(f"{value:<20} :<  Left aligned")
print(f"{value:>20} :>  Right aligned")
print(f"{value:^20} :^  Center aligned")
print(f"{value:=+20} :=  Sign at the left most position")
print(f"{value:+20} :+  Plus sign for positive numbers")
print(f"{neg_value:-20} :-  Minus sign for negative numbers")
print(f"{value: 20} :   Space before positive numbers")
print(f"{value:,} :,  Comma as thousand separator")
print(f"{value:_} :_  Underscore as thousand separator")
print(f"{int(value):b} :b  Binary format")
print(f"{char_value:c} :c  Unicode character")
print(f"{value:.2f} :f  Fixed point number format (2 decimal places)")
print(f"{value:e} :e  Scientific format (lowercase e)")
print(f"{value:E} :E  Scientific format (uppercase E)")
print(f"{value:.2g} :g  General format (2 significant digits)")
print(f"{int(value):x} :x  Hex format (lowercase)")
print(f"{value:%} :%  Percentage format")

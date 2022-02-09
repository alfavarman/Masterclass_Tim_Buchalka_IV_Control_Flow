Extract uppercases
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
##### VER 1
#cap = "".join(i for i in quote if i.isupper())
### Ver 2
# cap = ''
# for i in str(quote):
#     if i.isupper():
#         cap = str(cap + i)
#cap = (quote.isupper())
print(cap)
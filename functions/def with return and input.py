def fishstore(fish_entry, price_entry):
    return fish_entry, price_entry

fish_entry = input('enter fish name: ').title()
price_entry = input('enter the fish price(no symbols): ')

print("Fish Type: ", fish_entry, "costs $", price_entry)

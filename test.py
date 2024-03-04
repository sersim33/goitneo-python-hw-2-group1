def len_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return phone
    else:
        print(f"Your phone number {phone} is not correct")

print(len_phone("78787878"))
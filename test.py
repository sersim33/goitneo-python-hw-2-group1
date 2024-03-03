def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        if len(result) == 12:
            return f'+{result}'
        return f'+38{result}'
    return inner   
    


@format_phone_number
def sanitize_phone_number(phone):
    # if len(phone) == 0:
    #     raise KeyError
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

phones = ['48(050)1233-234', '(050)3451234', '0508889900', '+380501112222  ', '+380501112211   ']
for phone in phones:
    print(sanitize_phone_number(phone))
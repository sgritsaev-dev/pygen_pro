def is_valid(pin):
    x=True
    if len(pin) not in (4,5,6):
        x=False
    for c in pin:
        if not c.isdigit():
            x=False
    return x


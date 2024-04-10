
def hide_card(card):
    x=''
    for c in card:
        if c.isdigit():
            if len(x)<12:
                x+='*'
            elif len(x)>=12:
                x+=c
    return x
card = '905 678123 45612 56'

print(hide_card(card))
def permit(name):
    persona_grata = 'Antonio', 'Bob', 'Yan', 'Dolores'
    if name in persona_grata:
        msg = 'Salvete ' + name + '!'
    else:
        msg = 'I de hic! You have no permission to be here'
    print(msg)

nomine = input('Quid nomen tuum est? ')

permit(nomine)
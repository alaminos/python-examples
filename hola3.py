
def permit(name):
    persona_grata = 'Antonio'
    if name == persona_grata:
        msg = 'Salvete!'
    else:
        msg = 'I de hic! You have no permission to be here'
    print(msg)

nomine = input('Quid nomen tuum est? ')

permit(nomine)
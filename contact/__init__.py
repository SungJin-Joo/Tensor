from contact.model import Contact

if __name__ == "__main__":
    Contact.run()

    pass
    """
    cont = Contact("주성진", "010-2825-1587", "joosj@nsetec.com", "대전광역시")
    print(cont)
    cont.updateName("지윤아")
    print(cont)
    cont.deletePhone("010-9428-8703")
    print(cont)

    name = cont.name

    print('\n이름은 {} 이구만!'.format(name))
    """
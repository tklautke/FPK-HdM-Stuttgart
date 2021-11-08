alter = int(input("Gebe bitte dein Alter an: "))

if alter < 14:
    print("Du darfst noch nicht Mofa fahren")
elif alter >= 14 and alter < 16:
    print("Du darfst Mofa fahren aber nicht Moped!")
elif alter >= 16 and alter < 18:
    print("Du darfst Moped fahren aber nicht Auto!")
elif alter >= 18:
    print("Du darfst endlich Auto fahren!")

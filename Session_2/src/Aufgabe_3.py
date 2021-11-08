programmier_note = int(input("Gebe deine Note ein: "))

if programmier_note <= 0:
    print("Biste dumm? Es gibt keine negativen Noten...")
elif programmier_note == 5:
    print("Der FPK war mega unnötig :(")
elif programmier_note <= 4:
    print("Der FKP hat was gebracht :)")
else:
    print("Bist du dumm? Die Noten gehen nur bis 5....")

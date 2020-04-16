from procedures import *


auth = login_reg_procedure()

init_procedure(auth)

endQ = False

while not endQ:
  inp = input("What do you want to do?\n> ").lower().split(" ")

  if inp[0] == "q":
    endQ = True

  elif inp[0] in ["n", "north"]:
      move_procedure(auth, 'n')

  elif inp[0] in ["s", "south"]:
      move_procedure(auth, 's')

  elif inp[0] in ["e", "east"]:
      move_procedure(auth, 'e')

  elif inp[0] in ["w", "west"]:
      move_procedure(auth, 'w')

  # elif inp[0] in ["i", "inv", "inventory"]:
    # pass

  # elif inp[0] in ["l", "look"]:
    # pass

  # elif inp[0] in ["d", "drop"]:
    # pass

  # elif inp[0] in ["g", "get"]:
    # pass

  # elif inp[0] in ["debug"]:
    # pass
  print("\n")


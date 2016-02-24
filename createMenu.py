  def CreateMenu(listOfChoices):
        menu = "\n\n"
        count = 1

        for i in listOfChoices:
               option = str(count) + ")" + i + "\n"
               menu += option
               count = count + 1
        return menu
print("Main Menu:")
mainMenuStr = CreateMenu(
        ["Checking","Savings","Exit"])
print(mainMenuStr)
subMenuStr = CreateMenu(
        ["Deposit","WithDraw","Return to Main Menus"])
saveMenuStr = CreateMenu(
        ["Print Balance","Calculate Intrest","Close Savings Account",\
         "Return to Main Menue"])
choice = input("enter the number of your choice")

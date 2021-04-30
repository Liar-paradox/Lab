class Restaurant:
    def __init__(self, adress, hours, name):
        self.adress = adress
        self.hours = hours
        self.name = name

    def information(self):
        print("Punkt gastronomiczny {}.".format(self.name))
        print("{}, {}".format(self.adress, self.hours))

    def show_flavours(self):
        pass


class IceCreamStand(Restaurant):
    flavours_scoop = ["Wanilia", "Czekolada", "Pistacja", "Guma Balonowa", "Śmietana"]
    flavours_italiano = ["Śmietana", "Czekolada", "Mix"]
    form = ["Wafelek", "Kubek"]
    size_italiano = ["Duży", "Średni", "Mały"]
    max_scoop = 5

    def __init__(self, adress, hours, name):
        super().__init__(adress, hours, name)

    def show_flavours(self):
        print("Dostępne smaki lodów w gałce to:")
        for x in self.flavours_scoop:
            print("-", x)
        print("Dostępne smaki lodów włoskich to:")
        for x in self.flavours_italiano:
            print("-", x)

    def pick_ice_cream(self, type):  # 0 scoop, 1 italiano
        if type == 0:
            sauce = None
            while True:  # wybor ilosci galek
                try:
                    scoop_count = int(input("Wybierz ilość gałek"))
                    break
                except:
                    print("Podaj całkowitą ilość gałek.")

            while True:  # wybor smaku
                i = 1
                for x in self.flavours_scoop:
                    print("{} - {}".format(i, x))
                    i += 1
                flavour = int(input("Wybierz smak od 1 do 5"))
                if flavour not in [1, 2, 3, 4, 5]:
                    print("Wybierz smak od 1 do 5")
                else:
                    break

            while True:  # wybor opakowania
                container = input("Wybierz wafelek(W), lub kubek.(K)")
                if container == "w" or "W":
                    break
                elif container == "k" or "K":
                    break
                else:
                    print("Wybierz opcję W lub K.")

            if container == "k" or "K":  # wybor polewy
                while True:
                    sauce = input("Czy chcesz polewę? (T-Tak, N-Nie")
                    if sauce == "t" or "T":
                        break
                    elif sauce == "n" or "N":
                        break
                    else:
                        print("Wybierz opcję T lub N.")

            if container == "w" or "W":
                print("Zamawiasz {} gałek loda o smaku {} w wafelku.".format(scoop_count,
                                                                             self.flavours_scoop[flavour - 1]))
            elif container == "k" or "K":
                if sauce == "t" or "T":
                    print("Zamawiasz {} gałek loda o smaku {} w kubeczku, z polewą.".format(scoop_count,self.flavours_scoop[flavour - 1]))


                elif sauce == None:
                    print("Zamawiasz {} gałek loda o smaku {} w kubeczku.".format(scoop_count,self.flavours_scoop[flavour - 1]))

            else:
                print("nie dziala")


class CoffeeShop(Restaurant):
    def __init__(self, adress, hours, name):
        super().__init__(adress, hours, name)


ic1 = IceCreamStand("Partyzantów 12, Wrocław", "12:00-22:00", "Polish Loda")
ic1.show_flavours()
ic1.information()
ic1.pick_ice_cream(0)
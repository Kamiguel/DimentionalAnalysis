# Dimentional analysis

# class definition and main functions
class unit:
    # constructor:
    # __init__: str str str str str str str -> Unit
    # given an amount of strings representing the basic units in the SI returns a Unit with them
    def __init__(self, length="m^0", time="s^0", substanceAmount="mole^0", electricCurrent="A^0", temperature="K^0", luminousIntensity="cd^0", mass="kg^0"):
        self.__length = str(length)
        self.__time = str(time)
        self.__substanceAmount = str(substanceAmount)
        self.__electricCurrent = str(electricCurrent)
        self.__temperature = str(temperature)
        self.__luminousIntensity = str(luminousIntensity)
        self.__mass = str(mass)

    # getlength: none -> str
    # Returns the length units associated with the Unit
    def getlength(self):
        return self.__length

    # gettime: none -> str
    # Returns the time units associated with the Unit
    def gettime(self):
        return self.__time

    # getsubstanceAmount: none -> str
    # Returns the substanceAmount units associated with the Unit
    def getsubstanceAmount(self):
        return self.__substanceAmount

    # getelectricCurrent: none -> str
    # Returns the electricCurrent units associated with the Unit
    def getelectricCurrent(self):
        return self.__electricCurrent

    # gettemperature: none -> str
    # Returns the temperature units associated with the Unit
    def gettemperature(self):
        return self.__temperature

    # getluminousIntensity: none -> str
    # Returns the luminousIntensity units associated with the Unit
    def getluminousIntensity(self):
        return self.__luminousIntensity

    # getmass: none -> str
    # Returns the mass units associated with the Unit
    def getmass(self):
        return self.__mass

    # __product__: Unit -> Unit
    # does a multiplication between two Units
    def __product__(self,unidad):
        largoAux1 = self.__length.split("^")
        largoAux2 = unidad.__length.split("^")
        largo1 = int(largoAux1[1])
        largo2 = int(largoAux2[1])
        largoNew = str(largo1+largo2)
        tiempoAux1 = self.__time.split("^")
        tiempoAux2 = unidad.__time.split("^")
        tiempo1 = int(tiempoAux1[1])
        tiempo2 = int(tiempoAux2[1])
        tiempoNew = str(tiempo1+tiempo2)
        sustanciaAux1 = self.__substanceAmount.split("^")
        sustanciaAux2 = unidad.__substanceAmount.split("^")
        sustancia1 = int(sustanciaAux1[1])
        sustancia2 = int(sustanciaAux2[1])
        sustanciaNew = str(sustancia1+sustancia2)
        corrienteAux1 = self.__electricCurrent.split("^")
        corrienteAux2 = unidad.__electricCurrent.split("^")
        corriente1 = int(corrienteAux1[1])
        corriente2 = int(corrienteAux2[1])
        corrienteNew = str(corriente1+corriente2)
        temperaturaAux1 = self.__temperature.split("^")
        temperaturaAux2 = unidad.__temperature.split("^")
        temperatura1 = int(temperaturaAux1[1])
        temperatura2 = int(temperaturaAux2[1])
        temperaturaNew = str(temperatura1+temperatura2)
        luminosidadAux1 = self.__luminousIntensity.split("^")
        luminosidadAux2 = unidad.__luminousIntensity.split("^")
        luminosidad1 = int(luminosidadAux1[1])
        luminosidad2 = int(luminosidadAux2[1])
        luminosidadNew = str(luminosidad1+luminosidad2)
        masaAux1 = self.__mass.split("^")
        masaAux2 = unidad.__mass.split("^")
        masa1 = int(masaAux1[1])
        masa2 = int(masaAux2[1])
        masaNew = str(masa1+masa2)
        newUnit = Unit("m^"+largoNew,"s^"+tiempoNew,"mole^"+sustanciaNew,"A^"+corrienteNew,"K^"+temperaturaNew,"cd^"+luminosidadNew,"kg^"+masaNew)
        return newUnit

# known units
Meter = Unit("m^1","s^0","mole^0","A^0","K^0","cd^0","kg^0")
Second = Unit("m^0","s^1","mole^0","A^0","K^0","cd^0","kg^0")
Mole = Unit("m^0","s^0","mole^1","A^0","K^0","cd^0","kg^0")
Amper = Unit("m^0","s^0","mole^0","A^1","K^0","cd^0","kg^0")
Kelvin = Unit("m^0","s^0","mole^0","A^0","K^1","cd^0","kg^0")
Candela = Unit("m^0","s^0","mole^0","A^0","K^0","cd^1","kg^0")
Kilogram = Unit("m^0","s^0","mole^0","A^0","K^0","cd^0","kg^1")

# To-do list:
# funcion que permita ajustar magnitud: kg a gr etc
# funcion q convierta a string, simplifique unidades conocidas
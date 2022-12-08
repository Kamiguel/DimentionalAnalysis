# Dimentional analysis

# class definition and main functions
class unit:
    # constructor:
    # __init__: str str str str str str str -> Unit
    # given an amount of strings representing the basic units in the SI returns a Unit with them
    def __init__(self, length=0, time=0, substanceAmount=0, electricCurrent=0, temperature=0, luminousIntensity=0, mass=0):
        self.__length = "m^"+str(length)
        self.__time = "s^"+str(time)
        self.__substanceAmount = "mol^"+str(substanceAmount)
        self.__electricCurrent = "A^"+str(electricCurrent)
        self.__temperature = "K^"+str(temperature)
        self.__luminousIntensity = "cd^"+str(luminousIntensity)
        self.__mass = "kg^"+str(mass)

    # getlength: none -> str
    # Returns the length units associated with the unit
    def getlength(self):
        return self.__length

    # gettime: none -> str
    # Returns the time units associated with the unit
    def gettime(self):
        return self.__time

    # getsubstanceAmount: none -> str
    # Returns the substanceAmount units associated with the unit
    def getsubstanceAmount(self):
        return self.__substanceAmount

    # getelectricCurrent: none -> str
    # Returns the electricCurrent units associated with the unit
    def getelectricCurrent(self):
        return self.__electricCurrent

    # gettemperature: none -> str
    # Returns the temperature units associated with the unit
    def gettemperature(self):
        return self.__temperature

    # getluminousIntensity: none -> str
    # Returns the luminousIntensity units associated with the unit
    def getluminousIntensity(self):
        return self.__luminousIntensity

    # getmass: none -> str
    # Returns the mass units associated with the Unit
    def getmass(self):
        return self.__mass

    # __add__: none -> Unit
    # does a multiplication between two units
    def __add__(self,unidad):
        largoAux1 = self.__length.split("^")
        largoAux2 = unidad.__length.split("^")
        largo1 = int(largoAux1[1])
        largo2 = int(largoAux2[1])
        largoNew = largo1+largo2
        tiempoAux1 = self.__time.split("^")
        tiempoAux2 = unidad.__time.split("^")
        tiempo1 = int(tiempoAux1[1])
        tiempo2 = int(tiempoAux2[1])
        tiempoNew = tiempo1+tiempo2
        sustanciaAux1 = self.__substanceAmount.split("^")
        sustanciaAux2 = unidad.__substanceAmount.split("^")
        sustancia1 = int(sustanciaAux1[1])
        sustancia2 = int(sustanciaAux2[1])
        sustanciaNew = sustancia1+sustancia2
        corrienteAux1 = self.__electricCurrent.split("^")
        corrienteAux2 = unidad.__electricCurrent.split("^")
        corriente1 = int(corrienteAux1[1])
        corriente2 = int(corrienteAux2[1])
        corrienteNew = corriente1+corriente2
        temperaturaAux1 = self.__temperature.split("^")
        temperaturaAux2 = unidad.__temperature.split("^")
        temperatura1 = int(temperaturaAux1[1])
        temperatura2 = int(temperaturaAux2[1])
        temperaturaNew = temperatura1+temperatura2
        luminosidadAux1 = self.__luminousIntensity.split("^")
        luminosidadAux2 = unidad.__luminousIntensity.split("^")
        luminosidad1 = int(luminosidadAux1[1])
        luminosidad2 = int(luminosidadAux2[1])
        luminosidadNew = luminosidad1+luminosidad2
        masaAux1 = self.__mass.split("^")
        masaAux2 = unidad.__mass.split("^")
        masa1 = int(masaAux1[1])
        masa2 = int(masaAux2[1])
        masaNew = masa1+masa2
        newUnit = unit(largoNew,tiempoNew,sustanciaNew,corrienteNew,temperaturaNew,luminosidadNew,masaNew)
        return newUnit

    # __ToVector: none -> list
    # transforms a unit into a vector
    def __ToVector__(self):
        largoAux = self.__length.split("^")
        largo = int(largoAux[1])
        tiempoAux = self.__time.split("^")
        tiempo = int(tiempoAux[1])
        sustanciaAux = self.__substanceAmount.split("^")
        sustancia = int(sustanciaAux[1])
        corrienteAux = self.__electricCurrent.split("^")
        corriente = int(corrienteAux[1])
        temperaturaAux = self.__temperature.split("^")
        temperatura = int(temperaturaAux[1])
        luminosidadAux = self.__luminousIntensity.split("^")
        luminosidad = int(luminosidadAux[1])
        masaAux = self.__mass.split("^")
        masa = int(masaAux[1])
        unidadVector = [largo,tiempo,sustancia,corriente,temperatura,luminosidad,masa]
        return unidadVector

    # __ToString: none -> str
    #def __ToString__(self):
       # unidadVector = self.__ToVector__()
       # unidadString =
       # return
    # una funcion que lo simplifique se necesita antes

# known units
# syntaxis: name = unit(length, time, substanceAmount, electricCurrent, temperature, luminousIntensity,mass)
# syntaxis: name = unit(m, s, mole, A, K, cd, kg)
Meter = unit(1,0,0,0,0,0,0)
Second = unit(0,1,0,0,0,0,0)
Mole = unit(0,0,1,0,0,0,0)
Amper = unit(0,0,0,1,0,0,0)
Kelvin = unit(0,0,0,0,1,0,0)
Candela = unit(0,0,0,0,0,1,0)
Kilogram = unit(0,0,0,0,0,0,1)
# Derived units:
Newton = unit(1,-2,0,0,0,0,1)
Coulomb = unit(0,1,0,1,0,0,0)
Hertz = unit(0,-1,0,0,0,0,0)
Volt = unit(2,-3,0,-1,0,0,1)
Henry = unit(2,-2,0,-2,0,0,1)
Farad = unit(-2,4,0,2,0,0,-1)
Ohm = unit(2,-3,0,-2,0,0,1)
Siemens = unit(-2,3,0,2,0,0,-1)
Weber = unit(2,-2,0,-1,0,0,1)
Tesla = unit(0,-2,0,-1,0,0,1)
Joule = unit(2,-2,0,0,0,0,1)
Watt = unit(2,-3,0,0,0,0,1)
Radian = unit(0,0,0,0,0,0,0)
Steradian = unit(0,0,0,0,0,0,0)
# To-do list:
# funcion que permita ajustar magnitud: kg a gr etc
# funcion q convierta a string, simplifique unidades conocidas
# ver que hacer con las unidades que tienen las misma unidades basicas
# añadir mas derivatives
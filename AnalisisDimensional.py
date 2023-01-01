# Dimentional analysis

# class definition and main functions
class unit:
    # constructor:
    # __init__: str str str str str str str num -> Unit
    # given an amount of strings representing the basic units in the SI returns a Unit with them
    def __init__(self, length=0, time=0, substanceAmount=0, electricCurrent=0, temperature=0, luminousIntensity=0, mass=0, multiplier=1):
        self.__length = "m^"+str(length)
        self.__time = "s^"+str(time)
        self.__substanceAmount = "mol^"+str(substanceAmount)
        self.__electricCurrent = "A^"+str(electricCurrent)
        self.__temperature = "K^"+str(temperature)
        self.__luminousIntensity = "cd^"+str(luminousIntensity)
        self.__mass = "kg^"+str(mass)
        self.__multiplier = multiplier

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

    # getmultiplier: none -> num
    # Returns the multiplier for the unit,
    # for basic SI units is 1 (except for kilogram), for multiples is a 10 power, while for non SI units can be any number
    def getmultiplier(self):
        return self.__multiplier

    # __mul__: none -> Unit
    # does a multiplication between two units
    def __mul__(self,unidad):
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
        multiplier1 = self.__multiplier
        multiplier2 = unidad.__multiplier
        multiplierNew = multiplier1 * multiplier2
        newUnit = unit(largoNew,tiempoNew,sustanciaNew,corrienteNew,temperaturaNew,luminosidadNew,masaNew,multiplierNew)
        return newUnit

    # __truediv__: none -> Unit
    # does a divition between two units
    def __truediv__(self, unidad):
        largoAux1 = self.__length.split("^")
        largoAux2 = unidad.__length.split("^")
        largo1 = int(largoAux1[1])
        largo2 = int(largoAux2[1])
        largoNew = largo1 - largo2
        tiempoAux1 = self.__time.split("^")
        tiempoAux2 = unidad.__time.split("^")
        tiempo1 = int(tiempoAux1[1])
        tiempo2 = int(tiempoAux2[1])
        tiempoNew = tiempo1 - tiempo2
        sustanciaAux1 = self.__substanceAmount.split("^")
        sustanciaAux2 = unidad.__substanceAmount.split("^")
        sustancia1 = int(sustanciaAux1[1])
        sustancia2 = int(sustanciaAux2[1])
        sustanciaNew = sustancia1 - sustancia2
        corrienteAux1 = self.__electricCurrent.split("^")
        corrienteAux2 = unidad.__electricCurrent.split("^")
        corriente1 = int(corrienteAux1[1])
        corriente2 = int(corrienteAux2[1])
        corrienteNew = corriente1 - corriente2
        temperaturaAux1 = self.__temperature.split("^")
        temperaturaAux2 = unidad.__temperature.split("^")
        temperatura1 = int(temperaturaAux1[1])
        temperatura2 = int(temperaturaAux2[1])
        temperaturaNew = temperatura1 - temperatura2
        luminosidadAux1 = self.__luminousIntensity.split("^")
        luminosidadAux2 = unidad.__luminousIntensity.split("^")
        luminosidad1 = int(luminosidadAux1[1])
        luminosidad2 = int(luminosidadAux2[1])
        luminosidadNew = luminosidad1 - luminosidad2
        masaAux1 = self.__mass.split("^")
        masaAux2 = unidad.__mass.split("^")
        masa1 = int(masaAux1[1])
        masa2 = int(masaAux2[1])
        masaNew = masa1 - masa2
        multiplier1 = self.__multiplier
        multiplier2 = unidad.__multiplier
        multiplierNew = multiplier1 / multiplier2
        newUnit = unit(largoNew, tiempoNew, sustanciaNew, corrienteNew, temperaturaNew, luminosidadNew, masaNew, multiplierNew)
        return newUnit

    # __eq__: unit -> bool
    # evaluates if two units are equal
    def __eq__(self, other):
        if not isinstance(other, unit):
            return NotImplemented
        return self.__length == other.__length and self.__time == other.__time and self.__substanceAmount == other.__substanceAmount and \
        self.__electricCurrent == other.__electricCurrent and self.__temperature == other.__temperature and self.__luminousIntensity == other.__luminousIntensity and \
        self.__mass == other.__mass and self.__multiplier == other.__multiplier

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
        multiplier = self.__multiplier
        unidadVector = [largo,tiempo,sustancia,corriente,temperatura,luminosidad,masa, multiplier]
        return unidadVector

    # __ToString: none -> str
    # takes a unit and returns it in a readable form, if the unit is a SI unit returns it instead
    def __str__(self):
        resultado = ""
        largoAux1 = self.__length.split("^")
        largo1 = int(largoAux1[1])
        tiempoAux1 = self.__time.split("^")
        tiempo1 = int(tiempoAux1[1])
        sustanciaAux1 = self.__substanceAmount.split("^")
        sustancia1 = int(sustanciaAux1[1])
        corrienteAux1 = self.__electricCurrent.split("^")
        corriente1 = int(corrienteAux1[1])
        temperaturaAux1 = self.__temperature.split("^")
        temperatura1 = int(temperaturaAux1[1])
        luminosidadAux1 = self.__luminousIntensity.split("^")
        luminosidad1 = int(luminosidadAux1[1])
        masaAux1 = self.__mass.split("^")
        masa1 = int(masaAux1[1])
        if self.__multiplier != 1:
            resultado += str(self.__multiplier)+"("
        if largo1 != 0:
            resultado += self.__length+" "
        if tiempo1 != 0:
            resultado += self.__time+" "
        if sustancia1 != 0:
            resultado += self.__substanceAmount+" "
        if corriente1 != 0:
            resultado += self.__electricCurrent+" "
        if temperatura1 != 0:
            resultado += self.__temperature+" "
        if luminosidad1 != 0:
            resultado += self.__luminousIntensity+" "
        if masa1 != 0:
            resultado += self.__mass
        if self.__multiplier != 1:
            resultado += ")"
        return resultado

# known units
# syntaxis: name = unit(length, time, substanceAmount, electricCurrent, temperature, luminousIntensity,mass, multiplier)
# syntaxis: name = unit(m, s, mole, A, K, cd, kg, multiplier)
Meter = unit(1,0,0,0,0,0,0)
Second = unit(0,1,0,0,0,0,0)
Mole = unit(0,0,1,0,0,0,0)
Amper = unit(0,0,0,1,0,0,0)
Kelvin = unit(0,0,0,0,1,0,0)
Candela = unit(0,0,0,0,0,1,0)
Kilogram = unit(0,0,0,0,0,0,1,10**3)
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
Radian = unit(0,0,0,0,0,0,0) # adimensional (m/m)
Steradian = unit(0,0,0,0,0,0,0) # adimensional (m^2/m^2)
# Pascal =
# as a list:
UnitDatabase =[Meter,Second,Mole,Amper,Kelvin,Kilogram,Newton,Coulomb,Hertz,Volt,Henry,Farad,Ohm,Siemens,Weber, Tesla,Joule,Watt]
# To-do list:
# funcion que permita ajustar magnitud: kg a gr etc
# funcion q simplifique unidades conocidas:
#                  for i in range(len(UnitDatabase)):
#            if self == 2: #self == UnitDatabase[i]:
#                return UnitDatabase[i] # debe ser un str, arreglar (hacer caso a caso)
#            else:
# ver que hacer con las unidades que tienen las misma unidades basicas
# añadir mas derivatives
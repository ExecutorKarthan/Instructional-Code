class Substance:
    def __init__(self, concentration, coefficient, power):
        self.concentration = concentration
        self.coefficient = coefficient
        self.power = power 
             
valueK = int(input("What is your value of K?"))

reactants = []
products = []

reactants_done = False
products_done = False

while(not reactants_done):
    concentration = float(input("What is the concentration of your reactant? If it is not factored in the equalibrium, write a 0"))
    coefficient = float(input("What is the coefficent of your reactant? If it is not factored in the equalibrium, write a 1"))
    reactants.append(Substance(concentration, coefficient, coefficient**coefficient))
    finished = input("Is that all the reactants? Please respond with a Y or a Yes")
    if finished.lower == "yes" or finished.lower == "y":
        reactants_done = True
    
while(not products_done):
    concentration = float(input("What is the concentration of your product? If it is not factored in the equalibrium, write a 0"))
    coefficent = float(input("What is the coefficent of your product? If it is not factored in the equalibrium, write a 1"))
    products.append(Substance(concentration, coefficient, coefficient**coefficient))
    if finished.lower == "yes" or finished.lower == "y":
        product_done = True

def quad_coeff_calc(reactant, products, valueK):
    #concentration then coefficicent
    numerator = Substance(1, 1, 1)
    denominator = Substance(1, 1, 1)
    for product in products:
        if product.concentration > 0:
            numerator.append()
    for value in reactants:
        denominator.append()
        

def quadatric (a, b, c):
    print("Your values are: \n ", "A = ", a, "\n B = ", b, "\n C = ", c)
    negVal = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
    posVal = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    return negVal, posVal

a = float(input("A value is..."))
b = float(input("B value is..."))
c = float(input("C value is..."))
print(quadatric(a, b, c))
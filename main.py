import numpy as np
from mealpy import FloatVar, ABC
import math

# Définir la fonction Rosenbrock
def rosenbrock(solution):
    d = len(solution)
    sum_val = 0
    for i in range(d - 1):  # Parcours de 0 à d-2
        xi = solution[i]
        xnext = solution[i + 1]
        sum_val += 100 * (xnext - xi**2)**2 + (xi - 1)**2
    return sum_val

# Définir la fonction Rastrigin
def rastrigin(solution):
    d = len(solution)
    sum = 0.0
    for s in solution:
        sum += (s * s - 10 * math.cos(2 * math.pi * s))
    return 10 * d + sum

# Définir la fonction Ackley
def ackley(solution):
    a = 20
    b = 0.2
    c = 2 * np.pi

    d = len(solution)
    sum1 = np.sum(solution ** 2)
    sum2 = np.sum(np.cos(c * solution))
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)
    return term1 + term2 + a + np.exp(1)

# Définir la fonction Schwefel
def schwefel(solution):
    d = len(solution)
    sum_value = np.sum(solution * np.sin(np.sqrt(np.abs(solution))))
    return 418.9829 * d - sum_value

# Définition du problème de la fonction Rosenbrock
problem_dict_Rosenbrock = {
    "bounds": FloatVar(lb=(-2.048,) * 30, ub=(2.048,) * 30, name="delta"),
    "minmax": "min",
    "obj_func": rosenbrock
}

# Définition du problème de la fonction Rastrigin
problem_dict_Rastringin = {
    "bounds": FloatVar(lb=(-5.12,) * 30, ub=(5.12,) * 30, name="delta"),
    "minmax": "min",
    "obj_func": rastrigin
}

# Définition du problème de la fonction Ackley
problem_dict_Ackley = {
    "bounds": FloatVar(lb=(-32.768,) * 30, ub=(32.768,) * 30, name="delta"),
    "minmax": "min",
    "obj_func": ackley
}

# Définition du problème de la fonction Schwefel
problem_dict_Schwefel = {
    "bounds": FloatVar(lb=(-500.,) * 30, ub=(500.,) * 30, name="delta"),
    "minmax": "min",
    "obj_func": schwefel
}

# Fichier de sortie pour les moyennes et les ecart type
output_file = "Moyennes_EcartTypesPython.txt"

# Stockage des meilleures fitness pour chaque fonction objectif
best_fitnesses_Rosenbrock = []
best_fitnesses_Rastrigin = []
best_fitnesses_Ackley = []
best_fitnesses_Schwefel = []

#Nombre d'appel (10)
run = 10

# Appel de l'algorithme 10 fois
for i in range(run):
    print(f"Exécution {i + 1}...")

    # n_limits qui prends comme valeur : (10,50,100)
    model = ABC.OriginalABC(epoch=1000, pop_size=30, n_limits=100)

    g_best_Rosenbrock = model.solve(problem_dict_Rosenbrock)
    g_best_Rastringin = model.solve(problem_dict_Rastringin)
    g_best_Ackley = model.solve(problem_dict_Ackley)
    g_best_Schwefel = model.solve(problem_dict_Schwefel)

    best_fitnesses_Rosenbrock.append(g_best_Rosenbrock.target.fitness)
    best_fitnesses_Rastrigin.append(g_best_Rastringin.target.fitness)
    best_fitnesses_Ackley.append(g_best_Ackley.target.fitness)
    best_fitnesses_Schwefel.append(g_best_Schwefel.target.fitness)

# Moyenne et écart-type avec numpy
moyenne_Rosenbrock = np.mean(best_fitnesses_Rosenbrock)
moyenne_Rastrigin = np.mean(best_fitnesses_Rastrigin)
moyenne_Ackley = np.mean(best_fitnesses_Ackley)
moyenne_Schwefel = np.mean(best_fitnesses_Schwefel)

ecart_ype_Rosenbrock = np.std(best_fitnesses_Rosenbrock)
ecart_ype_Rastringin = np.std(best_fitnesses_Rastrigin)
ecart_ype_Ackley = np.std(best_fitnesses_Ackley)
ecart_ype_Schwefel = np.std(best_fitnesses_Schwefel)

# Sauvegarde des moyennes et écarts types dans un fichier texte
with open(output_file, mode="w") as file:
    file.write(f"Rosenbrock\n")
    file.write(f"Moyenne : {moyenne_Rosenbrock}\n")
    file.write(f"Ecart type : {ecart_ype_Rosenbrock}\n")

    file.write(f"Rastrigin\n")
    file.write(f"Moyenne :{moyenne_Rastrigin}\n")
    file.write(f"Ecart type :{ecart_ype_Rastringin}\n")

    file.write(f"Ackley\n")
    file.write(f"Moyenne :{moyenne_Ackley}\n")
    file.write(f"Ecart type :{ecart_ype_Ackley}\n")

    file.write(f"Schwefel\n")
    file.write(f"Moyenne :{moyenne_Schwefel}\n")
    file.write(f"Ecart type :{ecart_ype_Schwefel}\n")

print(f"Les moyennes et les écarts types ont été stockés dans le fichier {output_file}")


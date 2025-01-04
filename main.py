import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv("data.csv")

# Liste des fonctions objectives
functions = data["Function_objective"].unique()

# Générer un graphique pour chaque fonction
for function in functions:
    plt.figure(figsize=(10, 6))

    # Filtrer les données pour la fonction actuelle
    function_data = data[data["Function_objective"] == function]

    # Générer des barres pour chaque implementation (C++ et Python)
    for implementation in ["C++", "Python"]:
        impl_data = function_data[function_data["Implementation"] == implementation]
        plt.bar(
            impl_data["n_limits"].astype(str) + f" ({implementation})",
            impl_data["Std"],
            label=f"{implementation}"
        )

    # Ajouter des détails au graphique
    plt.title(f"Comparaison des écarts-types pour la fonction {function}")
    plt.xlabel("n_limits (Implementation)")
    plt.ylabel("Écart-type")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Enregistrer le graphique ou l'afficher
    plt.tight_layout()
    plt.savefig(f"graph_{function}.png")
    plt.show()

#!/usr/bin/env python3
"""
Simple Python program to sum values.
"""

def sum_values(numbers):
    """
    Calcule la somme d'une liste de valeurs numériques.
    """
    if not numbers:
        return 0.0
    return sum(float(x) for x in numbers)


def main():
    print("=== Simple Sum Calculator ===")
    
    # Exemple
    example_list = [1, 2.5, 3, 4.75, 10]
    result = sum_values(example_list)
    print(f"Somme de {example_list} = {result}")
    
    # Mode interactif
    try:
        user_input = input("\nEntrez des nombres séparés par des espaces : ").strip()
        if user_input:
            numbers = [float(x) for x in user_input.split()]
            result = sum_values(numbers)
            print(f"Somme = {result}")
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")


if __name__ == "__main__":
    main()

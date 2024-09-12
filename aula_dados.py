import random

def roll_dice(num_dice, num_sides):
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results

def main():
    print("Bem-vindo ao simulador de dados!")
    
    while True:
        try:
            num_dice = int(input("Digite o número de dados que você deseja rolar: "))
            num_sides = int(input("Digite o número de lados em cada dado: "))
            
            if num_dice <= 0 or num_sides <= 0:
                print("O número de dados e o número de lados devem ser maiores que 0.")
                continue

            results = roll_dice(num_dice, num_sides)
            print(f"Resultados dos {num_dice} dados de {num_sides} lados: {results}")
            print(f"Soma dos resultados: {sum(results)}")
            
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")
        
        next_simulation = input("Você quer simular novamente? (sim/não): ")
        if next_simulation.lower() != 'sim':
            break

if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt

#Exercitiul 2
#X = 5
#Y = 9

def plot_data(data, X, Y):
    #Primul grafic
    plt.figure(figsize=(16, 9))

    plt.title('Graficul 1 - graficul pulsului, pulsului maxim si caloriilor pe baza duratei')    
    plt.plot(data.index, data['Durata'], label='Durata', marker='o', color = 'pink')    
    plt.plot(data.index, data['Puls'], label='Puls', marker='o', color = 'red')
    plt.plot(data.index, data['MaxPuls'], label='Puls maxim', marker='o', color = 'blue')
    plt.plot(data.index, data['Calorii'], label='Calorii', marker='o', color = 'yellow')

    plt.legend()
    plt.show()

    #Al doilea grafic grafic
    plt.figure(figsize=(16, 9))
    plt.title(f'Graficul 2 - graficul pulsului, pulsului maxim si caloriilor pe baza duratei - primele {X} valori')    

    plt.plot(data.index[:X], data['Durata'][:X], label='Durata', marker='o', color = 'green')    
    plt.plot(data.index[:X], data['Puls'][:X], label='Puls', marker='o', color = 'red')
    plt.plot(data.index[:X], data['MaxPuls'][:X], label='Puls maxim', marker='o', color = 'blue')
    plt.plot(data.index[:X], data['Calorii'][:X], label='Calorii', marker='o', color = 'yellow')

    plt.legend()
    plt.show()

    #Al treilea grafic
    plt.figure(figsize=(16, 9))
    plt.title(f'Graficul 3 - graficul pulsului, pe baza duratei - ultimele {Y} valori')

    plt.plot(data.index[-Y:], data['Durata'].tail(Y), label='Durata', marker='o', color = 'green')    
    plt.plot(data.index[-Y:], data['Puls'].tail(Y), label='Puls', marker='o', color = 'red')

    plt.legend()
    plt.show()

def main():
    data = pd.read_csv("data.csv")
    plot_data(data, 5, 9)

if __name__ == "__main__":
    main()
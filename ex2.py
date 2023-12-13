import pandas as pd
import matplotlib.pyplot as plt

#Exercitiul 2
#X = 5
#Y = 9

def plot_data(data, X, Y):
    #Primul grafic
    plt.figure(figsize=(16, 9))
    
    plt.plot(data.index, data['Durata'], label='Durata', marker='*', color = 'green')    
    plt.plot(data.index, data['Puls'], label='Puls', marker='*', color = 'red')
    plt.plot(data.index, data['MaxPuls'], label='Puls maxim', marker='*', color = 'blue')
    plt.plot(data.index, data['Calorii'], label='Calorii', marker='*', color = 'yellow')

    plt.title('Graficul 1 - graficul pulsului, pulsului maxim si caloriilor pe baza duratei')
    plt.legend()
    plt.show()

    #Al doilea grafic grafic
    plt.figure(figsize=(16, 9))
    
    plt.plot(data.index[:X], data['Durata'][:X], label='Durata', marker='*', color = 'green')    
    plt.plot(data.index[:X], data['Puls'][:X], label='Puls', marker='*', color = 'red')
    plt.plot(data.index[:X], data['MaxPuls'][:X], label='Puls maxim', marker='*', color = 'blue')
    plt.plot(data.index[:X], data['Calorii'][:X], label='Calorii', marker='*', color = 'yellow')

    plt.title(f'Graficul 2 - graficul pulsului, pulsului maxim si caloriilor pe baza duratei - primele {X} valori')
    plt.legend()
    plt.show()

    #Al treilea grafic
    plt.figure(figsize=(16, 9))
    
    plt.plot(data.index[-Y:], data['Durata'].tail(Y), label='Durata', marker='*', color = 'green')    
    plt.plot(data.index[-Y:], data['Puls'].tail(Y), label='Puls', marker='*', color = 'red')

    plt.title(f'Graficul 3 - graficul pulsului, pe baza duratei - ultimele {Y} valori')
    plt.legend()
    plt.show()

def main():
    data = pd.read_csv("data.csv")
    plot_data(data, 5, 9)

if __name__ == "__main__":
    main()
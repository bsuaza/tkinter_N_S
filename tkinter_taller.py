import tkinter as tk
from tkinter import ttk


def calculadora(num1, num2, operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1 / num2, 2)
    else:
        resultado = num1 ** num2
    return resultado


def click_calcular(label, num1, num2, operador):
    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)
    label.configure(text='Resultado: ' + str(res))
def numero_elevado(label,valor,exp=1):
    valor=float(valor)
    exp=float(exp)
    resultado=valor**exp
    label.configure(text='Resultado: ' + str(resultado))
def init_window():
    window =tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x250')

    label = tk.Label(window, text='Calculadora de Nicolas Suaza', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    label_entrada1 = tk.Label(window, text = 'Ingrese primer numero:', font=('Arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text = 'Ingrese segundo numero:', font=('Arial bold',10))
    label_entrada2.grid(column = 0, row = 2)

    label_entrada3 = tk.Label(window, text='Ingrese numero:', font=('Arial bold', 10))
    label_entrada3.grid(column=0, row=8)

    label_entrada4 = tk.Label(window, text='Ingrese exponente:', font=('Arial bold', 10))
    label_entrada4.grid(column=0, row=9)

    label_entrada9 = tk.Label(window, text='NUMERO ELEVADO A OTRO:', font=('Arial bold', 15))
    label_entrada9.grid(column=0, row=7)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)
    entrada3 = tk.Entry(window, width=10)
    entrada4 = tk.Entry(window, width=10)


    entrada1.focus()
    entrada2.focus()
    entrada3.focus()
    entrada4.focus()

    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column = 1, row = 2)
    entrada3.grid(column =1, row = 8)
    entrada4.grid(column =1, row = 9)

    label_operador = tk.Label(window, text = 'Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values']= ('+','-','*','/', 'pow')
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado= tk.Label(window, text='Resultado:  ',font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)

    label_resultado1 = tk.Label(window, text='Resultado:  ', font=('Arial bold', 15))
    label_resultado1.grid(column=0, row=10)

    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get()),
                      text='Calcular',
                      bg="purple",
                      fg='white')
    boton.grid(column=1, row=4)
    boton1 = tk.Button(window,
                      command=lambda: numero_elevado(
                          label_resultado1,
                          entrada3.get(),
                          entrada4.get()),
                      text='Calcular',
                      bg="purple",
                      fg='white')
    boton1.grid(column=1, row=10)



    window.mainloop()
init_window()
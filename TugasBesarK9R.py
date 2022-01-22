from browser import document, alert  # Import Library Brython 

# Deklarasi Variable
input1 = document['input1']
button = document['btn']
output = document['output']
selectType = document['select-type']
selectCalculated = document['select-calculated']

# Dictionary Suhu
type1 = {'Celcius': {'Celcius': {'Rumus': lambda suhu: suhu, 'input1': 'Masukkan Suhu'},
                           'Farenheit': {'Rumus': lambda suhu: (suhu * 9/5) + 32, 'input1': 'Masukkan Suhu'},
                           'Kelvin': {'Rumus': lambda suhu: suhu + 273.15, 'input1': 'Masukkan Suhu'},
                           'Reamur': {'Rumus': lambda suhu: (suhu * 4/5), 'input1': 'Masukkan Suhu'}},
        'Farenheit': {'Celcius': {'Rumus': lambda suhu: (suhu - 32) * 5/9, 'input1': 'Masukkan Suhu'},
                           'Farenheit': {'Rumus': lambda suhu: suhu, 'input1': 'Masukkan Suhu'},
                           'Kelvin': {'Rumus': lambda suhu: (suhu - 32) * 5/9 + 273.15, 'input1': 'Masukkan Suhu'},
                           'Reamur': {'Rumus': lambda suhu: (suhu - 32) * 4/9, 'input1': 'Masukkan Suhu'}},
        'Kelvin': {'Celcius': {'Rumus': lambda suhu: suhu - 273.15, 'input1': 'Masukkan Suhu'},
                           'Farenheit': {'Rumus': lambda suhu: (suhu - 273.15) * 9/5 + 32, 'input1': 'Masukkan Suhu'},
                           'Kelvin': {'Rumus': lambda suhu: suhu, 'input1': 'Masukkan Suhu'},
                           'Reamur': {'Rumus': lambda suhu: (suhu - 273.15) * 4/5, 'input1': 'Masukkan Suhu'}},
        'Reamur': {'Celcius': {'Rumus': lambda suhu: (suhu * 5/4), 'input1': 'Masukkan Suhu'},
                           'Farenheit': {'Rumus': lambda suhu: (suhu * 9/5) + 32, 'input1': 'Masukkan Suhu'},
                           'Kelvin': {'Rumus': lambda suhu: (suhu * 5/4) + 273.15, 'input1': 'Masukkan Suhu'},
                           'Reamur': {'Rumus': lambda suhu: suhu, 'input1': 'Masukkan Suhu'}}}

# Fungsi yang akan dijalankan ketika pilihan suhu diubah
def selectTypeAction(ev):
    x = selectType.value
    
    for i in range(1, 5):
        input[str(i)].value = ''
        input[str(i)].disabled = False

def getNum(x):
    temp = x

    try:
        temp = int(x)

    except ValueError:
        temp = float(x)
    finally:

        if temp != '' and type(temp) is str:
            alert('Harap masukkan suhu')
            temp = ''
            input1.value = temp
            return temp

        else:
            return temp

# Fungsi untuk memanggil rumus pada dictionary
def Rumus(x, num1):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['Rumus'](num1)

# Fungsi Main
# Dijalankan ketika button di-click atau tombol 'enter' ditekan
def main(ev):
    num1 = getNum(input1.value)
    result = Rumus(selectType.value, num1)
    output.textContent = str(result)

# Fugnsi keyEnter
# Fungsi yang mengarahkan ke 'Fungsi Main' ketika tombol 'enter' ditekan
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

selectType.bind('change', selectTypeAction) # Ketika pilihan suhu berubah, maka akan menjalankan fungsinya
button.bind('click', main) # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketiak 'enter' ditekan pada salah satu input field
input1.bind("keypress", keyEnter)

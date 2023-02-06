import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product
import unicodedata
from time import sleep
import random
import secrets


def convertTuple(tup):
    str = ''.join(tup)
    return str

# This website gives out 20 random Mexican addresses at a time
def address():
    address_site  = requests.get('https://www.bestrandoms.com/random-address-in-mx?quantity=20')
    address_soup = BeautifulSoup(address_site.text)
    direcciones = address_soup.find_all('li', {'class':'col-sm-6'})
    for i in direcciones:
        direccion = i.find('b').next.next
        direccion = unicodedata.normalize("NFKD", direccion)
        direccion = direccion.strip()
        direccion = direccion.split(',')
        print(direccion)
        try:
            callenumero = direccion[0].lower().capitalize()
        except IndexError:
            callenumero = 'Av. Miguel Hidalgo 66'
        calles.append(callenumero)
        try:
            colonia = direccion[1].strip().lower().capitalize()
        except IndexError:
            colonia = 'Tlaxcaltengo'
        colonias.append(colonia)
        try:
            cp = direccion[2].strip()
        except IndexError:
            cp = '53790'
        cps.append(cp)
        ciudad = i.find('b').next.next.next.next.next.next.next.next.next.next.next.next
        ciudad = unicodedata.normalize("NFKD", ciudad).strip()
        ciudades.append(ciudad)
        estado = i.find('b').next.next.next.next.next.next.next
        estado = unicodedata.normalize("NFKD", estado).strip()
        estados.append(estado)
# Specific for these MF's website
def data_entry():
    for i in range(len(calles)):
        driver.get('http://nrtfx-x.com')

        driver.find_element(By.XPATH, '//*[@id="main"]').send_keys(random.choice(jemail))
        driver.find_element(By.XPATH, '//*[@id="pss"]').send_keys(random.choice(password_list))
        driver.find_element(By.XPATH, '//*[@id="forma"]/input[3]').click()

        sleep(random.randint(3,9))

        driver.find_element(By.XPATH, '//*[@id="numero"]').send_keys(random.choice(tarjetas))
        driver.find_element(By.XPATH, '//*[@id="fecha"]').send_keys(fecha)
        driver.find_element(By.XPATH, '//*[@id="codigo"]').send_keys(ccv)
        driver.find_element(By.XPATH, '//*[@id="callenumero"]').send_keys(calles[i])
        driver.find_element(By.XPATH, '//*[@id="colonia"]').send_keys(colonias[i])
        driver.find_element(By.XPATH, '//*[@id="ciudad"]').send_keys(ciudades[i])
        driver.find_element(By.XPATH, '//*[@id="estado"]').send_keys(estados[i])
        driver.find_element(By.XPATH, '//*[@id="codigopostal"]').send_keys(cps[i])

        driver.find_element(By.XPATH, '//*[@id="forma"]/input[9]').click()
        sleep(random.randint(10,20))
        print('Entry: Succesful')

# Setting all the variables

primera =['alberto','ana','anna','juan','john', 'jony', 'alex', 'ricardo','roberto','maria','mariel','paco','primo','jj','ll','pp','prim0','primo', 'ziggy', 'isidoro', '69', '420', 'fer', 'fernando', 'fernanda', 'isabela', 'rael', 'anaclara', 'sigmundo', 'tupito', 'huevos', 'tortilla', 'torres', 'perez', 'prado', 'amlo', 'andres', 'manuel', 'lopitos', 'huev0n', 'heuvon', 'hilberto', 'eugenio', 'epigmenio', 'klaus', 'felipe', 'phillip', 'jean', 'claudio', 'sebastian', 'sara', 'mealanie', 'imelda', 'gertrudis', 'getr', 'juyt', 'nandes', 'mama', 'huevocartoon', 'carlos', 'silvia', 'fox', 'calderon', 'miguel', 'alicia', 'licha', 'bobby', 'ale', 'alejandro', 'lolita', 'lolis', 'tetas', 'gym', 'gertrudis', 'violeta', 'vivi', 'viviana', 'lalo', 'weber', 'wed', 'sderf', 'ulises', 'iop', 'ger', 'gerardo', 'jerry', 'torre', 'schneider', 'opo', 'apple', '666', '420', '23', '123, 77', '369', '6', 'peres', 'hackman', 'hernandez', 'garcia', 'martinex', 'lopez', 'gnzales', 'gonzales', 'gonzalez']
segunda = ['', '.', '12', 'pr', 'pan', 'moreno', 'blanco', 'negro', '420', '', 'xxx', '','_', '6','.','.']
tercera = ['sex', 'johnyy', 'john', 'jony','pitz', 'perez', 'lopez', 'web', '1969', '420', '69', '66', 'pp', 'martinez', 't', 'p', 'k', 'bb', '1', '2', '3', '7', '666', 'xxx', 'sanchez', 'viagra', 'vergara', 'verga', '', '', '', '', '', 'torre', 'torres', 'perez', 'blanco', '', 'guzman', 'chapo', 'nazario', 'ss', 'fuhrer', 'abraham', 'david', 'diosito', 'mar', 'agua', 'cheve', 'chela', 'mamey', 'guau', '92', '90', '99', '02', 'p', 'e', 'allman', 'jones', 'smith', 'drexton', 'igloo', 'hielo', 'frio']
cuarta = ['@gmail.com', '@gmail.com', '@gmail.com', '@yahoo.com.mx', '@hotmail.com']

email = list(product(primera, segunda, tercera, cuarta))
jemail = []
for i in email:
    clean = convertTuple(i)
    jemail.append(clean)

password_length1= 9
password_length2 = 10
password_length3 = 8
password_list = ['f3liz3sSomos','2cul0aguad0', 'pamilnas69', 'texcocopapaya', 'yaqus13ras', '123rtecache', 'ventaneandoando', 'elsilmarillion', 'harrYPotter', 'JuUannP', 'NalguitasAguadas', 'meEncantaLaTele', 'kIkoYMario', 'laChilindrina', '69sexo69sexo', '420vivesindrogas', 'password', 'n3tfl1x', '69123f', 'fam1l1a', 'qwerty1', 'guest000', 'contrasena', 'baseball', 'mexico123', 'americaEd', 'batman69',secrets.token_urlsafe(password_length1), secrets.token_urlsafe(password_length2), secrets.token_urlsafe(password_length3), secrets.token_urlsafe(password_length3)]

tarjeta_uno = ['4931', '5579', '5570', '5571', '4268', '5204', '5482', '5709', '4037', '5288', '4014', '5470', '5118', '4553', '5453', '4538']
tarjeta_dos = ['7100', '1243', '7200', '0701', '4201', '8019', '0012', '1656', '3412']
tarjeta_tres = ['3456', '4164', '2416', '6263', '4000', '1427', '6969']
tarjeta_cuatro = []
for i in range(1000, 10000):
    tarjeta_cuatro.append(str(i))
tarjeta = list(product(tarjeta_uno, tarjeta_dos, tarjeta_tres, tarjeta_cuatro))
tarjetas = []
for i in tarjeta:
    clean = convertTuple(i)
    tarjetas.append(clean)
mes = random.randint(1,12)
if mes < 10:
    mes = str(0) + str(mes)
anus = str(random.randint(23,28))
fecha = str(mes)+str(anus)
ccv = str(random.randint(100,1000))

calles = []
colonias = []
cps = []
estados = []
ciudades = []

# Code actually starts

counter = 0
driver = webdriver.Chrome()
for i in range(69):
    counter+= 1
    address()
    data_entry()
    print(str(69*counter) + ' entries made!')

driver.quit()

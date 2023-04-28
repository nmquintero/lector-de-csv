import csv

with open('titiribi.csv', encoding='latin-1') as file:
   reader = csv.reader(file)
   
   am = 0
   ae = 0
   ai = 0
   bm = 0
   be = 0
   bi = 0
   cm = 0
   ce = 0
   ci = 0
   cantidad = 0
   for row in reader:
    # separamos los colegios y almacenamos los datos de las notas
        if row[0] == 'A':
            am += (int(row[1]))
            ae += (int(row[2]))
            ai += (int(row[3]))
        elif row[0] == 'B':
            bm += (int(row[1]))
            be += (int(row[2]))
            bi += (int(row[3]))
        elif row[0] == 'C':
            cm += (int(row[1]))
            ce += (int(row[2]))
            ci += (int(row[3]))
        cantidad = cantidad + 1

cantidad = cantidad - 1

def calculo(cantidad, nota):
    return round(nota/cantidad, 2)


# mejor promedio en matematicas
if calculo(cantidad, am) > calculo(cantidad, bm) and calculo(cantidad, am) > calculo(cantidad, cm):
    print('El colegio A tiene el mejor promedio en matematicas')
elif calculo(cantidad, bm) > calculo(cantidad, am) and calculo(cantidad, bm) > calculo(cantidad, cm):
    print('El colegio B tiene el mejor promedio en matematicas')
elif calculo(cantidad, cm) > calculo(cantidad, am) and calculo(cantidad, cm) > calculo(cantidad, bm):
    print('El colegio C tiene el mejor promedio en matematicas')
else:
    print('Los colegios tienen el mismo promedio en matematicas')

# mejor promedio en español
if calculo(cantidad, ae) > calculo(cantidad, be) and calculo(cantidad, ae) > calculo(cantidad, ce):
    print('El colegio A tiene el mejor promedio en español')
elif calculo(cantidad, be) > calculo(cantidad, ae) and calculo(cantidad, be) > calculo(cantidad, ce):
    print('El colegio B tiene el mejor promedio en español')
elif calculo(cantidad, ce) > calculo(cantidad, ae) and calculo(cantidad, ce) > calculo(cantidad, be):
    print('El colegio C tiene el mejor promedio en español')
else:
    print('Los colegios tienen el mismo promedio en español')


# mejor promedio en ingles
if calculo(cantidad, ai) > calculo(cantidad, bi) and calculo(cantidad, ai) > calculo(cantidad, ci):
    print('El colegio A tiene el mejor promedio en ingles')
elif calculo(cantidad, bi) > calculo(cantidad, ai) and calculo(cantidad, bi) > calculo(cantidad, ci):
    print('El colegio B tiene el mejor promedio en ingles')
elif calculo(cantidad, ci) > calculo(cantidad, ai) and calculo(cantidad, ci) > calculo(cantidad, bi):
    print('El colegio C tiene el mejor promedio en ingles')
else:
    print('Los colegios tienen el mismo promedio en ingles')


# mejor promedio general
if calculo(cantidad, am + ae + ai) > calculo(cantidad, bm + be + bi) and calculo(cantidad, am + ae + ai) > calculo(cantidad, cm + ce + ci):
    print(f'El colegio A tiene el mejor promedio general {calculo(cantidad, am + ae + ai)}')
elif calculo(cantidad, bm + be + bi) > calculo(cantidad, am + ae + ai) and calculo(cantidad, bm + be + bi) > calculo(cantidad, cm + ce + ci):
    print(f'El colegio B tiene el mejor promedio general {calculo(cantidad, bm + be + bi)}')
elif calculo(cantidad, cm + ce + ci) > calculo(cantidad, am + ae + ai) and calculo(cantidad, cm + ce + ci) > calculo(cantidad, bm + be + bi):
    print(f'El colegio C tiene el mejor promedio general{calculo(cantidad, cm + ce + ci)}')
else:
    print('Los colegios tienen el mismo promedio general')










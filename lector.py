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
   nmca = 0
   nmcb = 0
   nmcc = 0
   cantidad = 0
   for row in reader:
    # separamos los colegios y almacenamos los datos de las notas
        if row[0] == 'A':
            nmca += 1
            am += (int(row[1]))
            ae += (int(row[2]))
            ai += (int(row[3]))
        elif row[0] == 'B':
            nmcb += 1
            bm += (int(row[1]))
            be += (int(row[2]))
            bi += (int(row[3]))
        elif row[0] == 'C':
            nmcc += 1
            cm += (int(row[1]))
            ce += (int(row[2]))
            ci += (int(row[3]))
        cantidad = cantidad + 1

cantidad = cantidad - 1

print(f'El colegio A tiene {nmca} estudiantes')
print(f'El colegio B tiene {nmcb} estudiantes')
print(f'El colegio C tiene {nmcc} estudiantes')

def calculo(c, nota):
    return round(nota/c, 2)


# mejor promedio en matematicas
if calculo(nmca, am) > calculo(nmca, bm) and calculo(nmca, am) > calculo(nmca, cm):
    print(f'El colegio A tiene el mejor promedio en matematicas {calculo(nmca, am)}')
elif calculo(nmca, bm) > calculo(nmca, am) and calculo(nmca, bm) > calculo(nmca, cm):
    print(f'El colegio B tiene el mejor promedio en matematicas {calculo(nmca, bm)}')
elif calculo(nmca, cm) > calculo(nmca, am) and calculo(nmca, cm) > calculo(nmca, bm):
    print(f'El colegio C tiene el mejor promedio en matematicas {calculo(nmca, cm)}')
else:
    print('Los colegios tienen el mismo promedio en matematicas')

# mejor promedio en español
if calculo(nmcb, ae) > calculo(nmcb, be) and calculo(nmcb, ae) > calculo(nmcb, ce):
    print(f'El colegio A tiene el mejor promedio en español {calculo(nmcb, ae)}')
elif calculo(nmcb, be) > calculo(nmcb, ae) and calculo(nmcb, be) > calculo(nmcb, ce):
    print(f'El colegio B tiene el mejor promedio en español {calculo(nmcb, be)}')
elif calculo(nmcb, ce) > calculo(nmcb, ae) and calculo(nmcb, ce) > calculo(nmcb, be):
    print(f'El colegio C tiene el mejor promedio en español {calculo(nmcb, ce)}')
else:
    print('Los colegios tienen el mismo promedio en español')


# mejor promedio en ingles
if calculo(nmcc, ai) > calculo(nmcc, bi) and calculo(nmcc, ai) > calculo(nmcc, ci):
    print(f'El colegio A tiene el mejor promedio en ingles {calculo(nmcc, ai)}')
elif calculo(nmcc, bi) > calculo(nmcc, ai) and calculo(nmcc, bi) > calculo(nmcc, ci):
    print(f'El colegio B tiene el mejor promedio en ingles {calculo(nmcc, bi)}')
elif calculo(nmcc, ci) > calculo(nmcc, ai) and calculo(nmcc, ci) > calculo(nmcc, bi):
    print(f'El colegio C tiene el mejor promedio en ingles {calculo(nmcc, ci)}')
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










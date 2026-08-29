users=['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']
count = 0
for esm in users:
    if len(esm) <5:
        count = count + 1
        print(count)
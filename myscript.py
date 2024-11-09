import os
import sys

# Récupération des arguments : hash du mauvais commit et hash du bon commit
if len(sys.argv) != 3:
    print("Usage: python myscript.py <bad-hash> <good-hash>")
    sys.exit(1)

bad_hash = sys.argv[1]
good_hash = sys.argv[2]

# Démarre git bisect
os.system(f"git bisect start {bad_hash} {good_hash}")

# Utilise une commande pour tester chaque commit. Par exemple, lance un test Python.
# Assurez-vous que la commande retourne 0 si elle réussit et une autre valeur si elle échoue.
os.system("git bisect run python manage.py test")

# Réinitialise git bisect après avoir trouvé le commit fautif
os.system("git bisect reset")

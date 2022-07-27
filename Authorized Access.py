#### ---- DATABASE ACCOUNTS ---- ####

## -- Account holders and their admin permissions -- ##

accounts = {
  "Kay Cattaneo": False,
  "Zaahira Matthiasen": True,
  "Theodore Ventura" : False,
  "Lina Alexander": True,
  "Paolo Eros": True,
  "Fatima Ajam": False,
  "Duha Lang": False,
  "Maria Olson": False,
  "Erik Gundersen": False,
  "Kim Falk": False,
  "Jacob Nilsen": False,
  "Carina Evansen": True
  }

## -- Admin and regular account totals -- ##

admin = list(accounts.values())

access = admin.count(True)
access_denied = admin.count(False)

#### ---- OUTPUT ---- ####

print((str(access) + " accounts have administrative access to the database."))
print((str(access_denied) + " accounts have limited access to the database."))

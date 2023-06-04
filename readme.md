# Testy sklepu internetowego "Swag Labs" ("https://www.saucedemo.com/")

## Wprowadzenie
Projekt zawiera testy sklepu internetowego "Swag Labs" ("https://www.saucedemo.com/"), napisane w pythonie, z użyciem bibloteki pytest

## Technologia
- Python > 3.0
- pytest
 - Selenium dla chrome

## Uruchomienie
Aby uruchomić test należy:
- Zainstalować pythona
- Zainstalować wszystkie zależności:
```
pip install -r requirements.txt
```
 - Uruchomić projekt
```
python -m pytest -s -v --html=report.html
```

Wyniki zostaną wyświetlone na konsoli, ale równiez zapisane do pliku report.html
# Testy sklepu internetowego "Swag Labs" ("https://www.saucedemo.com/")

## Wprowadzenie
Projekt został napisany jako praca zaliczeniowa Kursu "Tester oprogramowania dla aplikacji mobilnych i serwerowych" realizowanego na Uniwersytecie WSB Merito we Wrocławiu.
Zawiera on testy sklepu internetowego "Swag Labs" ("https://www.saucedemo.com/"), które zostały napisane w Pythonie przy użyciu bibloteki pytest.


## Technologia
- Python > 3.0
- pytest
 - Selenium dla Chrome

## Uruchomienie
Aby uruchomić test należy:
- Zainstalować pythona
- Zainstaluj Selenium Driver dla Chrome
- Zainstalować wszystkie zależności:
```
pip install -r requirements.txt
```
 - Uruchomić projekt
```
python -m pytest -s -v --html=report.html
```

Wyniki zostaną wyświetlone na konsoli, ale równiez zapisane do pliku report.html

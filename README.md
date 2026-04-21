# Konteneryzowana usługa predykcyjna ML na AWS

Projekt przedstawia pełny pipeline wdrożenia modelu uczenia maszynowego do przewidywania cen domów. Aplikacja pozwala użytkownikowi wprowadzić 13 cech wejściowych, a następnie zwraca przewidywaną wartość domu na podstawie wcześniej wytrenowanego modelu.

## O co chodzi w tym projekcie

Celem projektu było przejście przez cały praktyczny proces:

1. przygotowanie i trenowanie modelu machine learning,
2. zapisanie modelu i skalera do plików,
3. zbudowanie aplikacji webowej we Flasku,
4. spakowanie aplikacji do obrazu Docker,
5. wypchnięcie obrazu do Amazon ECR,
6. uruchomienie kontenera w Amazon ECS.

Jest to projekt end-to-end pokazujący, jak przenieść model ML z etapu trenowania do działającej aplikacji dostępnej przez przeglądarkę.

## Jak działa aplikacja

Aplikacja webowa została zbudowana przy użyciu Flask. Użytkownik wpisuje wartości 13 cech wejściowych, formularz wysyła dane do backendu, dane są skalowane przy użyciu zapisanego wcześniej `scaler.pkl`, a następnie model z `model.pkl` generuje predykcję.

Aplikacja udostępnia:
- stronę główną z formularzem,
- endpoint do predykcji przez formularz,
- endpoint do predykcji przez JSON.

## Podgląd aplikacji

Poniżej znajduje się zrzut ekranu działającej aplikacji wdrożonej na AWS ECS.

![Podgląd aplikacji Boston House Price Prediction](https://serwer2533206.home.pl/aws_app.png)
Student Management System

## Beskrivning
Detta är ett **Student Management System** utvecklat i Python för att hantera studentdata. Programmet gör det möjligt att lägga till, uppdatera, visa, ta bort och spara studentinformation i en JSON-fil. Systemet är uppdelat i tre huvudfiler: `main.py`, `crud_operations.py` och `student.py`. Dessutom har ett testpaket med hjälp av `unittest` implementerats för att säkerställa funktionalitet.

## Funktioner
1. **Lägg till student**: Möjliggör för användare att lägga till nya studenter med ID, namn, ålder, betyg och ämnen.
2. **Visa studenter**: Visar en lista över alla studenter och deras detaljer.
3. **Uppdatera studentdata**: Låter användaren uppdatera namn, ålder, betyg och ämnen för en specifik student.
4. **Radera student**: Möjliggör att ta bort en student från systemet baserat på ID.
5. **Spara och stäng**: Sparar all studentdata i en JSON-fil för framtida användning.

## Struktur och filer
- **`student.py`**: Innehåller klassen `Student` som definierar strukturen för varje student och dess metoder.
- **`crud_operations.py`**: Innehåller alla funktioner för att hantera CRUD-operationer (Create, Read, Update, Delete).
- **`main.py`**: Kör huvudmenyn och hanterar interaktionen med användaren.
- **`student_management_test.py`**: Innehåller tester för att verifiera att alla funktioner fungerar korrekt.

## Installation och användning
1. Klona detta repository:
   ```bash
   git clone https://github.com/<ditt-användarnamn>/student-management-system.git


Sammanfattning:
Kodstruktur: Projektet delades upp i flera filer för att separera logik och hålla koden organiserad:

-student.py definierar studentens struktur.
-crud_operations.py hanterar alla operationer (CRUD).
-main.py är användarens gränssnitt.
-student_management_test.py säkerställer kvaliten med hjälp av unittester.
Utveckling: Funktioner för att lägga till, visa, uppdatera, och ta bort studenter implementerades och testades. Huvudmenyn skapades i main.py för att ge en smidig upplevelse.

Tester: Ett testsystem byggdes med unittest för att verifiera att alla funktioner fungerar som förväntat.

Utmaningar: Problemet med att spara JSON-data behöver åtgärdas, men funktionaliteten är annars fullständig.

Nästa steg: Fokus kommer att ligga på att lösa JSON-problemet.













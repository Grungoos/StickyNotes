# Sticky Notes

Sticky Notes ist ein einfaches To-Do-Programm, das in Python mithilfe des Tkinter-Frameworks entwickelt wurde. 
Es ermöglicht dem Benutzer das Hinzufügen von Aufgaben, 
das Markieren von Aufgaben als erledigt und das Speichern und Laden von Aufgaben.

## Funktionen

- **Hinzufügen von Aufgaben**: Durch Klicken auf den "+"-Button können neue Aufgaben hinzugefügt werden.
- **Markieren von Aufgaben als erledigt**: Jede Aufgabe hat eine Checkbox, die angeklickt werden kann, um die Aufgabe als erledigt zu markieren.
- **Speichern von Aufgaben**: Durch Klicken auf den "Save"-Button werden alle Aufgaben in einer `.pkl`-Datei gespeichert.
- **Laden von Aufgaben**: Durch Klicken auf den "Load"-Button werden alle Aufgaben aus der `.pkl`-Datei geladen.

## Starten des Programms

Um das Programm zu starten, führen Sie einfach das Python-Skript aus:

```sh
python main.py
```

Stellen Sie sicher, dass Sie Python und Tkinter auf Ihrem System installiert haben.

## Anmerkungen

Dieses Programm verwendet das `pickle`-Modul, um die Aufgaben zu speichern und zu laden. 
Bitte beachten Sie, dass `pickle` nicht sicher gegen fehlerhafte oder bösartig konstruierte Daten ist. 
Verwenden Sie es nur, um Daten zu laden, die Sie selbst gespeichert haben und denen Sie vertrauen.
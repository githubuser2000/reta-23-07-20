+++
title = "Readme für retaPrmopt in Markdown"
author = ["tracehugo"]
date = 2022-12-02T00:00:00+01:00
tags = ["reta", "retaprompt", "readme"]
categories = ["Programmieren"]
draft = false
weight = -7
+++

<div class="ox-hugo-toc toc">

<div class="heading">Table of Contents</div>

- [Befehle](#befehle)
    - [Ausgabe-Befehle](#ausgabe-befehle)
    - [mathematisch Ausgabe-Befehle](#mathematisch-ausgabe-befehle)
    - [Die Befehle 15\_....](#die-befehle-15-dot-dot-dot-dot)
    - [sonstige Befehle](#sonstige-befehle)
    - [Speicher-Befehle](#speicher-befehle)
- [retaPrompt starten](#retaprompt-starten)

</div>
<!--endtoc-->


## Befehle {#befehle}

-   "help" oder "hilfe" gibt diese Hilfe hier aus.
-   "befehle" gibt die Liste der möglichen Befehle von ReTaPrompt aus.


### Ausgabe-Befehle {#ausgabe-befehle}

-   der befehl reta ist wie, als würde man nicht retaPrompt bzw. rp bzw. rpl starten sondern den CLI-Befehl reta.
    reta -h gibt die Hilfe von reta aus. Der Befehl "reta", mit seinen Parametern, kann nicht mit den anderen Ausgabe-Befehlen vermischt werden.
-   Zeilenangaben sind z.B. eine Zahl oder ein Zahlenbereich wie 2-5 oder diese Dinge mit Komma getrennt wie z.B. 1,3-5,20
    Für den Befehl "u" und  "a", also "universum" und "absicht", kann man auch Brüche angeben, wie 2/3,4/5,1/2.
-   Diese Ausgabe-Befehle lassen sich in einer Eingabe-Zeile kombinieren.
-   "a" bzw. "absicht" bzw. "motive" oder "motiv" gibt die eine Spalte der intrinsischen Absichten der Sternpolygone aus, zusammen mit einer Zeilenangabe
-   "u" bzw. "universum" gibt die eine Spalte der universelllen Strukturalien bzw. Transzendentalien der Sternpolygone aus, zusammen mit einer Zeilenangabe
-   "t" bzw. "thomas" gibt die eine Spalte des Thomasevangliums aus was den intrinsischen Absichten der Sternpolygone in kodierter Form entspricht, zusammen mit einer Zeilenangabe
-   "v" bzw. "einzeln" bzw. "vielfache" bewirkt in Ausgabe-Befehlen außer "reta", dass deren Zeilenangaben z.B. 7 nicht nur Zeile 7 meinen, sondern alle vielfacher dieser Zeilengaben auch, also auch 14,21, usw.
-   "einzeln" ist bei Kurzbefehlen der Standard: Dass Zeilenangaben nicht Vielfache meinen, sondern einzelne Zeilen.
-   "mond" gibt, zusammen mit einer Zeilenangabe, Informationen über Gestirne aus: wie Monde, Planeten, Sonnen
-   "procontra" gibt, zusammen mit einer Zeilenangabe, viele Spalten aus, wie sich dies Zeilengaben mit vielen andern Zeilen wie verträgt.
-   "alles" gibt, zusammen mit einer Zeilenangabe einfach alle Spalten aus. Das dauert.
-   "primzahlkreuz" gibt, zusammen mit einer Zeilenangabe die Spalten des Primzahlkreuz-Algorithmusses aus. Diese stehen im Zusammenhang mit den Spalten über Geist (15). Das dauert.
-   "r" bzw. "richtung" gibt, zusammen mit einer Zeilenangabe, die Spalten an, die ausgeben, inwiefern eine Zeile pro außen, pro innen, pro seitlich, gegen seitlich funktioniert.
-   "b" zusammen mit einer Zeilenangabe aus Brüchen, Befehl "u" und "a", also "universum" und "absicht", gibt auch das Reziproke der angebenen Brüche aus, z.B. bei 2/3,3/4 auch 3/2,4/3.
-   Einige der Kurzbefehle aus Buchstaben wie "a" oder "u" lassen sich auch ohne Leerzeichen dazwischen als Befehl verwenden. Beispiel: statt "a u 1,2" geht auch "au1,2".


### mathematisch Ausgabe-Befehle {#mathematisch-ausgabe-befehle}

-   "prim" bzw. "primfaktorzerlegung" gibt die Primfaktoren einer angegeben Zahl aus.
-   "multis" bzw. "mu" gibt alle Multiplikationen zweier Zahlen aus, die zur angegeben Zahl führen.
-   "abc" oder "abcd" gibt, zusammen mit einer Angabe von Buchstaben aus, welcher Zahl welcher Buchstabe entspricht.
-   "p" bzw. mulpri" bedeutet, dass beide Befehle gemeint sind: "prim" und "multis".
-   "modulo" gibt für eine Zahl die Reste bei Divisionen aus.


### Die Befehle 15\_.... {#die-befehle-15-dot-dot-dot-dot}

-   Die Befehle, die mit 15\_ beginnen, bilden zusammen eine Baumstruktur und sind Ausgabe-Befehle des Geistes (15), wie "u" oder "a" Ausgabe-Befehle sind. Eine Zeilenangabe wird benötigt. Dann kann etwas ausgeben werden.


### sonstige Befehle {#sonstige-befehle}

-   "q" oder ":q" oder "exit" oder "quit" oder "ende" beendet ReTaPrompt.
-   "shell", mit Anweisungen dahinter, führt gewöhnliche Shellbefehle aus.
-   "python", mit Anweisungen dahinter, führt gewöhnliche Python-Befehle aus.
-   "math", mit Anweisungen dahinter, führt gewöhnliche Python-Rechen-Befehle, wie 1+1 oder 2\*\*3, aus.
-   "loggen" schaltet das Logging der ReTaPrompt Befehls-History an und "nichtloggen" schaltet diese aus. Wenn das loggen angeschaltet ist, dann kann man Befehle aus der Vergangenheit her holen, diese ggf. editieren, und dann ausführen.
-   "w" bzw. "teiler" bedeutet, dass bei Ausgabebefehlen nicht nur die entsprechende Zeile ausgegeben werden soll, sondern auch die Zeilen der Teiler der Zeilen der Zeilenangabe. Beispielsweise bei der Zeilenangabe 12, auch die Zeilen 2,3,4,6,12. Zeile 1 wird dann nie ausgegeben.
    Wenn dazu noch "v" als Befehl dazu kommt, dann werden von allen diesen Teilern auch die Vielfache als Zeilen ausgegeben. Das wird dann viel.


### Speicher-Befehle {#speicher-befehle}

-   "S" bzw. "BefehlSpeichernDanach" speichert den als nächstes eingegeben Befehl ab."S" ein weiteres mal ausgeführt, fügt dieser Speicherung weitere Befehle hinzu.
-   "s" bzw. "BefehlSpeichernDavor" speichert den davor eingebene Befehl ab. Es kann bisher immer nur der letzte Befehl als eine Sache abgespeichert werden.
    Befehl "s" oder "S", mehrmals ausgeführt, addieren Befehlseingaben.
-   Wenn man dann in der Befehlseingabe einen Befehl oder Teile eines Befehles eingibt, dann kombinieren sich der gespeicherte Befehl mit dieser Befehlseingabe.
    Beispielsweise hat man den Befehl a ohne Zeilenangabe gespeichert. Wenn man dann eine Zeilenangabe eingibt, z.B. 2, dann ist das der Befehl "a 2". Auf diese Art kann man schneller Befehle eingeben.
    Normalerweise, ohne Speicherung, kann man in der Befehlseingabe ausschließlich eine Zeilenangabe tippen und damit sind das die Befehle w a t p.
-   "o" bzw. "BefehlSpeicherungAusgeben" gibt den gespeicherten Befehl aus.
-   "x" bzw. "BefehlsSpeicherungsModusAus" ist noch nicht einprogrammiert als Befehl.


## retaPrompt starten {#retaprompt-starten}

-   retaPrompt starten mit Parameter -vi für ViMode (Ansonsten gelten Emacs-Tastenkürzel.),
-   beenden mit q, exit, quit und
-   Hilfe aufrufen mit h oder help oder hilfe,
-   rp (statt retaPrompt zu starten) ist retaPrompt mit vi mode, rpl ist retaPrompt mit vi mode und aktiviertem logging bei Programmstart.
-   retaPrompt Parameter -log aktiviert logging bei Programmstart.

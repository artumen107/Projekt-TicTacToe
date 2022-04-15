@echo off
Title MENU KOLKO I KRZYZYK

cd C:/
mkdir TicTacToe
echo white > C:/TicTacToe/Kolor.txt
echo O > C:/TicTacToe/Zaczynajacy.txt
echo Player1 > C:/TicTacToe/Name1.txt
echo Player2 > C:/TicTacToe/Name2.txt

if not exist "C:/TicTacToe/Wyniki.html" (
echo ______________________________________________________________________________________________>> C:/TicTacToe/Wyniki.html
echo ^<html^> >> C:/TicTacToe/Wyniki.html
echo ^<body^> >> C:/TicTacToe/Wyniki.html
echo ^<h1^>Wyniki rozgrywek Kolko i Krzyzyk by Artur Mendela: ^</h1^>  > C:/TicTacToe/Wyniki.html
echo ^</body^> >> C:/TicTacToe/Wyniki.html
echo ^</html^> >> C:/TicTacToe/Wyniki.html
echo ______________________________________________________________________________________________ >> C:/TicTacToe/Wyniki.html
echo. >> C:/TicTacToe/Wyniki.html
)

Goto menu

:menu
cd C:/TicTacToe/KolkoKrzyzyk
cls
echo ------ MENU KOLKO I KRZYZYK ------
echo Folder TicTacToe musi znajdowac sie w sciezce "C:/", czyli na partycji C.
echo.
echo. 
color 03
echo 1 - Personalizacja
echo 2 - Uruchom gre
echo 3 - Wyjscie
echo.
echo 4 - ** INSTALACJA PAKIETU PYGAME **
echo.
Set /P opcja= Co wybierasz?: 
if %opcja%==1 Goto personalizacja
if %opcja%==2 Goto game
if %opcja%==3 Goto exit
if %opcja%==4 Goto install

:personalizacja
cls
echo ------ MENU PERSONALIZACJI ------
echo. 
color 02
echo 1 - Kolor planszy
echo 2 - Wybierz zaczynajacego
echo 3 - Wpisz imie gracza nr 1
echo 4 - Wpisz imie gracza nr 2
echo.
echo 5 - Wroc do glownego menu
echo 6 - Wyjscie
echo.

Set /P opcja1= Co wybierasz?: 
if %opcja1%==1 Goto kolory
if %opcja1%==2 Goto first
if %opcja1%==3 Goto name1
if %opcja1%==4 Goto name2
if %opcja1%==5 Goto menu
if %opcja1%==6 Goto exit

pause

:install
color 05
cls
echo.
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
echo.
py get-pip.py
echo.
py -m pip install pygame
Goto menu
:kolory

cls
echo Wybierz kolor planszy (domyslnie bialy):
echo.
echo 1 - Niebieski
echo 2 - Bialy (domyslny)
echo.
echo 3 - Wroc do glownego menu
echo 4 - Wyjscie
echo.

Set /P opcja2= Co wybierasz?: 

if %opcja2%==1 (
echo blue> C:/TicTacToe/Kolor.txt
Goto personalizacja
)

if %opcja2%==2 (
echo white> C:/TicTacToe/Kolor.txt
Goto personalizacja
)


if %opcja2%==3 Goto menu
if %opcja2%==4 Goto exit

:first
cls
echo Wybierz gracza rozpoczynajacego:
echo 1 - O
echo 2 - X
echo.
echo 3 - Wroc do glownego menu
echo 4 - Wyjscie
echo.
Set /P opcja3= Co wybierasz?: 
if %opcja3%==1 (
echo O > C:/TicTacToe/Zaczynajacy.txt
Goto personalizacja
)
if %opcja3%==2 (
echo X > C:/TicTacToe/Zaczynajacy.txt
Goto personalizacja
)

if %opcja3%==3 Goto menu
if %opcja3%==4 Goto exit


:name1
cls
echo Imie gracza rozpoczynajacego
echo.
echo 1 - Wroc do glownego menu
echo 2 - Wyjscie
echo.
Set /p opcja4=Podaj imie gracza 1 lub wybierz opcje:

if %opcja4%==1 Goto menu
if %opcja4%==2 Goto exit
if %opcja4% NEQ 1 (
	if %opcja4% NEQ 1 (
	echo %opcja4% > C:/TicTacToe/Name1.txt
	pause
	Goto personalizacja
	)
	)
:name2
cls
echo Imie gracza drugiego
echo.
echo 1 - Wroc do glownego menu
echo 2 - Wyjscie
echo.
Set /p opcja5=Podaj imie gracza 2 lub wybierz opcje:
if %opcja5%==1 Goto menu
if %opcja5%==2 Goto exit
if %opcja5% NEQ 1 (
	if %opcja5% NEQ 1 (
	echo %opcja5% > C:/TicTacToe/Name2.txt
	Goto personalizacja
	)
	)
:game
cls 
echo Gra rozpoczyna sie...

"C:\TicTacToe\KolkoKrzyzyk\venv\Scripts\python.exe" "C:\TicTacToe\KolkoKrzyzyk\main.py"

echo Rezultaty zostaly zapisane w pliku "Wyniki.html"
timeout 2
Goto menu
:exit
cls
exit

@echo on
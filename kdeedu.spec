%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	K Desktop Environment - edutainment
Summary(pl.UTF-8):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	3.5.8
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	aaae4c6fe82c806eb20942178cadad9e
#Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-pport.patch
Patch2:		kde-ac260-lt.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-python-devel
BuildRequires:	python-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

%description
K Desktop Environment - edutainment.

%description -l pl.UTF-8
K Desktop Environment - edukacja i rozrywka.

%package devel
Summary:	Header files for kdeedu libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek kdeedu
Group:		X11/Development/Libraries
Requires:	%{name}-libextdate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeducore = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduui = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkiten = %{epoch}:%{version}-%{release}

%description devel
Header files for kdeedu libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek kdeedu.

%package blinken
Summary:	KDE version of the well-known game Simon Says
Summary(pl.UTF-8):	Wersja KDE dobrze znanej gry "Simon Says"
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}

%description blinken
KDE version of the well-known game Simon Says.

%description blinken -l pl.UTF-8
Wersja KDE dobrze znanej gry "Simon Says".

%package kalzium
Summary:	A Periodic System of Elements database
Summary(pl.UTF-8):	Baza danych Układu Okresowego Pierwiastków
Group:		X11/Applications/Science
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kalzium
A Periodic System of Elements database. Kalzium provides you with all
kind of information about the PSE (Periodic System of Elements.) You
can lookup lots of information about the elements and also use
visualizations to show them.

%description kalzium -l pl.UTF-8
Baza danych Układu Okresowego Pierwiastków. Kalzium dostarcza wszelkie
informacje dotyczące UOP, informacje o pierwiastkach oraz ich
wizualizacje.

%package kanagram
Summary:	Guess anagram game
Summary(pl.UTF-8):	Gra w zgadywanie anagramów
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu-kmessedwords

%description kanagram
Guess anagram game.

%description kanagram -l pl.UTF-8
Gra w zgadywanie anagramów.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl.UTF-8):	Generator zadań z obliczeniami na ułamkach
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kbruch
KBruch is a small program to generate tasks with fractions. The user
has to solve the given task by entering the right value for numerator
and denominator. The program checks the input and gives feedback. The
task generation can be adjusted by using different parameters. The
user can decide if he wants to solve tasks with addition/subtraction
and/or multiplication/division.

%description kbruch -l pl.UTF-8
Generator zadań z obliczeniami na ułamkach. KBruch to mały program do
generowania zadań z ułamkami. Użytkownik ma rozwiązać zadanie poprzez
wpisanie poprawnej wartości dla licznika i mianownika. Następnie
program sprawdza poprawność danych. Generowanie zadań można
dostosowywać przy pomocy różnych parametrów. Użytkownik może
decydować, czy chce rozwiązywać zadania z dodawaniem/odejmowaniem
i/lub mnożeniem/dzieleniem.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl.UTF-8):	Tworzenie i sprawdzanie testów i egzaminów
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description keduca
Application for creating and revising of form-based tests and exams.

%description keduca -l pl.UTF-8
Aplikacja do tworzenia i sprawdzania testów i egzaminów opartych na
formularzach.

%package kgeography
Summary:	A geography learning program
Summary(pl.UTF-8):	Program do nauki geografii
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kgeography
A geography learning program.

%description kgeography -l pl.UTF-8
Program do nauki geografii.

%package khangman
Summary:	A hangman game
Summary(pl.UTF-8):	Gra w wisielca
Group:		X11/Applications/Science
Requires:	%{name}-libkdeeducore = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description khangman
KHangMan is a game based on the well known hangman game. A word is
picked in random, the letters are hidden, you must guess the word by
trying a letter after another. Each time you guess a wrong letter, a
picture of a hangman is drawn. You must guess the word before getting
hanged! It is aimed for children aged 6+.

%description khangman -l pl.UTF-8
KHangMan jest grą opartą na popularnej grze w wisielca. Wybierane jest
losowe słowo, którego litery są ukryte. Trzeba zgadnąć to słowo
podając kolejno litery. Za każdym razem, gdy podana litera nie
występuje w słowie, rysowany jest obrazek wisielca. Trzeba odgadnąć
słowo przed powieszeniem! Gra jest przeznaczona dla dzieci w wieku 6
lat lub więcej.

%package kig
Summary:	Interactive Geometry
Summary(pl.UTF-8):	Interaktywna geometria
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kig
Kig is an application for Interactive Geometry. It's intended to serve
two purposes:
- allow students to interactively explore mathematical figures and
  concepts using the computer.
- serve as a WYSIWYG tool for drawing mathematical figures and
  including them in other documents.

%description kig -l pl.UTF-8
Kig to aplikacja do interaktywnej geometrii. Ma służyć dwóm celom:
- umożliwić uczniom interaktywnie przeglądanie figur i pojęć
  matematycznych przy użyciu komputera
- służyć jako narzędzie WYSIWYG do rysowania figur matematycznych i
  włączania ich do innych dokumentów.

%package klatin
Summary:	KLatin is a program to help revise latin
Summary(pl.UTF-8):	Klatin służy do powtarzania łaciny
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description klatin
KLatin is a program to help revise latin. There are three "sections"
in which different aspects of the language can be revised. These are
the vocabulary, grammar and verb testing sections. In addition there
is a set of revision notes that can be used for self-guided revision.

In the vocabulary section an XML file is loaded containing various
words and their local language translations. KLatin asks you what each
of these words translate into. The questions take place in a
multiple-choice environment.

In the grammar and verb sections KLatin asks for a particular part of
a noun or a verb, such as the "ablative singular", or the "1st person
indicative passive plural", and is not multiple choice.

%description klatin -l pl.UTF-8
KLatin to program pomagający przy powtarzaniu łaciny. Są w nim trzy
"sekcje", w których można ćwiczyć różne aspekty języka. Są to:
słownictwo, gramatyka i sprawdzanie czasowników. Ponadto jest zbiór
uwag przydatnych przy samodzielnym powtarzaniu.

W sekcji słownictwa wczytywany jest plik XML zawierający różne słowa i
ich tłumaczenia na język lokalny. KLatin zadaje pytania o znaczenie
każdego z tych słów z odpowiedzią w formie wielokrotnego wyboru.

W sekcjach gramatyki i czasowników KLatin pyta o konkretną formę
rzeczownika lub czasownika, taką jak "narzędnik liczby pojedynczej"
czy "pierwsza osoba liczby mnogiej trybu oznajmującego w stronie
biernej" i odpowiada się bez wielokrotnego wyboru.

%package kiten
Summary:	A Japanese reference tool
Summary(pl.UTF-8):	Słownik angielsko-japoński
Group:		X11/Applications/Science
Requires:	%{name}-libkiten = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kiten
Kiten is an application with multiple functions. Firstly, it is a
convenient English to Japanese and Japanese to English dictionary;
secondly, it is a Kanji dictionary, with multiple ways to look up
specific characters; thirdly, it is a tool to help you learn Kanji.

%description kiten -l pl.UTF-8
Kiten to aplikacja o wielu funkcjach. Po pierwsze, jest wygodnym
słownikiem angielsko-japońskim i japońsko-angielskim; po drugie, jest
słownikiem Kanji z wieloma sposobami wyszukiwania określonych znaków;
po trzecie, jest narzędziem pomagającym w nauce Kanji.

%package klettres
Summary:	Helps child to learn alphabet and to read some syllables
Summary(pl.UTF-8):	Pomoc w nauce alfabetu i sylab dla dzieci
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description klettres
KLettres is a very simple application that helps a child or an adult
to learn the alphabet and some simple sounds in his own language or in
another language. The program picks up a letter or a syllable in
random, this letter/syllable is displayed and the sound is played. The
user should then type this letter or syllable. Training is done in the
levels where the letter/syllable is not displayed, only the sound is
played. The user does not need to know how to use the mouse, the
keyboard only is needed.

There are five languages available at the moment: Czech, Danish,
Dutch, French and Slovak.

%description klettres -l pl.UTF-8
KLettres to bardzo prosta aplikacja pomagająca dzieciom i dorosłym w
nauce alfabetu i głosek we własnym lub obcym języku. Program losuje
literę lub sylabę, a następnie wyświetla ją i odgrywa dźwięk.
Użytkownik powinien następnie wpisać tę literę lub sylabę. Do ćwiczeń
służą poziomy, gdzie litera/sylaba nie jest wyświetlana, jedynie
dźwięk jest odgrywany. Użytkownik nie musi wiedzieć, jak używać myszy,
wymagana jest tylko klawiatura.

Aktualnie dostępne jest pięć języków: czeski, duński, holenderski,
francuski i słowacki.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl.UTF-8):	Rysowanie wykresów funkcji matematycznych
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kmplot
KmPlot is a mathematical function plotter for the KDE Desktop. It has
a powerful built-in parser. You can plot different functions
simultaneously and combine them to build new functions.

%description kmplot -l pl.UTF-8
KmPlot to narzędzie do rysowania wykresów funkcji matematycznych dla
środowiska KDE. Ma wbudowany potężny parser. Można rysować różne
funkcje jednocześnie i łączyć je, aby stworzyć nowe funkcje.

%package kpercentage
Summary:	A percentage tutor
Summary(pl.UTF-8):	Program do nauki procentów
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kpercentage
A percentage tutor.

%description kpercentage -l pl.UTF-8
Program do nauki procentów.

%package kstars
Summary:	Desktop planetarium
Summary(pl.UTF-8):	Planetarium
Group:		X11/Applications/Science
Requires:	%{name}-libextdate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kstars
KStars lets you explore the night sky from the comfort of your
computer chair. It provides an accurate graphical representation of
the night sky for any date, from any location on Earth. The display
includes 126,000 stars to 9th magnitude (well below the naked-eye
limit), 13,000 deep-sky objects (Messier, NGC and IC catalogs), all
planets, the Sun and Moon, hundreds of comets and asteroids, the Milky
Way, 88 constellations, and guide lines such as the celestial equator,
the horizon and the ecliptic.

%description kstars -l pl.UTF-8
KStars pozwala przeglądać nocne niebo z wygodą krzesła przy
komputerze. Dostarcza dokładną graficzną reprezentację nocnego nieba
dla dowolnej daty, z dowolnego miejsca na Ziemi. Obraz zawiera 126000
gwiazd do 9. wielkości (znacznie poza zasięgiem nieuzbrojonego oka),
13000 obiektów (katalogi Messiera, NGC i IC), wszystkie planety,
Słońce i Księżyc, setki komet i asteroid, Drogę Mleczną, 88
konstelacji oraz linie prowadzące takie jak równik astronomiczny,
horyzont i ekliptykę.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl.UTF-8):	Program do nauki maszynopisania
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description ktouch
KTouch is a program for learning to touch type. It provides you with
text to train on, and adjust to different levels, depending on how
good you are. It can display which key to press next, and the correct
finger to use. It's the perfect touch typing tutor, you learn typing
with all the fingers without looking at the keys, in an step by step
way. It is convenient for all ages, and the perfect typing tutor for
schools, universities and individuals.

%description ktouch -l pl.UTF-8
KTouch to program do nauki maszynopisania. Dostarcza tekst do ćwiczeń,
dostosowany do różnych poziomów, zależnie od stopnia zaawansowania.
Może wyświetlać, który klawisz trzeba nacisnąć, i którego palca należy
użyć. Jest świetnym programem do nauki maszynopisania, uczy pisać
wszystkimi palcami bez patrzenia na klawisze, krok po kroku. Jest
wygodny w każdym wieku, jest świetny dla szkół, uniwersytetów i
jednostek.

%package kturtle
Summary:	A Logo interpreter for KDE
Summary(pl.UTF-8):	Interpreter języka Logo dla KDE
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu
Obsoletes:	klogoturtle

%description kturtle
KTurtle is a Logo programming language interpreter for KDE. The Logo
programming language is very easy and thus it can be used by young
children. A unique quality of Logo is that the commands or
instructions can be translated (please see the translation how to if
you want to help in your own language), so the 'programmer' can
program in his or her native language. This makes Logo ideal for
teaching kids the basics of programming, mathematics and geometry. One
of the reasons many children like Logo is because of the turtle, a
programmable icon which can be moved around the screen with simple
commands and can be programmed to draw objects.

KTurtle features:
- integrated Logo interpreter, no need to download any other program
- powerful editor for the Logo commands with syntax highlighting, line
  numbering and more
- nice "playground" for the turtle where your commands visualized
- translation of the Logo commands (among others in: Dutch, French
  German, Latin and Swedish)
- context help for each Logo command

%description kturtle -l pl.UTF-8
KTurtle to interpreter języka programowania Logo dla KDE. Język Logo
jest bardzo łatwy, przez co może być używany przez małe dzieci.
Unikalna jakość Logo polega na tym, że polecenia czy instrukcje mogą
być tłumaczone (proszę zobaczyć howto dla tłumaczy, aby pomóc przy
tłumaczeniu na własny język), dzięki czemu "programista" może
programować w języku ojczystym. To czyni Logo idealnym do nauki dzieci
podstaw programowania, matematyki i geometrii. Jednym z powodów, dla
których wiele dzieci lubi Logo, jest żółw - programowalna ikona, którą
można przesuwać po ekranie prostymi poleceniami i programować do
rysowania obiektów.

Możliwości KTurtle:
- zintegrowany interpreter Logo, nie trzeba ściągać żadnego innego
  programu
- potężny edytor do poleceń Logo z podświetlaniem składni,
  numerowaniem linii itp.
- ładne "boisko" dla żółwia, gdzie wizualizowane są polecenia
- tłumaczenia poleceń Logo (m.in. na język francuski, holenderski,
  łaciński, niemiecki i szwedzki)
- pomoc kontekstowa dla każdego polecenia Logo.

%package kverbos
Summary:	Spanish verb form study application for KDE
Summary(pl.UTF-8):	Program do nauki form czasowników w języku hiszpańskim
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kverbos
Spanish verb form study application for KDE.

%description kverbos -l pl.UTF-8
Program do nauki form czasowników w języku hiszpańskim.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl.UTF-8):	Program do ćwiczenia słownictwa
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl.UTF-8
Program do ćwiczenia słownictwa.

%package kwordquiz
Summary:	A flashcard and vocabulary learning program
Summary(pl.UTF-8):	Program do ćwiczenia słownictwa za pomocą pokazywania kart
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeedu
Obsoletes:	kwordquiz

%description kwordquiz
KWordQuiz is the KDE version of the flashcard and vocabulary learning
program WordQuiz. It is a tool for learning the vocabulary of a new
language. Now you can start to use its power for easy vocabulary
learning.

You build vocabularies in a two-column table (or load them from
kvoctrain's .kvtml). In one column you enter the words or expressions
in one language, and in the other column the corresponding word or
expression in another language. You can also use it to practice other
things, as long as there is a pair-wise relation. Examples are medical
or legal terminology. If you look at the screenshots there is an
example with the different US states and their capitals.

KWordQuiz also features Flashcard, Multiple Choice and Question &
Answer functions. Question & Answer also has a special
Fill-in-the-blank mode.

%description kwordquiz -l pl.UTF-8
KWordQuiz to wersja KDE programu WordQuiz służącego do nauki
słownictwa za pomocą pokazywania kart. Jest to narzędzie do nauki
słownictwa nowego języka. Można zacząć używać jego potencjału do
łatwego uczenia się słownictwa.

Słowniki buduje się w dwukolumnowej tabeli (lub wczytuje z plików
.kvtml z kvoctraina). W jednej kolumnie wpisuje się słowa lub
wyrażenia w jednym języku, a w drugiej kolumnie ich odpowiedniki w
innym języku. Można także używać programu do ćwiczenia innych rzeczy,
jeśli tylko mają parowalną relację - na przykład terminologii
medycznej czy prawniczej. Na screenshotach widać przykład z różnymi
stanami USA i ich stolicami.

KWordQuiz zawiera także funkcje Flashcard (pokazywania kart), testu
wielokrotnego wyboru oraz pytań i odpowiedzi. Pytania i odpowiedzi
mają także specjalny tryb wypełniania luk.

%package libextdate
Summary:	Extensive date support library in KDE
Summary(pl.UTF-8):	Biblioteka rozszerzonej obsługi dat w KDE
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libextdate
This library consists of a group of classes which allow KDE
applications to access calendar dates outside of the limited range of
years imposed by QDate.

The QDate class has a limited range of valid dates. It does not
recognize dates prior to 14 Oct 1752 (when the Gregorian calendar was
adopted by England), nor dates after 31 Dec 8000. Both of these limits
are arbitrary.

%description libextdate -l pl.UTF-8
Ta biblioteka zawiera grupę klas pozwalających aplikacjom KDE na
dostęp do dat spoza zakresu lat narzuconego przez QDate.

Klasa QDate ma ograniczony zakres dopuszczalnych dat. Nie rozpoznaje
dat wcześniejszych niż 14 października 1752 (kiedy w Anglii
zaadoptowano kalendarz gregoriański) ani późniejszych niż 31 grudnia
8000. Oba te limity są samowolne.

%package libkdeeducore
Summary:	KDE educational module core library
Summary(pl.UTF-8):	Podstawowa biblioteka modułu edukacyjnego KDE
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeedu-flashkard

%description libkdeeducore
The core library for education applications in KDE.

%description libkdeeducore -l pl.UTF-8
Podstawowa biblioteka z funkcjami wykorzystywanymi przez aplikacje
edukacyjne w KDE.

%package libkdeeduplot
Summary:	A KDE library for plotting
Summary(pl.UTF-8):	Biblioteka KDE do rysowania wykresów
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkdeeduplot
Library with plotting functions for KDE educational applications.

%description libkdeeduplot -l pl.UTF-8
Biblioteka z funkcjami do rysowania wykresów, wykorzystywanymi przez
aplikacje edukacyjne w KDE.

%package libkdeeduui
Summary:	A userf interface library for KDE educational module
Summary(pl.UTF-8):	Biblioteka interfejsu użytkownika dla modułu edukacyjnego KDE
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkdeeduui
A library with user interface functions for KDE educational
applications.

%description libkdeeduui -l pl.UTF-8
Biblioteka z funkcjami interfejsu użytkownika, wykorzystywanymi przez
aplikacje edukacyjne w KDE.

%package libkiten
Summary:	Kiten library
Summary(pl.UTF-8):	Biblioteka Kiten
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkiten
Kiten library.

%description libkiten -l pl.UTF-8
Biblioteka Kiten.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Education;Science;Chemistry;/' \
./kalzium/src/kalzium.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Education;Languages;/' \
./kvoctrain/kvoctrain/kvoctrain.desktop \
./kverbos/kverbos/kverbos.desktop \
./kiten/kiten.desktop \
./klettres/klettres/klettres.desktop \
./klatin/klatin/klatin.desktop \
./khangman/khangman/khangman.desktop \
./kwordquiz/src/kwordquiz.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Education;Teaching;/' \
./keduca/resources/keduca.desktop \
./keduca/resources/keducabuilder.desktop

for f in `find . -name *.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
cp /usr/share/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir} \
	--enable-kig-python-scripting \
	--enable-kig-compressed-files

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps

mv $RPM_BUILD_ROOT%{_iconsdir}/locolor/16x16/actions/edit_{add,remove}.png \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions

# applnk is obsolete, isn't it?
rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk

%find_lang blinken	--with-kde
%find_lang kanagram	--with-kde
%find_lang kgeography	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   libextdate	-p /sbin/ldconfig
%postun libextdate	-p /sbin/ldconfig

%post	libkdeeducore 	-p /sbin/ldconfig
%postun	libkdeeducore	-p /sbin/ldconfig

%post	libkdeeduplot	-p /sbin/ldconfig
%postun	libkdeeduplot	-p /sbin/ldconfig

%post	libkdeeduui	-p /sbin/ldconfig
%postun	libkdeeduui	-p /sbin/ldconfig

%post	libkiten	-p /sbin/ldconfig
%postun	libkiten	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libextdate.so
%attr(755,root,root) %{_libdir}/libkdeeducore.so
%attr(755,root,root) %{_libdir}/libkdeeduplot.so
%attr(755,root,root) %{_libdir}/libkdeeduui.so
%attr(755,root,root) %{_libdir}/libkiten.so
%{_includedir}/libkdeedu
%{_includedir}/libkiten
%{_includedir}/*.h

%files blinken -f blinken.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blinken
%{_desktopdir}/kde/blinken.desktop
%{_datadir}/apps/blinken
%{_datadir}/config.kcfg/blinken.kcfg
%{_iconsdir}/[!l]*/*/*/blinken.*

%files kalzium
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_datadir}/config.kcfg/kalzium.kcfg
%{_desktopdir}/kde/kalzium.desktop
%{_iconsdir}/[!l]*/*/apps/kalzium*
#%{_mandir}/man1/kalzium.1*
%{_kdedocdir}/en/kalzium

%files kanagram -f kanagram.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kanagram
%{_datadir}/config.kcfg/kanagram.kcfg
%{_datadir}/apps/kanagram
%{_desktopdir}/kde/kanagram.desktop
%{_iconsdir}/[!l]*/*/*/kanagram.*

%files kbruch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_datadir}/config.kcfg/kbruch.kcfg
%{_desktopdir}/kde/kbruch.desktop
%{_iconsdir}/[!l]*/*/*/kbruch*
%{_kdedocdir}/en/kbruch

%files keduca
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%attr(755,root,root) %{_bindir}/keducabuilder
%{_libdir}/kde3/libkeducapart.la
%attr(755,root,root) %{_libdir}/kde3/libkeducapart.so
%{_datadir}/apps/keduca
%{_datadir}/config.kcfg/keduca.kcfg
%{_datadir}/mimelnk/application/x-edu.desktop
%{_datadir}/mimelnk/application/x-edugallery.desktop
%{_datadir}/services/keduca_part.desktop
%{_desktopdir}/kde/keduca*.desktop
%{_iconsdir}/*/*/apps/keduca.png
%{_kdedocdir}/en/keduca

%files kgeography -f kgeography.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeography
%{_datadir}/config.kcfg/kgeography.kcfg
%{_desktopdir}/kde/kgeography.desktop
%{_datadir}/apps/kgeography
%{_iconsdir}/[!l]*/*/*/kgeography.*

%files khangman
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_datadir}/config/khangmanrc
%{_datadir}/config.kcfg/khangman.kcfg
%{_desktopdir}/kde/khangman.desktop
%{_iconsdir}/[!l]*/*/apps/khangman*
%{_kdedocdir}/en/khangman

%files kig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kig
%attr(755,root,root) %{_bindir}/pykig.py
%{_libdir}/kde3/libkigpart.la
%attr(755,root,root) %{_libdir}/kde3/libkigpart.so
%{_libdir}/kde3/kfile_drgeo.la
%attr(755,root,root) %{_libdir}/kde3/kfile_drgeo.so
%{_libdir}/kde3/kfile_kig.la
%attr(755,root,root) %{_libdir}/kde3/kfile_kig.so
%{_datadir}/apps/kig*
#%{_datadir}/apps/katepart/syntax/python-kig.xml
%{_datadir}/config/magic/cabri.magic
%{_datadir}/config/magic/drgeo.magic
%{_datadir}/mimelnk/application/x-kgeo.desktop
%{_datadir}/mimelnk/application/x-kig.desktop
%{_datadir}/mimelnk/application/x-kseg.desktop
%{_datadir}/mimelnk/application/x-cabri.desktop
%{_datadir}/mimelnk/application/x-drgeo.desktop
%{_datadir}/services/kig_part.desktop
%{_datadir}/services/kfile_drgeo.desktop
%{_datadir}/services/kfile_kig.desktop
%{_desktopdir}/kde/kig.desktop
%{_iconsdir}/[!l]*/*/apps/kig*
%{_iconsdir}/crystalsvg/*/mimetypes/kig_doc.*
%{_kdedocdir}/en/kig

%files kiten
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
%{_datadir}/apps/kiten
%{_datadir}/config.kcfg/kiten.kcfg
%{_desktopdir}/kde/kiten.desktop
%{_iconsdir}/*/*/actions/kanjidic.png
%{_iconsdir}/*/*/actions/edit_*.png
%{_iconsdir}/*/*/apps/kiten*
%{_kdedocdir}/en/kiten

%files klatin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klatin
%{_datadir}/config.kcfg/klatin.kcfg
%{_datadir}/apps/klatin
%{_desktopdir}/kde/klatin.desktop
%{_kdedocdir}/en/klatin
%{_iconsdir}/*/*/apps/klatin*

%files klettres
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_datadir}/config/klettresrc
%{_datadir}/config.kcfg/klettres.kcfg
%{_desktopdir}/kde/klettres.desktop
%{_iconsdir}/[!l]*/*/*/klettres*
%{_kdedocdir}/en/klettres

%if 0
%files kmessedwords
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_datadir}/config.kcfg/kmessedwords.kcfg
%{_desktopdir}/kde/kmessedwords.desktop
%{_iconsdir}/[!l]*/*/apps/kmessedwords*
%{_kdedocdir}/en/kmessedwords
%endif

%files kmplot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_libdir}/kde3/libkmplotpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmplotpart.so
%{_datadir}/apps/kmplot
%{_datadir}/config.kcfg/kmplot.kcfg
%{_desktopdir}/kde/kmplot.desktop
%{_datadir}/mimelnk/application/x-kmplot.desktop
%{_datadir}/services/kmplot_part.desktop
%{_iconsdir}/[!l]*/*/apps/kmplot*
%{_kdedocdir}/en/kmplot

%files kpercentage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_desktopdir}/kde/kpercentage.desktop
%{_iconsdir}/[!l]*/*/apps/kpercentage*
%{_kdedocdir}/en/kpercentage

%files kstars
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fliccd
%attr(755,root,root) %{_bindir}/v4ldriver
%attr(755,root,root) %{_bindir}/v4lphilips
%attr(755,root,root) %{_bindir}/celestrongps
%attr(755,root,root) %{_bindir}/indiserver
%attr(755,root,root) %{_bindir}/kstars
%attr(755,root,root) %{_bindir}/lx200*
%attr(755,root,root) %{_bindir}/temma
%attr(755,root,root) %{_bindir}/apmount
%attr(755,root,root) %{_bindir}/apogee_ppi
%attr(755,root,root) %{_bindir}/fliwheel
%attr(755,root,root) %{_bindir}/meade_lpi
%attr(755,root,root) %{_bindir}/sbigccd
%attr(755,root,root) %{_bindir}/skycommander
%{_datadir}/apps/kstars
%{_datadir}/config/kstarsrc
%{_datadir}/config.kcfg/kstars.kcfg
%{_desktopdir}/kde/kstars.desktop
%{_iconsdir}/[!l]*/*/apps/kstars*
%{_kdedocdir}/en/kstars

%files ktouch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_datadir}/config.kcfg/ktouch.kcfg
%{_desktopdir}/kde/ktouch.desktop
%{_iconsdir}/*/*/apps/ktouch*
%{_kdedocdir}/en/ktouch

%files kturtle
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kturtle
%{_datadir}/apps/kturtle
%{_datadir}/apps/katepart/syntax/logohighlightstyle*
%{_datadir}/config.kcfg/kturtle.kcfg
%{_desktopdir}/kde/kturtle.desktop
%{_kdedocdir}/en/kturtle
%{_iconsdir}/*/*/apps/kturtle*

%files kverbos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kverbos
%{_datadir}/apps/kverbos
%{_datadir}/config.kcfg/kverbos.kcfg
%{_desktopdir}/kde/kverbos.desktop
%{_iconsdir}/*/*/actions/kverbosuser.png
%{_iconsdir}/*/*/apps/kverbos*
%{_kdedocdir}/en/kverbos

%files kvoctrain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%attr(755,root,root) %{_libdir}/libkvoctraincore.so.*
%{_libdir}/libkvoctraincore.la
%{_datadir}/apps/kvoctrain
%{_datadir}/config.kcfg/kvoctrain.kcfg
%{_datadir}/config.kcfg/languagesettings.kcfg
%{_datadir}/config.kcfg/presettings.kcfg
%{_datadir}/config/kvoctrainrc
%{_desktopdir}/kde/kvoctrain.desktop
%{_iconsdir}/*/*/apps/kvoctrain*
%{_kdedocdir}/en/kvoctrain
%{_datadir}/mimelnk/text/x-kvtml.desktop

%files kwordquiz
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwordquiz
%{_datadir}/apps/kwordquiz
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_desktopdir}/kde/kwordquiz.desktop
%{_kdedocdir}/en/kwordquiz
%{_iconsdir}/[!l]*/*/*/kwordquiz*
%{_datadir}/mimelnk/application/x-kwordquiz.desktop
%{_datadir}/config/kwordquizrc

%files libextdate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/test_extdate
%attr(755,root,root) %{_bindir}/test_extdatepicker
%{_libdir}/libextdate.la
%attr(755,root,root) %{_libdir}/libextdate.so.1.2.0

%files libkdeeducore
%defattr(644,root,root,755)
%{_libdir}/libkdeeducore.la
%attr(755,root,root) %{_libdir}/libkdeeducore.so.*.*.*

%files libkdeeduplot
%defattr(644,root,root,755)
%{_libdir}/libkdeeduplot.la
%attr(755,root,root) %{_libdir}/libkdeeduplot.so.*.*.*

%files libkdeeduui
%defattr(644,root,root,755)
%{_libdir}/libkdeeduui.la
%attr(755,root,root) %{_libdir}/libkdeeduui.so.*.*.*

%files libkiten
%defattr(644,root,root,755)
%{_libdir}/libkiten.la
%attr(755,root,root) %{_libdir}/libkiten.so.*.*.*

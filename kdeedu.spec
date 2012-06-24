#
%define		_state		stable
%define		_ver		3.2.3

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	%{_ver}
Release:	3
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	1c41b731f26269fdb39f2c097a95dd9a
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
Icon:		kde-edu.xpm
#Patch100:	%{name}-branch.diff
Patch0:		%{name}-vcategories.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - edutainment.

%description -l pl
K Desktop Environment - edukacja i rozrywka.

%package devel
Summary:	Header files for kdeedu libraries
Summary(pl):	Pliki nag��wkowe bibliotek kdeedu
Group:		X11/Development/Libraries
Requires:	%{name}-libkdeeducore = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduui = %{epoch}:%{version}-%{release}

%description devel
Header files for kdeedu libraries.

%description devel -l pl
Pliki nag��wkowe bibliotek kdeedu.

%package flashkard
Summary:	Flash card learning tool for KDE
Summary(pl):	Narz�dzie do nauki za pomoc� pokazywania kart
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkdeeducore = %{epoch}:%{version}-%{release}
Obsoletes:	kdeedu

%description flashkard
Flash card learning tool for KDE. FlashKard is based on a rather old
learning method used to teach children facts. The teacher presented a
number of cards with questions on them, and the pupil wrote the
answers on the back of the cards. These cards were then checked at the
end of the round by the teacher. The cards with the correct answers
were then removed from the pile and the incorrectly-answered questions
were repeated over and over again, until the answer was "drilled" into
the pupils memory.

%description flashkard -l pl
Narz�dzie dla KDE do nauki za pomoc� pokazywania kart. FlashKard jest
oparty na raczej starej metodzie nauczania dzieci fakt�w. Nauczyciel
pokazywa� zestaw kart z pytaniami, a ucze� pisa� odpowiedzi na
odwrocie tych kart. Karty by�y potem sprawdzane na ko�cu rundy przez
nauczyciela. Karty z poprawnymi odpowiedziami by�y usuwane z puli,
a pytania, na kt�re pad�y z�e odpowiedzi, by�y powtarzane a� do
wt�oczenia odpowiedzi do pami�ci uczni�w.

%package kalzium
Summary:	A Periodic System of Elements database
Summary(pl):	Baza danych Uk�adu Okresowego Pierwiastk�w
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Obsoletes:	kdeedu

%description kalzium
A Periodic System of Elements database. Kalzium provides you with all
kind of information about the PSE (Periodic System of Elements.) You
can lookup lots of information about the elements and also use
visualizations to show them.

%description kalzium -l pl
Baza danych Uk�adu Okresowego Pierwiastk�w. Kalzium dostarcza wszelkie
informacje dotycz�ce UOP, pozwala wyszukiwa� informacje o
pierwiastkach oraz wizualizowa� je.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl):	Generator zada� z obliczeniami na u�amkach
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kbruch
KBruch is a small program to generate tasks with fractions. The user
has to solve the given task by entering the right value for numerator
and denominator. The program checks the input and gives feedback. The
task generation can be adjusted by using different parameters. The
user can decide if he wants to solve tasks with addition/subtraction
and/or multiplication/division.

%description kbruch -l pl
Generator zada� z obliczeniami na u�amkach. KBruch to ma�y program do
generowania zada� z u�amkami. U�ytkownik ma rozwi�za� zadanie poprzez
wpisanie poprawnej warto�ci dla licznika i mianownika. Nast�pnie
program sprwdza poprawno�� danych. Generowanie zada� mo�na
dostosowywa� przy pomocy r�nych parametr�w. U�ytkownik mo�e
decydowa�, czy chce rozwi�zywa� zadania z dodawaniem/odejmowaniem
i/lub mno�eniem/dzieleniem.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie test�w i egzamin�w
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description keduca
Application for creating and revising of form-based tests and exams.

%description keduca -l pl
Aplikacja do tworzenia i sprawdzania test�w i egzamin�w opartych na
formularzach.

%package khangman
Summary:	A hangman game
Summary(pl):	Gra w wisielca
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkdeeducore = %{epoch}:%{version}-%{release}
Obsoletes:	kdeedu

%description khangman
KHangMan is a game based on the well known hangman game. A word is
picked in random, the letters are hidden, you must guess the word by
trying a letter after another. Each time you guess a wrong letter, a
picture of a hangman is drawn. You must guess the word before getting
hanged! It is aimed for children aged 6+.

%description khangman -l pl
KHangMan jest gr� opart� na popularnej grze w wisielca. Wybierane jest
losowe s�owo, kt�rego litery s� ukryte. Trzeba zgadn�� to s�owo
podaj�c kolejno litery. Za ka�dym razem, gdy podana litera nie
wyst�puje w s�owie, rysowany jest obrazek wisielca. Trzeba odgadn��
s�owo przed powieszeniem! Gra jest przeznaczona dla dzieci w wieku 6
lat lub wi�cej.

%package kig
Summary:	Interactive Geometry
Summary(pl):	Interaktywna geometria
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kig
Kig is an application for Interactive Geometry. It's intended to serve
two purposes:
- allow students to interactively explore mathematical figures and
  concepts using the computer.
- serve as a WYSIWYG tool for drawing mathematical figures and
  including them in other documents.

%description kig -l pl
Kig to aplikacja do interaktywnej geometrii. Ma s�u�y� dw�m celom:
- umo�liwi� uczniom interaktywnie przegl�danie figur i poj��
  matematycznych przy u�yciu komputera
- s�u�y� jako narz�dzie WISIWYG do rysowania figur matematycznych i
  w��czania ich do innych dokument�w.

%package kiten
Summary:	A Japanese reference tool
Summary(pl):	S�ownik angielsko-japo�ski
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kiten
Kiten is an application with multiple functions. Firstly, it is a
convenient English to Japanese and Japanese to English dictionary;
secondly, it is a Kanji dictionary, with multiple ways to look up
specific characters; thirdly, it is a tool to help you learn Kanji.

%description kiten -l pl
Kiten to aplikacja o wielu funkcjach. Po pierwsze, jest wygodnym
s�ownikiem angielsko-japo�skim i japo�sko-angielskim; po drugie,
jest s�ownikiem Kanji z wieloma sposobami wyszukiwania okre�lonych
znak�w; po trzecie, jest narz�dziem pomagaj�cym w nauce Kanji.

%package klettres
Summary:	Helps child to learn alphabet and to read some syllables
Summary(pl):	Pomoc w nauce alfabetu i sylab dla dzieci
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
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

%description klettres -l pl
KLettres to bardzo prosta aplikacja pomagaj�ca dzieciom i doros�ym w
nauce alfabetu i g�osek we w�asnym lub obcym j�zyku. Program losuje
liter� lub sylab�, a nast�pnie wy�wietla j� i odgrywa d�wi�k.
U�ytkownik powinien nast�pnie wpisa� t� liter� lub sylab�. Do �wicze�
s�u�� poziomy, gdzie litera/sylaba nie jest wy�wietlana, jedynie
d�wi�k jest odgrywany. U�ytkownik nie musi wiedzie�, jak u�ywa� myszy,
wymagana jest tylko klawiatura.

Aktualnie dost�pne jest pi�� j�zyk�w: czeski, du�ski, holenderski,
francuski i s�owacki.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl):	Rysowanie wykres�w funkcji matematycznych
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kmplot
KmPlot is a mathematical function plotter for the KDE Desktop. It has
a powerful built-in parser. You can plot different functions
simultaneously and combine them to build new functions.

%description kmplot -l pl
KmPlot to narz�dzie do rysowania wykres�w funkcji matematycznych dla
�rodowiska KDE. Ma wbudowany pot�ny parser. Mo�na rysowa� r�ne
funkcje jednocze�nie i ��czy� je, aby stworzy� nowe funkcje.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta �amig��wka
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kmessedwords
KMessedWords is the game, that is based on the word/letter puzzles
that I have played as a child. It is a very simple constructed game,
with 3 difficulty levels of play, and each level deserves it's value.
It is fully customizable game, that allows you to write in your own
words, and set your own "look and feel" of the game. It is aimed for
children aged 10+, because of the difficulty, but, everyone is welcome
to try. A word is picked in random, and displayed out in the messed
order, with difficulty dependant on the chosen level. You have
unlimited numbers of attempts, and the scores are kept.

%description kmessedwords -l pl
KMessedWords to gra oparta na �amig��wce s�owno-literowej, w kt�r�
autor gra� jako dziecko. Jest to bardzo prosto skonstruowana gra z
trzema poziomami trudno�ci gry, a ka�dy poziom zas�uguje na swoj�
warto��. Jest to w pe�ni dostosowywalna gra, pozwalaj�ca na wpisywanie
w�asnych s��w i ustawianie w�asnego "look and feel". Grup� docelow� s�
dzieci w wieku od 10 lat ze wzgl�du na trudno��, ale ka�dy mo�e
spr�bowa�. S�owa s� wybierane losowo i wy�wietlane w pomieszanej
kolejno�ci, z trudno�ci� zale�n� od wybranego poziomu. Liczba pr�b nie
jest ograniczona, a wyniki s� zachowywane.

%package kpercentage
Summary:	A percentage tutor
Summary(pl):	Program do nauki procent�w
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kpercentage
A percentage tutor.

%description kpercentage -l pl
Program do nauki procent�w.

%package kstars
Summary:	Desktop planetarium
Summary(pl):	Planetarium
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
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

%description kstars -l pl
KStars pozwala przegl�da� nocne niebo z wygod� krzes�a przy
komputerze. Dostarcza dok�adn� graficzn� reprezentacj� nocnego nieba
dla dowolnej daty, z dowolnego miejsca na Ziemi. Obraz zawiera 126000
gwiazd do 9. wielko�ci (znacznie poza ograniczeniem go�ego oka), 13000
obiekt�w (katalogi Messiera, NGC i IC), wszystkie planety, S�o�ce i
Ksi�yc, setki komet i asteroid, Drog� Mleczn�, 88 konstelacji oraz
linie prowadz�ce takie jak r�wnik astronomiczny, horyzont i ekliptyk�.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl):	Program do nauki maszynopisania
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description ktouch
KTouch is a program for learning to touch type. It provides you with
text to train on, and adjust to different levels, depending on how
good you are. It can display which key to press next, and the correct
finger to use. It's the perfect touch typing tutor, you learn typing
with all the fingers without looking at the keys, in an step by step
way. It is convenient for all ages, and the perfect typing tutor for
schools, universities and individuals.

%description ktouch -l pl
KTouch to program do nauki maszynopisania. Dostarcza tekst do �wicze�,
dostosowany do r�nych poziom�w, zale�nie od stopnia zaawansowania.
Mo�e wy�wietla�, kt�ry klawisz trzeba nacisn��, i kt�rego palca nale�y
u�y�. Jest �wietnym programem do nauki maszynopisania, uczy pisa�
wszystkimi palcami bez patrzenia na klawisze, krok po kroku. Jest
wygodny w ka�dym wieku, jest �wietny dla szk�, uniwersytet�w i
jednostek.

%package kverbos
Summary:	Spanish verb form study application for KDE
Summary(pl):	Program do nauki form czasownik�w w j�zyku hiszpa�skim
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kverbos
Spanish verb form study application for KDE.

%description kverbos -l pl
Program do nauki form czasownik�w w j�zyku hiszpa�skim.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl):	Program do �wiczenia s�ownictwa
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do �wiczenia s�ownictwa.

%package libkdeeducore
Summary:	kdeeducore library
Summary(pl):	Biblioteka kdeeducore
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdeedu-flashkard < 8:3.1.93.031105-1

%description libkdeeducore
kdeeducore shared library.

%description libkdeeducore -l pl
Biblioteka wsp�dzielona kdeeducore.

%package libkdeeduplot
Summary:	kdeeduplot library
Summary(pl):	Biblioteka kdeeduplot
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkdeeduplot
kdeeduplot shared library.

%description libkdeeduplot -l pl
Biblioteka wsp�dzielona kdeeduplot.

%package libkdeeduui
Summary:	kdeeduui library
Summary(pl):	Biblioteka kdeeduui
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkdeeduui
kdeeduui shared library.

%description libkdeeduui -l pl
Biblioteka wsp�dzielona kdeeduui.

%prep
%setup -q
#patch100 -p1
%patch0 -p1

for f in `find . -name *.desktop | xargs grep -l '^Terminal=0'`; do
	%{__sed} -i -e 's/^Terminal=0/Terminal=false/' $f
done
for f in `find . -name *.desktop | xargs grep -l '^Type=Application'`; do
	if ! grep '^Encoding=' $f >/dev/null; then
		%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' $f
	fi
done

%build
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps

mv $RPM_BUILD_ROOT%{_iconsdir}/locolor/16x16/actions/edit_{add,remove}.png \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkdeeducore 	-p /sbin/ldconfig
%postun	libkdeeducore	-p /sbin/ldconfig

%post	libkdeeduplot	-p /sbin/ldconfig
%postun	libkdeeduplot	-p /sbin/ldconfig

%post	libkdeeduui	-p /sbin/ldconfig
%postun	libkdeeduui	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libkdeeducore.so
%attr(755,root,root) %{_libdir}/libkdeeduplot.so
%attr(755,root,root) %{_libdir}/libkdeeduui.so
%{_includedir}/*.h

%files flashkard
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashkard
%{_datadir}/apps/flashkard
%{_desktopdir}/kde/flashkard.desktop
%{_iconsdir}/*/*/apps/flashkard.png
%{_mandir}/man1/flashkard.1*
%{_kdedocdir}/en/flashkard

%files kalzium
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_desktopdir}/kde/kalzium.desktop
%{_iconsdir}/[!l]*/*/apps/kalzium.png
%{_mandir}/man1/kalzium.1*
%{_kdedocdir}/en/kalzium

%files kbruch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_desktopdir}/kde/kbruch.desktop
%{_iconsdir}/[!l]*/*/apps/kbruch.png
%{_kdedocdir}/en/kbruch

%files keduca
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%attr(755,root,root) %{_bindir}/keducabuilder
%{_datadir}/apps/keduca
%{_datadir}/mimelnk/application/x-edu.desktop
%{_datadir}/mimelnk/application/x-edugallery.desktop
%{_desktopdir}/kde/keduca*.desktop
%{_iconsdir}/*/*/apps/keduca.png
%{_mandir}/man1/keduca.1*
%{_kdedocdir}/en/keduca

%files khangman
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_desktopdir}/kde/khangman.desktop
%{_iconsdir}/[!l]*/*/apps/khangman.png
%{_mandir}/man1/khangman.1*
%{_kdedocdir}/en/khangman
#%%{_iconsdir}/hicolor/48x48/apps/a_acute.png
#%%{_iconsdir}/hicolor/48x48/apps/a_circle.png
#%%{_iconsdir}/hicolor/48x48/apps/a_grave.png
#%%{_iconsdir}/hicolor/48x48/apps/a_tilde.png
#%%{_iconsdir}/hicolor/48x48/apps/a_umlaut.png
#%%{_iconsdir}/hicolor/48x48/apps/a_withe.png
#%%{_iconsdir}/hicolor/48x48/apps/c_cedil.png
#%%{_iconsdir}/hicolor/48x48/apps/e_acute.png
#%%{_iconsdir}/hicolor/48x48/apps/e_circ.png
#%%{_iconsdir}/hicolor/48x48/apps/e_grave.png
#%%{_iconsdir}/hicolor/48x48/apps/i_acute.png
#%%{_iconsdir}/hicolor/48x48/apps/i_grave.png
#%%{_iconsdir}/hicolor/48x48/apps/n_tilde.png
#%%{_iconsdir}/hicolor/48x48/apps/o_acute.png
#%%{_iconsdir}/hicolor/48x48/apps/o_circ.png
#%%{_iconsdir}/hicolor/48x48/apps/o_cross.png
#%%{_iconsdir}/hicolor/48x48/apps/o_grave.png
#%%{_iconsdir}/hicolor/48x48/apps/o_tilde.png
#%%{_iconsdir}/hicolor/48x48/apps/o_umlaut.png
#%%{_iconsdir}/hicolor/48x48/apps/sz_lig.png
#%%{_iconsdir}/hicolor/48x48/apps/u_acute.png
#%%{_iconsdir}/hicolor/48x48/apps/u_umlaut.png

%files kig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kig
%{_libdir}/kde3/libkigpart.la
%attr(755,root,root) %{_libdir}/kde3/libkigpart.so
%{_datadir}/apps/kig*
%{_datadir}/mimelnk/application/x-kgeo.desktop
%{_datadir}/mimelnk/application/x-kig.desktop
%{_datadir}/mimelnk/application/x-kseg.desktop
%{_datadir}/services/kig_part.desktop
%{_desktopdir}/kde/kig.desktop
%{_iconsdir}/[!l]*/*/apps/kig.png
%{_kdedocdir}/en/kig

%files kiten
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
%{_datadir}/apps/kiten
%{_desktopdir}/kde/kiten.desktop
%{_iconsdir}/*/*/actions/kanjidic.png
%{_iconsdir}/*/*/actions/edit_*.png
%{_iconsdir}/*/*/apps/kiten.png
%{_mandir}/man1/kiten.1*
%{_mandir}/man1/kitengen.1*
%{_kdedocdir}/en/kiten

%files klettres
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_datadir}/config.kcfg/klettres.kcfg
%{_desktopdir}/kde/klettres.desktop
%{_iconsdir}/[!l]*/*/*/klettres*
%{_iconsdir}/*/*/apps/grownup.png
%{_iconsdir}/*/*/apps/kids.png
%{_iconsdir}/*/*/apps/menubar.png
%{_mandir}/man1/klettres.1*
%{_kdedocdir}/en/klettres

%files kmessedwords
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_desktopdir}/kde/kmessedwords.desktop
%{_iconsdir}/[!l]*/*/apps/kmessedwords.png
%{_mandir}/man1/kmessedwords.1*
%{_kdedocdir}/en/kmessedwords

%files kmplot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_datadir}/apps/kmplot
%{_desktopdir}/kde/kmplot.desktop
%{_iconsdir}/[!l]*/*/apps/kmplot.png
%{_mandir}/man1/kmplot.1*
%{_kdedocdir}/en/kmplot

%files kpercentage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_desktopdir}/kde/kpercentage.desktop
%{_iconsdir}/[!l]*/*/apps/kpercentage.png
%{_mandir}/man1/kpercentage.1*
%{_kdedocdir}/en/kpercentage

%files kstars
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/celestrongps
%attr(755,root,root) %{_bindir}/indiserver
%attr(755,root,root) %{_bindir}/kstars
%attr(755,root,root) %{_bindir}/lx200generic
%{_datadir}/apps/kstars
%{_desktopdir}/kde/kstars.desktop
%{_iconsdir}/[!l]*/*/apps/kstars.png
%{_mandir}/man1/kstars.1*
%{_kdedocdir}/en/kstars

%files ktouch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_desktopdir}/kde/ktouch.desktop
%{_iconsdir}/*/*/apps/ktouch.png
%{_mandir}/man1/ktouch.1*
%{_kdedocdir}/en/ktouch

%files kverbos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kverbos
%{_datadir}/apps/kverbos
%{_desktopdir}/kde/kverbos.desktop
%{_iconsdir}/*/*/actions/kverbosuser.png
%{_iconsdir}/*/*/apps/kverbos.png
%{_mandir}/man1/kverbos.1*
%{_kdedocdir}/en/kverbos

%files kvoctrain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_desktopdir}/kde/kvoctrain.desktop
%{_iconsdir}/*/*/apps/kvoctrain.png
%{_mandir}/man1/kvoctrain.1*
%{_mandir}/man1/langen2kvtml.1*
%{_mandir}/man1/spotlight2kvtml.1*
%{_kdedocdir}/en/kvoctrain

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
%{_iconsdir}/*/*/apps/edu_*.*

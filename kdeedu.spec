%define		_state		stable
%define		_ver		3.3.0

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	%{_ver}
Release:	0.1
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/3.3/src/%{name}-%{version}.tar.bz2
# Source0-md5:	1c41b731f26269fdb39f2c097a95dd9a
Icon:		kde-edu.xpm
#Patch100:	%{name}-branch.diff
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - edutainment.

%description -l pl
K Desktop Environment - edukacja i rozrywka.

%package devel
Summary:	Header files for kdeedu libraries
Summary(pl):	Pliki nag³ówkowe bibliotek kdeedu
Group:		X11/Development/Libraries
Requires:	%{name}-libkdeeducore = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduui = %{epoch}:%{version}-%{release}

%description devel
Header files for kdeedu libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek kdeedu.

%package flashkard
Summary:	Flash card learning tool for KDE
Summary(pl):	Narzêdzie do nauki za pomoc± pokazywania kart
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
Narzêdzie dla KDE do nauki za pomoc± pokazywania kart. FlashKard jest
oparty na raczej starej metodzie nauczania dzieci faktów. Nauczyciel
pokazywa³ zestaw kart z pytaniami, a uczeñ pisa³ odpowiedzi na
odwrocie tych kart. Karty by³y potem sprawdzane na koñcu rundy przez
nauczyciela. Karty z poprawnymi odpowiedziami by³y usuwane z puli, a
pytania, na które pad³y z³e odpowiedzi, by³y powtarzane a¿ do
wt³oczenia odpowiedzi do pamiêci uczniów.

%package kalzium
Summary:	A Periodic System of Elements database
Summary(pl):	Baza danych Uk³adu Okresowego Pierwiastków
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
Baza danych Uk³adu Okresowego Pierwiastków. Kalzium dostarcza wszelkie
informacje dotycz±ce UOP, informacje o pierwiastkach oraz ich
wizualizacje.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl):	Generator zadañ z obliczeniami na u³amkach
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
Generator zadañ z obliczeniami na u³amkach. KBruch to ma³y program do
generowania zadañ z u³amkami. U¿ytkownik ma rozwi±zaæ zadanie poprzez
wpisanie poprawnej warto¶ci dla licznika i mianownika. Nastêpnie
program sprawdza poprawno¶æ danych. Generowanie zadañ mo¿na
dostosowywaæ przy pomocy ró¿nych parametrów. U¿ytkownik mo¿e
decydowaæ, czy chce rozwi±zywaæ zadania z dodawaniem/odejmowaniem
i/lub mno¿eniem/dzieleniem.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie testów i egzaminów
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description keduca
Application for creating and revising of form-based tests and exams.

%description keduca -l pl
Aplikacja do tworzenia i sprawdzania testów i egzaminów opartych na
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
KHangMan jest gr± opart± na popularnej grze w wisielca. Wybierane jest
losowe s³owo, którego litery s± ukryte. Trzeba zgadn±æ to s³owo
podaj±c kolejno litery. Za ka¿dym razem, gdy podana litera nie
wystêpuje w s³owie, rysowany jest obrazek wisielca. Trzeba odgadn±æ
s³owo przed powieszeniem! Gra jest przeznaczona dla dzieci w wieku 6
lat lub wiêcej.

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
Kig to aplikacja do interaktywnej geometrii. Ma s³u¿yæ dwóm celom:
- umo¿liwiæ uczniom interaktywnie przegl±danie figur i pojêæ
  matematycznych przy u¿yciu komputera
- s³u¿yæ jako narzêdzie WISIWYG do rysowania figur matematycznych i
  w³±czania ich do innych dokumentów.

%package klatin
Summary:	KLatin is a program to help revise latin
Summary(pl):	Klatin s³u¿y do powtarzania ³aciny
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
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

%description klatin -l pl
KLatin to program pomagaj±cy przy powtarzaniu ³aciny. S± w nim trzy
"sekcje", w których mo¿na æwiczyæ ró¿ne aspekty jêzyka. S± to:
s³ownictwo, gramatyka i sprawdzanie czasowników. Ponadto jest zbiór
uwag przydatnych przy samodzielnym powtarzaniu.

W sekcji s³ownictwa wczytywany jest plik XML zawieraj±cy ró¿ne s³owa i
ich t³umaczenia na jêzyk lokalny. KLatin zadaje pytania o znaczenie
ka¿dego z tych s³ów z odpowiedzi± w formie wielokrotnego wyboru.

W sekcjach gramatyki i czasowników KLatin pyta o konkretn± formê
rzeczownika lub czasownika, tak± jak "narzêdnik liczby pojedynczej"
czy "pierwsza osoba liczby mnogiej trybu oznajmuj±cego w stronie
biernej" i odpowiada siê bez wielokrotnego wyboru.

%package kiten
Summary:	A Japanese reference tool
Summary(pl):	S³ownik angielsko-japoñski
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
s³ownikiem angielsko-japoñskim i japoñsko-angielskim; po drugie, jest
s³ownikiem Kanji z wieloma sposobami wyszukiwania okre¶lonych znaków;
po trzecie, jest narzêdziem pomagaj±cym w nauce Kanji.

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
KLettres to bardzo prosta aplikacja pomagaj±ca dzieciom i doros³ym w
nauce alfabetu i g³osek we w³asnym lub obcym jêzyku. Program losuje
literê lub sylabê, a nastêpnie wy¶wietla j± i odgrywa d¼wiêk.
U¿ytkownik powinien nastêpnie wpisaæ tê literê lub sylabê. Do æwiczeñ
s³u¿± poziomy, gdzie litera/sylaba nie jest wy¶wietlana, jedynie
d¼wiêk jest odgrywany. U¿ytkownik nie musi wiedzieæ, jak u¿ywaæ myszy,
wymagana jest tylko klawiatura.

Aktualnie dostêpne jest piêæ jêzyków: czeski, duñski, holenderski,
francuski i s³owacki.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl):	Rysowanie wykresów funkcji matematycznych
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kmplot
KmPlot is a mathematical function plotter for the KDE Desktop. It has
a powerful built-in parser. You can plot different functions
simultaneously and combine them to build new functions.

%description kmplot -l pl
KmPlot to narzêdzie do rysowania wykresów funkcji matematycznych dla
¶rodowiska KDE. Ma wbudowany potê¿ny parser. Mo¿na rysowaæ ró¿ne
funkcje jednocze¶nie i ³±czyæ je, aby stworzyæ nowe funkcje.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta ³amig³ówka
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
KMessedWords to gra oparta na ³amig³ówce s³owno-literowej, w któr±
autor gra³ jako dziecko. Jest to bardzo prosto skonstruowana gra z
trzema poziomami trudno¶ci gry, a ka¿dy poziom zas³uguje na swoj±
warto¶æ. Jest to w pe³ni dostosowywalna gra, pozwalaj±ca na wpisywanie
w³asnych s³ów i ustawianie w³asnego "look and feel". Grup± docelow± s±
dzieci w wieku od 10 lat ze wzglêdu na trudno¶æ, ale ka¿dy mo¿e
spróbowaæ. S³owa s± wybierane losowo i wy¶wietlane w pomieszanej
kolejno¶ci, z trudno¶ci± zale¿n± od wybranego poziomu. Liczba prób nie
jest ograniczona, a wyniki s± zachowywane.

%package kpercentage
Summary:	A percentage tutor
Summary(pl):	Program do nauki procentów
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kpercentage
A percentage tutor.

%description kpercentage -l pl
Program do nauki procentów.

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
KStars pozwala przegl±daæ nocne niebo z wygod± krzes³a przy
komputerze. Dostarcza dok³adn± graficzn± reprezentacjê nocnego nieba
dla dowolnej daty, z dowolnego miejsca na Ziemi. Obraz zawiera 126000
gwiazd do 9. wielko¶ci (znacznie poza ograniczeniem go³ego oka), 13000
obiektów (katalogi Messiera, NGC i IC), wszystkie planety, S³oñce i
Ksiê¿yc, setki komet i asteroid, Drogê Mleczn±, 88 konstelacji oraz
linie prowadz±ce takie jak równik astronomiczny, horyzont i ekliptykê.

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
KTouch to program do nauki maszynopisania. Dostarcza tekst do æwiczeñ,
dostosowany do ró¿nych poziomów, zale¿nie od stopnia zaawansowania.
Mo¿e wy¶wietlaæ, który klawisz trzeba nacisn±æ, i którego palca nale¿y
u¿yæ. Jest ¶wietnym programem do nauki maszynopisania, uczy pisaæ
wszystkimi palcami bez patrzenia na klawisze, krok po kroku. Jest
wygodny w ka¿dym wieku, jest ¶wietny dla szkó³, uniwersytetów i
jednostek.

%package kturtle
Summary:	A Logo interpreter for KDE
Summary(pl):	Interpreter jêzyka Logo dla KDE
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kturtle
KTurtle is a Logo programming language interpreter for KDE. The Logo
programming language is very easy and thus it can be used by young
children. A unique quality of Logo is that the commands or
instructions can be translated (please see the tranlation how to if
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
- translation of the Logo commands (among others in : Dutch, French
  German, Latin and Swedish)
- context help for each Logo command

#description kturtle -l pl #likewise

%package kverbos
Summary:	Spanish verb form study application for KDE
Summary(pl):	Program do nauki form czasowników w jêzyku hiszpañskim
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kverbos
Spanish verb form study application for KDE.

%description kverbos -l pl
Program do nauki form czasowników w jêzyku hiszpañskim.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl):	Program do æwiczenia s³ownictwa
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do æwiczenia s³ownictwa.

%package kwordquiz
Summary:	A flashcard and vocabulary learning program
Summary(pl):	Program do æwiczenia s³ownictwa za pomoc± pokazywania kart
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

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

#description kvoctrain -l pl


%package libkdeeducore
Summary:	KDE educational module core library
Summary(pl):	Podstawowa biblioteka modu³u edukacyjnego KDE
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdeedu-flashkard < 8:3.1.93.031105-1

%description libkdeeducore
The core library for education applications in KDE.

%description libkdeeducore -l pl
Podstawowa biblioteka z funkcjami wykorzystywanymi przez aplikacje
edukacyjne w KDE.

%package libkdeeduplot
Summary:	A KDE library for plotting
Summary(pl):	Biblioteka KDE do rysowania wykresów
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkdeeduplot
Library with plotting functions for KDE educational applications.

%description libkdeeduplot -l pl
Biblioteka z funkcjami do rysowania wykresów, wykorzystywanymi przez
aplikacje edukacyjne w KDE.

%package libextdate
Summary:	Extensive date support library in KDE
Summary(pl):	Biblioteka rozszerzonej obs³ugi dat w KDE
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libextdate
This library consists of a group of classes which allow KDE
applications to access calendar dates outside of the limited range of
years imposed by QDate.

The QDate class has a limited range of valid dates. It does not
recognize dates prior to 14 Oct 1752 (when the Gregorian calendar was
adopted by England), nor dates after 31 Dec 8000. Both of these limits
are arbitrary.

%description libextdate -l pl
Ta biblioteka zawiera grupê klas pozwalaj±cych aplikacjom KDE na
dostêp do dat spoza zakresu lat narzuconego przez QDate.

Klasa QDate ma ograniczony zakres dopuszczalnych dat. Nie rozpoznaje
dat wcze¶niejszych ni¿ 14 pa¼dziernika 1752 (kiedy w Anglii
zaadoptowano kalendarz gregoriañski) ani pó¼niejszych ni¿ 31 grudnia
8000. Oba te limity s± samowolne.

%package libkdeeduui
Summary:	A userf interface library for KDE educational module
Summary(pl):	Biblioteka interfejsu u¿ytkownika dla modu³u edukacyjnego KDE
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkdeeduui
A library with user interface functions for KDE educational
applications.

%description libkdeeduui -l pl
Biblioteka z funkcjami interfejsu u¿ytkownika, wykorzystywanymi przez
aplikacje edukacyjne w KDE.

%prep
%setup -q
#patch100 -p1

for f in `find . -name *.desktop | xargs grep -l '^Terminal=0'`; do
	%{__sed} -i -e 's/^Terminal=0/Terminal=false/' $f
done
for f in `find . -name *.desktop | xargs grep -l '^Type=Application'`; do
	if ! grep '^Encoding=' $f >/dev/null; then
		%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' $f
	fi
done

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Education;Science;Chemistry;/' \
./kalzium/src/kalzium.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Education;Languages;/' \
./kvoctrain/kvoctrain/kvoctrain.desktop \
./kverbos/kverbos/kverbos.desktop \
./kiten/kiten.desktop \
./klettres/klettres/klettres.desktop \
./klatin/klatin/klatin.desktop \
./kmessedwords/kmessedwords/kmessedwords.desktop \
./khangman/khangman/khangman.desktop \
./kwordquiz/src/kwordquiz.desktop

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Education;Teaching;/' \
./keduca/resources/keduca.desktop \
./keduca/resources/keducabuilder.desktop

%{__sed} -i -e 's,appsdir =,#,g' \
	-e "s,apps_DATA,xdg_apps_DATA,g"  Makefile.am

%build
cp %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

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

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Edutainment/Miscellaneous/kwordquiz.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkdeeducore 	-p /sbin/ldconfig
%postun	libkdeeducore	-p /sbin/ldconfig

%post	libkdeeduplot	-p /sbin/ldconfig
%postun	libkdeeduplot	-p /sbin/ldconfig

%post	libkdeeduui	-p /sbin/ldconfig
%postun	libkdeeduui	-p /sbin/ldconfig

%post   libextdate	-p /sbin/ldconfig
%postun libextdate	-p /sbin/ldconfig


%files devel
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libkdeeducore.so
%attr(755,root,root) %{_libdir}/libkdeeduplot.so
%attr(755,root,root) %{_libdir}/libkdeeduui.so
%{_includedir}/*.h

#files flashkard
#defattr(644,root,root,755)
#attr(755,root,root) %{_bindir}/flashkard
#{_datadir}/apps/flashkard
#{_desktopdir}/kde/flashkard.desktop
#{_iconsdir}/*/*/apps/flashkard.png
#{_mandir}/man1/flashkard.1*
#{_kdedocdir}/en/flashkard

%files kalzium
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_datadir}/config.kcfg/kalzium.kcfg
%{_desktopdir}/kde/kalzium.desktop
%{_iconsdir}/[!l]*/*/apps/kalzium*
%{_mandir}/man1/kalzium.1*
%{_kdedocdir}/en/kalzium

%files kbruch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_datadir}/config.kcfg/kbruch.kcfg
%{_desktopdir}/kde/kbruch.desktop
%{_iconsdir}/[!l]*/*/*/kbruch*
%{_kdedocdir}/en/kbruch
%{_mandir}/man1/kbruch.1*

%files keduca
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%attr(755,root,root) %{_bindir}/keducabuilder
%{_datadir}/apps/keduca
%{_datadir}/mimelnk/application/x-edu.desktop
%{_datadir}/mimelnk/application/x-edugallery.desktop
%{_desktopdir}/kde/keduca*.desktop
%{_iconsdir}/*/*/apps/keduca.png
%{_mandir}/man1/keduca*.1*
%{_kdedocdir}/en/keduca

%files khangman
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_datadir}/config/khangmanrc
%{_datadir}/config.kcfg/khangman.kcfg
%{_desktopdir}/kde/khangman.desktop
%{_iconsdir}/[!l]*/*/apps/khangman*
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
%{_libdir}/kde3/kfile_drgeo.la
%attr(755,root,root) %{_libdir}/kde3/kfile_drgeo.so
%{_libdir}/kde3/kfile_kig.la
%attr(755,root,root) %{_libdir}/kde3/kfile_kig.so
%{_datadir}/apps/kig*
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
%{_kdedocdir}/en/kig
%{_mandir}/man1/kig.1*

%files kiten
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
%{_datadir}/apps/kiten
%{_desktopdir}/kde/kiten.desktop
%{_iconsdir}/*/*/actions/kanjidic.png
%{_iconsdir}/*/*/actions/edit_*.png
%{_iconsdir}/*/*/apps/kiten*
%{_mandir}/man1/kiten.1*
%{_mandir}/man1/kitengen.1*
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
%{_iconsdir}/[!l]*/*/apps/kmessedwords*
%{_mandir}/man1/kmessedwords.1*
%{_kdedocdir}/en/kmessedwords

%files kmplot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_datadir}/apps/kmplot
%{_datadir}/config.kcfg/kmplot.kcfg
%{_desktopdir}/kde/kmplot.desktop
%{_datadir}/mimelnk/application/x-kmplot.desktop
%{_iconsdir}/[!l]*/*/apps/kmplot*
%{_mandir}/man1/kmplot.1*
%{_kdedocdir}/en/kmplot

%files kpercentage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_desktopdir}/kde/kpercentage.desktop
%{_iconsdir}/[!l]*/*/apps/kpercentage*
%{_mandir}/man1/kpercentage.1*
%{_kdedocdir}/en/kpercentage

%files kstars
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fliccd
%attr(755,root,root) %{_bindir}/v4ldriver
%attr(755,root,root) %{_bindir}/v4lphilips
%attr(755,root,root) %{_bindir}/celestrongps
%attr(755,root,root) %{_bindir}/indiserver
%attr(755,root,root) %{_bindir}/kstars
%attr(755,root,root) %{_bindir}/lx200generic
%{_datadir}/apps/kstars
%{_datadir}/config/kstarsrc
%{_datadir}/config.kcfg/kstars.kcfg
%{_desktopdir}/kde/kstars.desktop
%{_iconsdir}/[!l]*/*/apps/kstars*
%{_mandir}/man1/kstars.1*
%{_mandir}/man1/celestrongps.1*
%{_mandir}/man1/indiserver.1*
%{_mandir}/man1/lx200_16.1*
%{_mandir}/man1/lx200autostar.1*
%{_mandir}/man1/lx200classic.1*
%{_mandir}/man1/lx200generic.1*
%{_mandir}/man1/lx200gps.1*
%{_kdedocdir}/en/kstars

%files ktouch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_desktopdir}/kde/ktouch.desktop
%{_iconsdir}/*/*/apps/ktouch*
%{_mandir}/man1/ktouch.1*
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
%{_mandir}/man1/kverbos.1*
%{_kdedocdir}/en/kverbos

%files kvoctrain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_datadir}/config.kcfg/kvoctrain.kcfg
%{_desktopdir}/kde/kvoctrain.desktop
%{_iconsdir}/*/*/apps/kvoctrain*
%{_mandir}/man1/kvoctrain.1*
%{_mandir}/man1/langen2kvtml.1*
%{_mandir}/man1/spotlight2kvtml.1*
%{_kdedocdir}/en/kvoctrain

%files kwordquiz
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwordquiz
%{_datadir}/apps/kwordquiz
%{_desktopdir}/kde/kwordquiz.desktop
%{_kdedocdir}/en/kwordquiz
%{_iconsdir}/[!l]*/*/*/kwordquiz*
%{_datadir}/mimelnk/application/x-kwordquiz.desktop

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

%files libextdate
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/test_extdate
%attr(755,root,root) %{_bindir}/test_extdatepicker
%attr(755,root,root) %{_libdir}/libextdate.so.1.2.0
%{_libdir}/libextdate.la

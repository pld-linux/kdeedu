#
%define		_state		stable
%define		_ver		3.2.3

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	%{_ver}
Release:	0.1
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	97174178360396ea50e69097979b8319
Icon:		kde-edu.xpm
Patch0:		%{name}-vcategories.patch
BuildRequires:	autoconf
BuildRequires:	unsermake >= 040511
BuildRequires:	automake
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	rpmbuild(macros) >= 1.129
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
Summary(pl):	Narzêdzie do nauki za pomoc± liczmanów
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
Narzêdzie do nauki za pomoc± liczmanów.

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
Baza danych Uk³adu Okresowego Pierwiastków.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl):	Generator zadañ z obliczeniami na u³amkach
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kbruch
Task generator for calculations with fractions. KBruch is a small
program to generate tasks with fractions. The user has to solve the
given task by entering the right value for numerator and denominator.
The program checks the input and gives feedback. The task generation
can be adjusted by using different parameters. The user can decide if
he wants to solve tasks with addition/subtraction and/or
multiplication/division.

%description kbruch -l pl
Generator zadañ z obliczeniami na u³amkach.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie testów i egzaminów
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description keduca
Application for creating and revising of form-based tests and exams.

%description keduca -l pl
Tworzenie i sprawdzanie testów i egzaminów.

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
Interaktywna geometria.

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
S³ownik angielsko-japoñski.

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
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl):	Koordynograf
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kmplot
KmPlot is a mathematical function plotter for the KDE Desktop. It has
a powerful built-in parser. You can plot different functions
simultaneously and combine them to build new functions.

%description kmplot -l pl
Koordynograf.

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
Prosta ³amig³ówka.

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

Desktop planetarium.

%description kstars -l pl
Planetarium.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl):	Program do nauki maszynopisania
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description ktouch
KTouch is a program for learning to touch type.

KTouch provides you with text to train on, and adjust to different
levels, depending on how good you are. It can display which key to
press next, and the correct finger to use. It's the perfect touch
typing tutor, you learn typing with all the fingers without looking at
the keys, in an step by step way. It is convenient for all ages, and
the perfect typing tutor for schools, universities and individuals.

%description ktouch -l pl
Program do nauki maszynopisania.

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

%package libkdeeducore
Summary:	kdeeducore library
Summary(pl):	Biblioteka kdeeducore
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdeedu-flashkard < 8:3.1.93.031105-1

%description libkdeeducore
kdeeducore shared library.

%description libkdeeducore -l pl
Biblioteka wspó³dzielona kdeeducore.

%package libkdeeduplot
Summary:	kdeeduplot library
Summary(pl):	Biblioteka kdeeduplot
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkdeeduplot
kdeeduplot shared library.

%description libkdeeduplot -l pl
Biblioteka wspó³dzielona kdeeduplot.

%package libkdeeduui
Summary:	kdeeduui library
Summary(pl):	Biblioteka kdeeduui
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkdeeduui
kdeeduui shared library.

%description libkdeeduui -l pl
Biblioteka wspó³dzielona kdeeduui.



%prep
%setup -q
%patch0 -p1

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

%files flashkard -f
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

%bcond_without  i18n    # dont build i18n subpackage

%define		_state		stable
%define		_ver		3.2.0
##%define		_snap		040110

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	a0a59713a19fb01dd62b13b92f222d08
%if %{with i18n}
Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	df911c323c20896db68a4bfc38ca8821
%endif
Patch0:		%{name}-vcategories.patch
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
Flash card learning tool for KDE.

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
A Periodic System of Elements database.

%description kalzium -l pl
Baza danych Uk³adu Okresowego Pierwiastków.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl):	Generator zadañ z obliczeniami na u³amkach
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kbruch
Task generator for calculations with fractions.

%description kbruch -l pl
Generator zadañ z obliczeniami na u³amkach.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie testów i egzaminów
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description keduca
Creation and revision of form-based tests and exams.

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
KHangMan jest gr± opart± na popularnej grze w wisielca. Wybierane
jest losowe s³owo, którego litery s± ukryte. Trzeba zgadn±æ to s³owo
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
Interactive Geometry.

%description kig -l pl
Interaktywna geometria.

%package kiten
Summary:	A Japanese reference tool
Summary(pl):	S³ownik angielsko-japoñski
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kiten
A Japanese reference tool.

%description kiten -l pl
S³ownik angielsko-japoñski.

%package klettres
Summary:	Helps child to learn French alphabet and to read some syllables
Summary(pl):	Pomoc w nauce francuskiego alfabetu i sylab dla dzieci
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description klettres
Helps child to learn French alphabet and to read some syllables.

%description klettres -l pl
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl):	Koordynograf
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kmplot
Mathematical function plotter.

%description kmplot -l pl
Koordynograf.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta ³amig³ówka
Group:		X11/Applications/Science
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdeedu

%description kmessedwords
Simple mind-training game.

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
Program for learning touch typing.

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

%package flashkard-i18n
Summary:	Internationalization and localization files for flashkard
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla flashkard
Group:	X11/Applications
Requires:	%{name}-flashkard = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description flashkard-i18n
Internationalization and localization files for flashkard.

%description -l pl flashkard-i18n
Pliki umiêdzynarodawiaj±ce dla flashkard.

%package kalzium-i18n
Summary:	Internationalization and localization files for kalzium
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kalzium
Group:	X11/Applications
Requires:	%{name}-kalzium = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kalzium-i18n
Internationalization and localization files for kalzium.

%description -l pl kalzium-i18n
Pliki umiêdzynarodawiaj±ce dla kalzium.

%package kbruch-i18n
Summary:	Internationalization and localization files for kbruch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kbruch
Group:	X11/Applications
Requires:	%{name}-kbruch = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kbruch-i18n
Internationalization and localization files for kbruch.

%description -l pl kbruch-i18n
Pliki umiêdzynarodawiaj±ce dla kbruch.

%package keduca-i18n
Summary:	Internationalization and localization files for keduca
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla keduca
Group:	X11/Applications
Requires:	%{name}-keduca = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description keduca-i18n
Internationalization and localization files for keduca.

%description -l pl keduca-i18n
Pliki umiêdzynarodawiaj±ce dla keduca.

%package khangman-i18n
Summary:	Internationalization and localization files for khangman
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khangman
Group:	X11/Applications
Requires:	%{name}-khangman = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description khangman-i18n
Internationalization and localization files for khangman.

%description -l pl khangman-i18n
Pliki umiêdzynarodawiaj±ce dla khangman.

%package kig-i18n
Summary:	Internationalization and localization files for kig
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kig
Group:	X11/Applications
Requires:	%{name}-kig = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kig-i18n
Internationalization and localization files for kig.

%description -l pl kig-i18n
Pliki umiêdzynarodawiaj±ce dla kig.

%package kiten-i18n
Summary:	Internationalization and localization files for kiten
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kiten
Group:	X11/Applications
Requires:	%{name}-kiten = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kiten-i18n
Internationalization and localization files for kiten.

%description -l pl kiten-i18n
Pliki umiêdzynarodawiaj±ce dla kiten.

%package klettres-i18n
Summary:	Internationalization and localization files for klettres
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klettres
Group:	X11/Applications
Requires:	%{name}-klettres = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description klettres-i18n
Internationalization and localization files for klettres.

%description -l pl klettres-i18n
Pliki umiêdzynarodawiaj±ce dla klettres.

%package kmessedwords-i18n
Summary:	Internationalization and localization files for kmessedwords
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmessedwords
Group:	X11/Applications
Requires:	%{name}-kmessedwords = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kmessedwords-i18n
Internationalization and localization files for kmessedwords.

%description -l pl kmessedwords-i18n
Pliki umiêdzynarodawiaj±ce dla kmessedwords.

%package kmplot-i18n
Summary:	Internationalization and localization files for kmplot
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmplot
Group:	X11/Applications
Requires:	%{name}-kmplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kmplot-i18n
Internationalization and localization files for kmplot.

%description -l pl kmplot-i18n
Pliki umiêdzynarodawiaj±ce dla kmplot.

%package kpercentage-i18n
Summary:	Internationalization and localization files for kpercentage
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kpercentage
Group:	X11/Applications
Requires:	%{name}-kpercentage = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kpercentage-i18n
Internationalization and localization files for kpercentage.

%description -l pl kpercentage-i18n
Pliki umiêdzynarodawiaj±ce dla kpercentage.

%package kstars-i18n
Summary:	Internationalization and localization files for kstars
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kstars
Group:	X11/Applications
Requires:	%{name}-kstars = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kstars-i18n
Internationalization and localization files for kstars.

%description -l pl kstars-i18n
Pliki umiêdzynarodawiaj±ce dla kstars.

%package ktouch-i18n
Summary:	Internationalization and localization files for ktouch
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktouch
Group:	X11/Applications
Requires:	%{name}-ktouch = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ktouch-i18n
Internationalization and localization files for ktouch.

%description -l pl ktouch-i18n
Pliki umiêdzynarodawiaj±ce dla ktouch.

%package kverbos-i18n
Summary:	Internationalization and localization files for kverbos
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kverbos
Group:	X11/Applications
Requires:	%{name}-kverbos = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kverbos-i18n
Internationalization and localization files for kverbos.

%description -l pl kverbos-i18n
Pliki umiêdzynarodawiaj±ce dla kverbos.

%package kvoctrain-i18n
Summary:	Internationalization and localization files for kvoctrain
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kvoctrain
Group:	X11/Applications
Requires:	%{name}-kvoctrain = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kvoctrain-i18n
Internationalization and localization files for kvoctrain.

%description -l pl kvoctrain-i18n
Pliki umiêdzynarodawiaj±ce dla kvoctrain.

%package i18n
Summary:	Common internationalization and localization files for kdeedu
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdeedu
Group:	X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdeedu.

%description -l pl i18n
Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdeedu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
        bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
		rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

install -d \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps

mv $RPM_BUILD_ROOT%{_iconsdir}/locolor/16x16/actions/edit_{add,remove}.png \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/actions

%find_lang flashkard	--with-kde
%find_lang kalzium	--with-kde
%find_lang kbruch	--with-kde
%find_lang keduca	--with-kde
%find_lang khangman	--with-kde
%find_lang kig		--with-kde
%find_lang kiten	--with-kde
%find_lang klettres	--with-kde
%find_lang kmathtool	--with-kde
%find_lang kmessedwords	--with-kde
%find_lang kmplot	--with-kde
%find_lang kpercentage	--with-kde
%find_lang kstars	--with-kde
%find_lang ktouch	--with-kde
%find_lang kverbos	--with-kde
%find_lang kvoctrain	--with-kde

%if %{with i18n}
%find_lang desktop_kdeedu	--with-kde
%endif

files="flashkard \
kalzium \
kbruch \
keduca \
khangman \
kig	 \
kiten \
klettres \
kmathtool \
kmessedwords \
kmplot \
kpercentage \
kstars \
ktouch \
kverbos \
kvoctrain"

for i in $files; do
        echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkdeeducore 	-p /sbin/ldconfig
%postun	libkdeeducore	-p /sbin/ldconfig

%post	libkdeeduplot	-p /sbin/ldconfig
%postun	libkdeeduplot	-p /sbin/ldconfig

%post	libkdeeduui	-p /sbin/ldconfig
%postun	libkdeeduui	-p /sbin/ldconfig

%if %{with i18n}
%files flashkard-i18n -f flashkard.lang
%files kalzium-i18n -f kalzium.lang
%files kbruch-i18n -f kbruch.lang
%files keduca-i18n -f keduca.lang
%files khangman-i18n -f khangman.lang
%files kig-i18n -f kig.lang
%files kiten-i18n -f kiten.lang
%files klettres-i18n -f klettres.lang
%files kmessedwords-i18n -f kmessedwords.lang
%files kmplot-i18n -f kmplot.lang
%files kpercentage-i18n -f kpercentage.lang
%files kstars-i18n -f kstars.lang
%files ktouch-i18n -f ktouch.lang
%files kverbos-i18n -f kverbos.lang
%files kvoctrain-i18n -f kvoctrain.lang
%files i18n -f desktop_kdeedu.lang
%endif

%files devel
%defattr(644,root,root,755)
%doc README
%{_includedir}/*
%{_libdir}/libkdeeducore.so
%{_libdir}/libkdeeduplot.so
%{_libdir}/libkdeeduui.so

%files flashkard -f flashkard_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashkard
%{_datadir}/apps/flashkard
%{_desktopdir}/kde/flashkard.desktop
%{_iconsdir}/*/*/apps/flashkard.png

%files kalzium -f kalzium_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_desktopdir}/kde/kalzium.desktop
%{_iconsdir}/[!l]*/*/apps/kalzium.png

%files kbruch -f kbruch_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_desktopdir}/kde/kbruch.desktop
%{_iconsdir}/[!l]*/*/apps/kbruch.png

%files keduca -f keduca_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%attr(755,root,root) %{_bindir}/keducabuilder
%{_datadir}/apps/keduca
%{_datadir}/mimelnk/application/x-edu.desktop
%{_datadir}/mimelnk/application/x-edugallery.desktop
%{_desktopdir}/kde/keduca*.desktop
%{_iconsdir}/*/*/apps/keduca.png

%files khangman -f khangman_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_desktopdir}/kde/khangman.desktop
%{_iconsdir}/[!l]*/*/apps/khangman.png

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

%files kig -f kig_en.lang
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

%files kiten -f kiten_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
%{_datadir}/apps/kiten
%{_desktopdir}/kde/kiten.desktop
%{_iconsdir}/*/*/actions/kanjidic.png
%{_iconsdir}/*/*/actions/edit_*.png
%{_iconsdir}/*/*/apps/kiten.png

%files klettres -f klettres_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_datadir}/config.kcfg/klettres.kcfg
%{_desktopdir}/kde/klettres.desktop
%{_iconsdir}/[!l]*/*/*/klettres*
%{_iconsdir}/*/*/apps/grownup.png
%{_iconsdir}/*/*/apps/kids.png
%{_iconsdir}/*/*/apps/menubar.png

%files kmessedwords -f kmessedwords_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_desktopdir}/kde/kmessedwords.desktop
%{_iconsdir}/[!l]*/*/apps/kmessedwords.png

%files kmplot -f kmplot_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_datadir}/apps/kmplot
%{_desktopdir}/kde/kmplot.desktop
%{_iconsdir}/[!l]*/*/apps/kmplot.png

%files kpercentage -f kpercentage_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_desktopdir}/kde/kpercentage.desktop
%{_iconsdir}/[!l]*/*/apps/kpercentage.png

%files kstars -f kstars_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/celestrongps
%attr(755,root,root) %{_bindir}/indiserver
%attr(755,root,root) %{_bindir}/kstars
%attr(755,root,root) %{_bindir}/lx200generic
%{_datadir}/apps/kstars
%{_desktopdir}/kde/kstars.desktop
%{_iconsdir}/[!l]*/*/apps/kstars.png

%files ktouch -f ktouch_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_desktopdir}/kde/ktouch.desktop
%{_iconsdir}/*/*/apps/ktouch.png

%files kverbos -f kverbos_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kverbos
%{_datadir}/apps/kverbos
%{_desktopdir}/kde/kverbos.desktop
%{_iconsdir}/*/*/actions/kverbosuser.png
%{_iconsdir}/*/*/apps/kverbos.png

%files kvoctrain -f kvoctrain_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_desktopdir}/kde/kvoctrain.desktop
%{_iconsdir}/*/*/apps/kvoctrain.png

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

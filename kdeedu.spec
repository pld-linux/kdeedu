
%define		_state		snapshots
%define		_ver		3.1.90
%define		_snap		030726

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	fefe2fef3443afca62ad458121bf802d
Patch0:		%{name}-vcategories.patch
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML
%define		_icondir	%{_datadir}/icons

%define		no_install_post_chrpath		1

%description
K Desktop Environment - edutainment.

%description -l pl
K Desktop Environment - edukacja i rozrywka.

%package devel
Summary:	Header Files
Summary(pl):	Pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name}-flashkard = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdeeduui = %{epoch}:%{version}-%{release}

%description devel
Header Files

%description devel -l pl
Pliki nag��wkowe

%package flashkard
Summary:	Flash card learning tool for KDE
Summary(pl):    Narz�dzie do nauki za pomoc� liczman�w
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}

%description flashkard
Flash card learning tool for KDE.

%description flashkard -l pl
Narz�dzie do nauki za pomoc� liczman�w.

%package kalzium
Summary:        A Periodic System of Elements database
Summary(pl):    Baza danych Uk�adu Okresowego Pierwiastk�w
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}

%description kalzium
A Periodic System of Elements database.

%description kalzium -l pl
Baza danych Uk�adu Okresowego Pierwiastk�w.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl):	Generator zada� z obliczeniami na u�amkach
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description kbruch
Task generator for calculations with fractions.

%description kbruch -l pl
Generator zada� z obliczeniami na u�amkach.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie test�w i egzamin�w
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}

%description keduca
Creation and revision of form-based tests and exams.

%description keduca -l pl
Tworzenie i sprawdzanie test�w i egzamin�w.

%package khangman
Summary:	A hangman game
Summary(pl):	Gra w wisielca
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description khangman
KHangMan is a game based on the well known hangman game. A word is
picked in random, the letters are hidden, you must guess the word by
trying a letter afteranother. Each time you guess a wrong letter, a
picture of a hangman is drawn. You must guess the word before getting
hanged! It is aimed for children aged 6+.

%description khangman -l pl
KHangMan jest gr� opart� na popularnej grze w wisielca. Wybierane
jest losowe s�owo, kt�rego litery s� ukryte. Trzeba zgadna� to s�owo
podaj�c kolejno litery. Za ka�dym razem, gdy podana litera nie
wyst�puje w s�owie, rysowany jest obrazek wisielca. Trzeba odgadn��
s�owo przed powieszeniem! Gra jest przeznaczona dla dzieci w wieku 6
lat lub wi�cej.

%package kig
Summary:        Interactive Geometry
Summary(pl):    Interaktywna geometria
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description kig
Interactive Geometry.

%description kig -l pl
Interaktywna geometria.

%package kiten
Summary:        A Japanese reference tool
Summary(pl):    S�ownik angielsko-japo�ski
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}

%description kiten
A Japanese reference tool.

%description kiten -l pl
S�ownik angielsko-japo�ski.

%package klettres
Summary:	Helps child to learn French alphabet and to read some syllables
Summary(pl):	Pomoc w nauce francuskiego alfabetu i sylab dla dzieci
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}

%description klettres
Helps child to learn French alphabet and to read some syllables.

%description klettres -l pl
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmplot
Summary:        Mathematical function plotter
Summary(pl):    Koordynograf
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description kmplot
Mathematical function plotter.

%description kmplot -l pl
Koordynograf.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta �amig��wka
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description kmessedwords
Simple mind-training game.

%description kmessedwords -l pl
Prosta �amig��wka.

%package kpercentage
Summary:        A percentage tutor
Summary(pl):    Program do nauki procent�w
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description kpercentage
A percentage tutor.

%description kpercentage -l pl
Program do nauki procent�w.

%package kstars
Summary:	Desktop planetarium
Summary(pl):	Planetarium
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{version}
Requires:	%{name}-libkdeeduplot = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}

%description kstars
Desktop planetarium.

%description kstars -l pl
Planetarium.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl):	Program do nauki maszynopisania
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}


%description ktouch
Program for learning touch typing.

%description ktouch -l pl
Program do nauki maszynopisania.

%package kverbos
Summary:	Spanish verb form study application for KDE
Summary(pl):	Program do nauki form czasownik�w w j�zyku hiszpa�skim
Group:          X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:	%{name}

%description kverbos
Spanish verb form study application for KDE.

%description kverbos -l pl
Program do nauki form czasownik�w w j�zyku hiszpa�skim.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl):	Program do �wiczenia s�ownictwa
Group:		X11/Applications/Science
Requires:	kdebase-core >= %{version}
Obsoletes:      %{name}

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do �wiczenia s�ownictwa.

%package libkdeeduplot
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
Requires:	kdelibs >= %{version}

%description libkdeeduplot
TODO.

%description libkdeeduplot -l pl
TODO.

%package libkdeeduui
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
Requires:	kdelibs >= %{version}

%description libkdeeduui
TODO.

%description libkdeeduui -l pl
TODO.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build

for plik in `find ./ -name *.desktop` ; do
	if [ -d $plik ]; then
		echo $plik
		sed -ie 's/\[nb\]/\[no\]/g' $plik
	fi
done

#%%{__make} -f Makefile.cvs

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Edutainment/Languages/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Edutainment/Mathematics/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Edutainment/Miscellaneous/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Edutainment/Science/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

mv $RPM_BUILD_ROOT%{_applnkdir}/Edutainment/Tools/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

cd $RPM_BUILD_ROOT%{_icondir}
mv locolor/16x16/actions/*.png crystalsvg/16x16/actions
cd -

# Bleh.. really don't wanna "make -f Makefile.cvs"
mv $RPM_BUILD_ROOT%{_icondir}/ktouch/hi16-app-ktouch.png \
	$RPM_BUILD_ROOT%{_icondir}/hicolor/16x16/apps/ktouch.png

mv $RPM_BUILD_ROOT%{_icondir}/ktouch/hi32-app-ktouch.png \
	$RPM_BUILD_ROOT%{_icondir}/hicolor/32x32/apps/ktouch.png

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	flashkard
/sbin/ldconfig

%postun	flashkard
/sbin/ldconfig

%post	libkdeeduplot
/sbin/ldconfig

%postun	libkdeeduplot
/sbin/ldconfig

%post	libkdeeduui
/sbin/ldconfig

%postun	libkdeeduui
/sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%doc README
%{_includedir}/*
%{_libdir}/libkdeeducore.so
%{_libdir}/libkdeeduplot.so
%{_libdir}/libkdeeduui.so

%files flashkard -f flashkard.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashkard
%{_libdir}/libkdeeducore.la
%attr(755,root,root) %{_libdir}/libkdeeducore.so.*.*.*
%{_datadir}/apps/flashkard
%{_desktopdir}/flashkard.desktop
%{_icondir}/*/*/apps/flashkard.png

%files kalzium -f kalzium.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_desktopdir}/kalzium.desktop
%{_icondir}/[!l]*/*/apps/kalzium.png

%files kbruch -f kbruch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_desktopdir}/kbruch.desktop
%{_icondir}/[!l]*/*/apps/kbruch.png

%files keduca -f keduca.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%attr(755,root,root) %{_bindir}/keducabuilder
%{_datadir}/apps/keduca
%{_datadir}/mimelnk/application/x-edu.desktop
%{_datadir}/mimelnk/application/x-edugallery.desktop
%{_desktopdir}/keduca*.desktop
%{_icondir}/*/*/apps/keduca.png

%files khangman -f khangman.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_desktopdir}/khangman.desktop
%{_icondir}/[!l]*/*/apps/khangman.png

%files kig -f kig.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kig
%{_libdir}/kde3/libkigpart.la
%attr(755,root,root) %{_libdir}/kde3/libkigpart.so
%{_datadir}/apps/kig*
%{_datadir}/mimelnk/application/x-kgeo.desktop
%{_datadir}/mimelnk/application/x-kig.desktop
%{_datadir}/mimelnk/application/x-kseg.desktop
%{_datadir}/services/kig_part.desktop
%{_desktopdir}/kig.desktop
%{_icondir}/[!l]*/*/apps/kig.png

%files kiten -f kiten.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
#%{_libdir}/kde3/kiten.la
#%attr(755,root,root) %{_libdir}/kde3/kiten.so
%{_datadir}/apps/kiten
%{_desktopdir}/kiten.desktop
%{_icondir}/*/*/actions/kanjidic.png
%{_icondir}/*/*/actions/edit_*.png
%{_icondir}/*/*/apps/kiten.png

%files klettres -f klettres.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_desktopdir}/klettres.desktop
%{_icondir}/[!l]*/*/*/klettres*
%{_icondir}/*/*/apps/grownup.png
%{_icondir}/*/*/apps/kids.png
%{_icondir}/*/*/apps/menubar.png

%files kmessedwords -f kmessedwords.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_desktopdir}/kmessedwords.desktop
%{_icondir}/[!l]*/*/apps/kmessedwords.png

%files kmplot -f kmplot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_datadir}/apps/kmplot
%{_desktopdir}/kmplot.desktop
%{_icondir}/[!l]*/*/apps/kmplot.png

%files kpercentage -f kpercentage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_desktopdir}/kpercentage.desktop
%{_icondir}/[!l]*/*/apps/kpercentage.png

%files kstars -f kstars.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/celestrongps
%attr(755,root,root) %{_bindir}/indiserver
%attr(755,root,root) %{_bindir}/kstars
%attr(755,root,root) %{_bindir}/lx200generic
%attr(755,root,root) %{_bindir}/wx
%{_datadir}/apps/kstars
%{_desktopdir}/kstars.desktop
%{_icondir}/[!l]*/*/apps/kstars.png

%files ktouch -f ktouch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_desktopdir}/ktouch.desktop
%{_icondir}/*/*/apps/ktouch.png

%files kverbos -f kverbos.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kverbos
%{_datadir}/apps/kverbos
%{_desktopdir}/kverbos.desktop
%{_icondir}/*/*/actions/kverbosuser.png
%{_icondir}/*/*/apps/kverbos.png

%files kvoctrain -f kvoctrain.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_desktopdir}/kvoctrain.desktop
%{_icondir}/*/*/apps/kvoctrain.png

%files libkdeeduplot
%defattr(644,root,root,755)
%{_libdir}/libkdeeduplot.la
%attr(755,root,root) %{_libdir}/libkdeeduplot.so.*.*.*

%files libkdeeduui
%defattr(644,root,root,755)
%{_libdir}/libkdeeduui.la
%attr(755,root,root) %{_libdir}/libkdeeduui.so.*.*.*

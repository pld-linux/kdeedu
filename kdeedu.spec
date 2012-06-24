
%define		_state		unstable
%define		_kdever		kde-3.1-rc5

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	3.1
Release:	1
Epoch:		7
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
#Patch0:		%{name}-DESTDIR.patch
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 	/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
K Desktop Environment - edutainment.

%description -l pl
K Desktop Environment - edukacja i rozrywka.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie test�w i egzamin�w.
Group:		X11/Applications/Science
Requires:	%{name} = %{version}

%description keduca
Creation and revision of form-based tests and exams.

%description keduca -l pl
Tworzenie i sprawdzanie test�w i egzamin�w.

%package kalzium
Summary:        A Pieriodic System of Elements database.
Summary(pl):    Baza danych Uk�adu Okresowego Pierwiastk�w.
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description kalzium
A Pieriodic System of Elements database.

%description kalzium -l pl
Baza danych Uk�adu Okresowego Pierwiastk�w.

%package flashkard
Summary:	Flash card learning tool for KDE  
Summary(pl):    Narz�dzie do nauki za pomoc� liczman�w.
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description flashkard
Flash card learning tool for KDE

%description flashkard -l pl
Narz�dzie do nauki za pomoc� liczman�w.


%package kgeo
Summary:	Interactive geometry
Summary(pl):	Interaktywna geometria
Group:		X11/Applications/Science
Requires:	%{name} = %{version}

%description kgeo
Interactive geometry.

%description kgeo -l pl
Interaktywna geometria.

%package khangman
Summary:        A hangman name.
Summary(pl):    Ko�o fortuny.
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description khangman
Hangman game. The child should guess a word letter by letter.

%description khangman -l pl
Ko�o fortuny. Zgadujemy has�a litera po literze.

%package kiten
Summary:        A Japanese reference tool.
Summary(pl):    S�ownik angielsko-japo�ski.
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description kiten
A Japanese reference tool.

%description kiten -l pl
S�ownik angielsko-japo�ski.

%package klettres
Summary:	Helps child to learn french alphabet and to read some syllables
Summary(pl):	Pomoc w nauce francuskiego alfabetu i sylab dla dzieci
Group:		X11/Applications/Science
Requires:	%{name} = %{version}

%description klettres
Helps child to learn french alphabet and to read some syllables

%description klettres -l pl
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmplot
Summary:        Mathematical function plotter
Summary(pl):    Koordynograf
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description kmplot
Mathematical function plotter

%description kmplot -l pl
Koordynograf

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta �amig��wka.
Group:		X11/Applications/Science
Requires:	%{name} = %{version}

%description kmessedwords
Simple mind-training game.

%description kmessedwords -l pl
Prosta �amig��wka.

%package kpercentage
Summary:        A percentage tutor.
Summary(pl):    Program do nauki procent�w.
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description kpercentage
A percentage tutor.

%description kpercentage -l pl
Program do nauki procent�w.

%package kstars
Summary:	Desktop planetarium
Summary(pl):	Planetarium.
Group:		X11/Applications/Science
Requires:	%{name} = %{version}

%description kstars
Desktop planetarium.

%description kstars -l pl
Planetarium.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl):	Program do nauki maszynopisania
Group:		X11/Applications/Science
Requires:	%{name} = %{version}
Provides:	ktouch
Obsoletes:	ktouch

%description ktouch
Program for learning touch typing.

%description ktouch -l pl
Program do nauki maszynopisania.

%package kverbos
Summary:	Spanish verb form study application for KDE
Summary(pl):	Program do nauki form czasownik�w w j�zyku hiszpa�skim.
Group:          X11/Applications/Science
Requires:       %{name} = %{version}

%description kverbos
Spanish verb form study application for KDE

%description kverbos -l pl
Program do nauki form czasownik�w w j�zyku hiszpa�skim.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl):	Program do �wiczenia s�ownictwa
Group:		X11/Applications/Science
Requires:	%{name} = %{version}

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do �wiczenia s�ownictwa.

%prep
%setup -q
#%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Scientific
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Chemistry
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Astronomy
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Learning
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Miscellanous
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Languages $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Languages
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Mathematics $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Mathematics
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Science/kalzium.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Chemistry/
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Science/kstars.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Astronomy/
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Tools/*.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Learning/
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Miscellanous/flashkard.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Learning/
mv $RPM_BUILD_ROOT/%{_applnkdir}/Edutainment/Miscellanous/ktouch.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Scientific/Miscellanous


#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang flashkard --with-kde
%find_lang kalzium --with-kde
%find_lang keduca --with-kde
%find_lang kgeo --with-kde
%find_lang khangman --with-kde
%find_lang klettres --with-kde
%find_lang kmessedwords --with-kde
%find_lang kmplot --with-kde
%find_lang kstars --with-kde
%find_lang ktouch --with-kde
%find_lang kverbos --with-kde
%find_lang kvoctrain --with-kde


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_datadir}/mimelnk/application/x-edu.desktop

%files flashkard -f flashkard.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashkard
%{_datadir}/apps/flashkard
%{_pixmapsdir}/*/*/*/*flashkard*
%{_applnkdir}/Scientific/Learning/flashkard.desktop

%files kalzium -f kalzium.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_pixmapsdir}/*/*/*/*kalzium*
%{_applnkdir}/Scientific/Chemistry/kalzium.desktop

%files keduca -f keduca.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%{_datadir}/apps/keduca
%{_pixmapsdir}/*/*/*/*keduca*
%{_applnkdir}/Scientific/Learning/keduca*.desktop

%files kgeo -f kgeo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeo
%{_datadir}/apps/kgeo
%{_pixmapsdir}/*/*/*/kgeo*
%{_applnkdir}/Scientific/Mathematics/kgeo.desktop

%files klettres -f klettres.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_pixmapsdir}/*/*/*/klettres*
#%{_applnkdir}/Edutainment/French/klettres.desktop

%files kmessedwords -f kmessedwords.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_pixmapsdir}/*/*/*/kmessedwords*
#%{_applnkdir}/Edutainment/kmessedwords.desktop

%files kstars -f kstars.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstars
%{_datadir}/apps/kstars
%{_pixmapsdir}/*/*/*/kstars*
#%{_applnkdir}/Edutainment/kstars.desktop

%files ktouch -f ktouch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_pixmapsdir}/*/*/*/ktouch*
#%{_applnkdir}/Edutainment/ktouch.desktop

%files kvoctrain -f kvoctrain.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_pixmapsdir}/*/*/*/kvoctrain*
%{_pixmapsdir}/kvoctrain*
#%{_applnkdir}/Edutainment/kvoctrain.desktop

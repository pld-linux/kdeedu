#
# Conditional build:
# _with_klatin        - build kdebase-klatin package
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	3.0.5a
Release:	0.2
Epoch:		7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-extra_pixmaps.tar.bz2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-klatin_and_khangman.patch
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
Summary(pl):	Tworzenie i sprawdzanie testów i egzaminów
Group:		X11/Applications
Requires:	%{name} = %{version}

%description keduca
Creation and revision of form-based tests and exams.

%description keduca -l pl
Tworzenie i sprawdzanie testów i egzaminów.

%package kgeo
Summary:	Interactive geometry
Summary(pl):	Interaktywna geometria
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kgeo
Interactive geometry.

%description kgeo -l pl
Interaktywna geometria.

%package khangman
Summary:	Hangman game
Summary(pl):	Gra w wisielca
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description khangman
KHangMan is a game based on the well known hangman game. A word is
picked in random, the letters are hidden, you must guess the word by
trying a letter afteranother. Each time you guess a wrong letter, a
picture of a hangman is drawn. You must guess the word before getting
hanged! It is aimed for children aged 6+.

%description khangman -l pl
KHangMan jest gr± opart± na popularnej grze w wisielca. Wybierane
jest losowe s³owo, którego litery s± ukryte. Trzeba zgadnaæ to s³owo
podaj±c kolejno litery. Za ka¿dym razem, gdy podana litera nie
wystêpuje w s³owie, rysowany jest obrazek wisielca. Trzeba odgadn±æ
s³owo zanim rysunek zostanie ukoñczony. Musisz odgadn±æ s³owo, zanim
ciê powiesz±! Gra jest przeznaczona dla dzieci w wieku powy¿ej 6 lat.

Zgadywane s± s³owa angielskie.

%if %{?_with_klatin:1}%{!?_with_klatin:0}
%package klatin
Summary:	Latin exercises
Summary(pl):	Æwiczenia z ³aciny
Group:		X11/Applications
Requires:	%{name} = %{version}

%description klatin
Latin exercises.

%description klatin -l pl
Æwiczenia z ³aciny.
%endif

%package klettres
Summary:	Helps child to learn French alphabet and to read some syllables
Summary(pl):	Pomoc w nauce francuskiego alfabetu i sylab dla dzieci
Group:		X11/Applications
Requires:	%{name} = %{version}

%description klettres
Helps child to learn French alphabet and to read some syllables.

%description klettres -l pl
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta ³amig³ówka
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kmessedwords
Simple mind-training game.

%description kmessedwords -l pl
Prosta ³amig³ówka.

%package kstars
Summary:	Desktop planetarium
Summary(pl):	Planetarium
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kstars
Desktop planetarium.

%description kstars -l pl
Planetarium.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl):	Program do nauki maszynopisania
Group:		X11/Applications
Requires:	%{name} = %{version}
Provides:	ktouch
Obsoletes:	ktouch

%description ktouch
Program for learning touch typing.

%description ktouch -l pl
Program do nauki maszynopisania.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl):	Program do æwiczenia s³ownictwa
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do æwiczenia s³ownictwa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#%{__make} -f Makefile.cvs
%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/*
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/kvoctrain.xpm

cat > $RPM_BUILD_ROOT%{_applnkdir}/Edutainment/French/.directory << EOF
[Desktop Entry]
Name=French
Name[pl]=Francuski
Comment=Learning French
Comment[pl]=Nauka francuskiego
Icon=package_french.png
Type=Directory
# vi: encoding=utf-8
EOF

%find_lang kgeo --with-kde
%find_lang klettres --with-kde
%find_lang kmessedwords --with-kde
%find_lang kstars --with-kde
%find_lang ktouch --with-kde
%find_lang kvoctrain --with-kde
%find_lang keduca --with-kde
%find_lang khangman --with-kde
# NWY (not working yet)
# the klatin program does not work with non-C locale set
%find_lang klatin --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files -f khangman.lang
%files
%defattr(644,root,root,755)
%doc README*
%{_datadir}/mimelnk/application/x-edu.desktop

%files keduca -f keduca.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%{_datadir}/apps/keduca
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/keduca.png}
%{_pixmapsdir}/keduca.png
%{_applnkdir}/Edutainment/keduca.desktop
%{_mandir}/man1/keduca.1

%files kgeo -f kgeo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeo
%{_datadir}/apps/kgeo
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/kgeo.png}
%{_pixmapsdir}/kgeo.png
%{_applnkdir}/Edutainment/kgeo.desktop
%{_mandir}/man1/kgeo.1

%files khangman -f khangman.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{?_with_pixmapsubdirs:%{_pixmapsdir}/locolor/*x*/apps/khangman.png}
%{_pixmapsdir}/khangman.png
%{_applnkdir}/Edutainment/khangman.desktop

%if %{?_with_klatin:1}%{!?_with_klatin:0}
%files klatin -f klatin.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klatin
%{_datadir}/apps/klatin
%{?_with_pixmapsubdirs:%{_pixmapsdir}/locolor/*x*/apps/klatin.png}
#%{_pixmapsdir}/klatin.png
%{_applnkdir}/Edutainment/klatin.desktop
%endif

%files klettres -f klettres.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/klettres*.png}
%{_pixmapsdir}/klettres.png
%{_pixmapsdir}/package_french.png
%{_applnkdir}/Edutainment/French
%{_mandir}/man1/klettres.1

%files kmessedwords -f kmessedwords.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/kmessedwords.png}
%{_pixmapsdir}/kmessedwords.png
%{_applnkdir}/Edutainment/kmessedwords.desktop
%{_mandir}/man1/kmessedwords.1

%files kstars -f kstars.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstars
%{_datadir}/apps/kstars
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/kstars.png}
%{_pixmapsdir}/kstars.png
%{_applnkdir}/Edutainment/kstars.desktop
%{_mandir}/man1/kstars.1

%files ktouch -f ktouch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ktouch.png}
%{_pixmapsdir}/ktouch.png
%{_applnkdir}/Edutainment/ktouch.desktop
%{_mandir}/man1/ktouch.1

%files kvoctrain -f kvoctrain.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
#%{_pixmapsdir}/*/*/*/kvoctrain*
%{_pixmapsdir}/kvoctrain*
%{_applnkdir}/Edutainment/kvoctrain.desktop
%{_mandir}/man1/kvoctrain.1

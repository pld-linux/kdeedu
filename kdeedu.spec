
%define		_state		stable
%define		_ver		3.1.4

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e710e5840b2f33e9c96b9b49d3914d5b
# generated from kde-i18n
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	aec4b56099e3cf364731fb83eca9c98f
Source2:	%{name}-extra_icons.tar.bz2
# Source2-md5:	26cab4490d7800c69a6a224b949a8369
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel = %{epoch}:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Requires:	kdebase-core >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

%description
K Desktop Environment - edutainment.

%description -l pl
K Desktop Environment - edukacja i rozrywka.

%package devel
Summary:	Header Files
Summary(pl):	Pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header Files

%description devel -l pl
Pliki nag��wkowe

%package flashkard
Summary:	Flash card learning tool for KDE
Summary(pl):	Narz�dzie do nauki za pomoc� liczman�w
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description flashkard
Flash card learning tool for KDE.

%description flashkard -l pl
Narz�dzie do nauki za pomoc� liczman�w.

%package keduca
Summary:	Creation and revision of form-based tests and exams
Summary(pl):	Tworzenie i sprawdzanie test�w i egzamin�w
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description keduca
Creation and revision of form-based tests and exams.

%description keduca -l pl
Tworzenie i sprawdzanie test�w i egzamin�w.

%package kalzium
Summary:	A Periodic System of Elements database
Summary(pl):	Baza danych Uk�adu Okresowego Pierwiastk�w
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kalzium
A Periodic System of Elements database.

%description kalzium -l pl
Baza danych Uk�adu Okresowego Pierwiastk�w.

%package kgeo
Summary:	Interactive geometry
Summary(pl):	Interaktywna geometria
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kgeo
Interactive geometry.

%description kgeo -l pl
Interaktywna geometria.

%package khangman
Summary:	A hangman game
Summary(pl):	Gra w wisielca
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

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

%package kiten
Summary:	A Japanese reference tool
Summary(pl):	S�ownik angielsko-japo�ski
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kiten
A Japanese reference tool.

%description kiten -l pl
S�ownik angielsko-japo�ski.

%package klettres
Summary:	Helps child to learn French alphabet and to read some syllables
Summary(pl):	Pomoc w nauce francuskiego alfabetu i sylab dla dzieci
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description klettres
Helps child to learn French alphabet and to read some syllables.

%description klettres -l pl
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl):	Koordynograf
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kmplot
Mathematical function plotter.

%description kmplot -l pl
Koordynograf.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta �amig��wka
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kmessedwords
Simple mind-training game.

%description kmessedwords -l pl
Prosta �amig��wka.

%package kpercentage
Summary:	A percentage tutor
Summary(pl):	Program do nauki procent�w
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kpercentage
A percentage tutor.

%description kpercentage -l pl
Program do nauki procent�w.

%package kstars
Summary:	Desktop planetarium
Summary(pl):	Planetarium
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kstars
Desktop planetarium.

%description kstars -l pl
Planetarium.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl):	Program do nauki maszynopisania
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}
Provides:	ktouch
Obsoletes:	ktouch

%description ktouch
Program for learning touch typing.

%description ktouch -l pl
Program do nauki maszynopisania.

%package kverbos
Summary:	Spanish verb form study application for KDE
Summary(pl):	Program do nauki form czasownik�w w j�zyku hiszpa�skim
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kverbos
Spanish verb form study application for KDE.

%description kverbos -l pl
Program do nauki form czasownik�w w j�zyku hiszpa�skim.

%package kvoctrain
Summary:	Vocabulary trainer
Summary(pl):	Program do �wiczenia s�ownictwa
Group:		X11/Applications/Science
Requires:	%{name} = %{epoch}:%{version}

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do �wiczenia s�ownictwa.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find . -name \*.desktop | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $plik 2>/dev/null
done

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

ALD=$RPM_BUILD_ROOT%{_applnkdir}/Edutainment
mv $ALD/{{Languages,Mathematics,Miscellanous,Science,Tools}/*.desktop,.}

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv locolor/16x16/actions/*.png crystalsvg/16x16/actions
mv {locolor,crystalsvg}/16x16/apps/kvoctrain.xpm
cd -

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}
for i in {flashkard,keduca,kstars}.png; do
	ln -s crystalsvg/48x48/apps/$i $RPM_BUILD_ROOT%{_pixmapsdir}/$i
done

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW/LC_MESSAGES/{K,k}iten.mo

%find_lang	flashkard	--with-kde
%find_lang	kalzium		--with-kde
%find_lang	keduca		--with-kde
%find_lang	kgeo		--with-kde
%find_lang	khangman	--with-kde
%find_lang	kiten		--with-kde
%find_lang	klettres	--with-kde
%find_lang	kmathtool	--with-kde
%find_lang	kmessedwords	--with-kde
%find_lang	kmplot		--with-kde
%find_lang	kpercentage	--with-kde
%find_lang	kstars		--with-kde
%find_lang	ktouch		--with-kde
%find_lang	kverbos		--with-kde
%find_lang	kvoctrain	--with-kde

# probably should be in another package
#%find_lang	knorskverbs	--with-kde

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kmathtool.lang
%defattr(644,root,root,755)
%doc README*
%{_libdir}/libkdeeducore.la
%attr(755,root,root) %{_libdir}/libkdeeducore.so.*
%{_datadir}/mimelnk/application/x-edu.desktop
%{_pixmapsdir}/*/*/actions/*
%{_pixmapsdir}/*/*/apps/edu_*
%{_pixmapsdir}/hicolor/48x48/apps/[!k]*
%{_pixmapsdir}/hicolor/48x48/apps/k[!v]*

%files devel
%defattr(644,root,root,755)
%doc README*
%{_includedir}/*
%{_libdir}/libkdeeducore.so

%files flashkard -f flashkard.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flashkard
%{_datadir}/apps/flashkard
%{_applnkdir}/Edutainment/flashkard.desktop
%{_pixmapsdir}/*/*/*/flashkard.png
%{_pixmapsdir}/flashkard.png
%{_mandir}/man1/flashkard.*

%files kalzium -f kalzium.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%{_datadir}/apps/kalzium
%{_applnkdir}/Edutainment/kalzium.desktop
%{_pixmapsdir}/[!l]*/*/*/kalzium.png
%{_pixmapsdir}/kalzium.png
%{_mandir}/man1/kalzium.*

%files keduca -f keduca.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%{_datadir}/apps/keduca
%{_applnkdir}/Edutainment/keduca*.desktop
%{_pixmapsdir}/*/*/*/keduca.png
%{_pixmapsdir}/keduca.png
%{_mandir}/man1/keduca.*

%files kgeo -f kgeo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeo
%{_datadir}/apps/kgeo
%{_applnkdir}/Edutainment/kgeo.desktop
%{_pixmapsdir}/[!l]*/*/*/kgeo.png
%{_pixmapsdir}/kgeo.png
%{_mandir}/man1/kgeo.*

%files khangman -f khangman.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_applnkdir}/Edutainment/khangman.desktop
%{_pixmapsdir}/[!l]*/*/*/khangman.png
%{_pixmapsdir}/khangman.png
%{_mandir}/man1/khangman.*

%files kiten -f kiten.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten*
%{_libdir}/kiten.la
%attr(755,root,root) %{_libdir}/kiten.so
%{_datadir}/apps/kiten
%{_applnkdir}/Edutainment/kiten.desktop
%{_pixmapsdir}/*/*/*/kiten.png
%{_pixmapsdir}/kiten.png
%{_mandir}/man1/kiten*

%files klettres -f klettres.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_applnkdir}/Edutainment/klettres.desktop
%{_pixmapsdir}/[!l]*/*/*/klettres.png
%{_pixmapsdir}/klettres.png
%{_mandir}/man1/klettres.*

%files kmessedwords -f kmessedwords.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_applnkdir}/Edutainment/kmessedwords.desktop
%{_pixmapsdir}/[!l]*/*/*/kmessedwords.png
%{_pixmapsdir}/kmessedwords.png
%{_mandir}/man1/kmessedwords.*

%files kmplot -f kmplot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_datadir}/apps/kmplot
%{_applnkdir}/Edutainment/kmplot.desktop
%{_pixmapsdir}/[!l]*/*/*/kmplot.png
%{_pixmapsdir}/kmplot.png
%{_mandir}/man1/kmplot.*

%files kpercentage -f kpercentage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_applnkdir}/Edutainment/kpercentage.desktop
%{_pixmapsdir}/[!l]*/*/*/kpercentage.png
%{_pixmapsdir}/kpercentage.png
%{_mandir}/man1/kpercentage.*

%files kstars -f kstars.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstars
%{_datadir}/apps/kstars
%{_applnkdir}/Edutainment/kstars.desktop
%{_pixmapsdir}/[!l]*/*/*/kstars.png
%{_pixmapsdir}/kstars.png
%{_mandir}/man1/kstars.*

%files ktouch -f ktouch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_applnkdir}/Edutainment/ktouch.desktop
%{_pixmapsdir}/*/*/*/ktouch.png
%{_pixmapsdir}/ktouch.png
%{_mandir}/man1/ktouch.*

%files kverbos -f kverbos.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kverbos
%{_datadir}/apps/kverbos
%{_applnkdir}/Edutainment/kverbos.desktop
%{_pixmapsdir}/*/*/*/kverbos*.png
%{_pixmapsdir}/kverbos.png
%{_mandir}/man1/kverbos.*

%files kvoctrain -f kvoctrain.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_applnkdir}/Edutainment/kvoctrain.desktop
%{_pixmapsdir}/[!l]*/*/*/kvoctrain*
%{_pixmapsdir}/kvoctrain.png
%{_mandir}/man1/kvoctrain.*
%{_mandir}/man1/langen2kvtml.*
%{_mandir}/man1/spotlight2kvtml.*

Summary:	K Desktop Environment - edutainment
Summary(pl):	K Desktop Environment - edukacja i rozrywka
Name:		kdeedu
Version:	3.0.4
Release:	1
Epoch:		7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
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
Group:		X11/Applications
Requires:	%{name} = %{version}

%description keduca
Creation and revision of form-based tests and exams.

%description keduca -l pl
Tworzenie i sprawdzanie test�w i egzamin�w.

%package kgeo
Summary:	Interactive geometry
Summary(pl):	Interaktywna geometria
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kgeo
Interactive geometry.

%description kgeo -l pl
Interaktywna geometria.

%package klettres
Summary:	Helps child to learn french alphabet and to read some syllables
Summary(pl):	Pomoc w nauce francuskiego alfabetu i sylab dla dzieci
Group:		X11/Applications
Requires:	%{name} = %{version}

%description klettres
Helps child to learn french alphabet and to read some syllables

%description klettres -l pl
Pomoc w nauce francuskiego alfabetu i sylab dla dzieci.

%package kmessedwords
Summary:	Simple mind-training game
Summary(pl):	Prosta �amig��wka.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kmessedwords
Simple mind-training game.

%description kmessedwords -l pl
Prosta �amig��wka.

%package kstars
Summary:	Desktop planetarium
Summary(pl):	Planetarium.
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
Summary(pl):	Program do �wiczenia s�ownictwa
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kvoctrain
Vocabulary trainer.

%description kvoctrain -l pl
Program do �wiczenia s�ownictwa.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#%{__make} -f Makefile.cvs
%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang kgeo --with-kde
%find_lang klettres --with-kde
%find_lang kmessedwords --with-kde
%find_lang kstars --with-kde
%find_lang ktouch --with-kde
%find_lang kvoctrain --with-kde
%find_lang keduca --with-kde
# WTF?
%find_lang klatin --with-kde
# WTF?
%find_lang khangman --with-kde

cat klatin.lang >> khangman.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f khangman.lang
%defattr(644,root,root,755)
%doc README*
%{_datadir}/mimelnk/application/x-edu.desktop

%files keduca -f keduca.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keduca
%{_datadir}/apps/keduca
%{_pixmapsdir}/*/*/*/keduca*
%{_applnkdir}/Edutainment/keduca.desktop

%files kgeo -f kgeo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeo
%{_datadir}/apps/kgeo
%{_pixmapsdir}/*/*/*/kgeo*
%{_applnkdir}/Edutainment/kgeo.desktop

%files klettres -f klettres.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_pixmapsdir}/*/*/*/klettres*
%{_applnkdir}/Edutainment/French/klettres.desktop

%files kmessedwords -f kmessedwords.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmessedwords
%{_datadir}/apps/kmessedwords
%{_pixmapsdir}/*/*/*/kmessedwords*
%{_applnkdir}/Edutainment/kmessedwords.desktop

%files kstars -f kstars.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kstars
%{_datadir}/apps/kstars
%{_pixmapsdir}/*/*/*/kstars*
%{_applnkdir}/Edutainment/kstars.desktop

%files ktouch -f ktouch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/apps/ktouch
%{_pixmapsdir}/*/*/*/ktouch*
%{_applnkdir}/Edutainment/ktouch.desktop

%files kvoctrain -f kvoctrain.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kvoctrain
%attr(755,root,root) %{_bindir}/langen2kvtml
%attr(755,root,root) %{_bindir}/spotlight2kvtml
%{_datadir}/apps/kvoctrain
%{_pixmapsdir}/*/*/*/kvoctrain*
%{_pixmapsdir}/kvoctrain*
%{_applnkdir}/Edutainment/kvoctrain.desktop

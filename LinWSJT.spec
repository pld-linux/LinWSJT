Summary:	JT44 and FSK441 for Linux
Summary(pl):	JT44 i FSK441 dla Linuksa
Name:		LinWSJT
Version:	0.4.6
Release:	2
License:	GPL
Group:		Applications
Source0:	http://www.qsl.net/g4klx/%{name}-%{version}.tar.gz
# Source0-md5:	dd9cf86f4bd260eea759abde8c2ae28c
Patch0:		%{name}-Makefile.patch
URL:		http://aldo.sourceforge.net/
BuildRequires:	wxGTK2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux version of the JT44 and FSK441 communications protocols, usually
described together as WSJT.

JT44 is used for very weak signal operation, for example Moonbounce,
while FSK441 is specifically designed for Meteor Scatter.
 
%description -l pl
Obs³uga protoko³ów komunikacyjnych JT44 oraz FSK441, zwykle
okre¶lanych razem jako WSJT.

JT44 jest u¿ywane w przypadku bardzo s³abych sygna³ów, np. odbicie od
ksiê¿yca, a FSK441 zosta³ zaprojektowany do ³±czno¶ci przez odbicie od
¶ladów meteorów.
  
%prep
%setup -q 
%patch -p1

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall -I.. `wxgtk2-2.4-config --cxxflags`" \
	LDFLAGS="`wxgtk2-2.4-config --ldflags`" \
	LIBS="-lfftw -lsndfile `wxgtk2-2.4-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*

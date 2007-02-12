Summary:	Wrapper for the Hi-Tech C CP/M compiler
Summary(pl.UTF-8):   Wrapper dla kompilatora Hi-Tech C pod CP/M
Name:		zxcc
Version:	0.5.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.seasip.demon.co.uk/Unix/Zxcc/%{name}-%{version}.tar.gz
# Source0-md5:	43d94e08016b7ad117318dde12073cfe
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www.seasip.demon.co.uk/Unix/Zxcc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpmio-devel
BuildRequires:	cpmredir-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zxcc is a wrapper for the Hi-Tech C CP/M compiler, allowing it to be
used as a cross-compiler under UNIX. Version 0.5.x also works with the
build tools necessary to assemble CP/M 3 (MAC, RMAC, LINK, GENCOM).

%description -l pl.UTF-8
zxcc to wrapper dla kompilatora Hi-Tech C dla CP/M, pozwalający na
używanie go jako kompilatora skrośnego pod systemami uniksowymi.
Wersje 0.5.x działają także z narzędziami potrzebnymi do asemblacji
CP/M 3 (MAC, RMAC, LINK, GENCOM).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-cpmio

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog zxcc.html
%attr(755,root,root) %{_bindir}/*
%{_libdir}/cpm

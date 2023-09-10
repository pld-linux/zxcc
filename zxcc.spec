Summary:	Wrapper for the Hi-Tech C CP/M compiler
Summary(pl.UTF-8):	Wrapper dla kompilatora Hi-Tech C pod CP/M
Name:		zxcc
Version:	0.5.7
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://www.seasip.info/Unix/Zxcc/%{name}-%{version}.tar.gz
# Source0-md5:	b20977f2c5e90ae67dbfe825223f5244
Patch0:		%{name}-system-libs.patch
URL:		http://www.seasip.info/Unix/Zxcc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpmio-devel >= 1.1.1
BuildRequires:	cpmredir-devel >= 1.1.1
BuildRequires:	libtool
Requires:	cpmio >= 1.1.1
Requires:	cpmredir >= 1.1.1
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

# packaged in HTML version as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/zxcc/zxcc.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog zxcc.html
%attr(755,root,root) %{_bindir}/zxas
%attr(755,root,root) %{_bindir}/zxc
%attr(755,root,root) %{_bindir}/zxcc
%attr(755,root,root) %{_bindir}/zxlibr
%attr(755,root,root) %{_bindir}/zxlink
%dir %{_libdir}/cpm
%dir %{_libdir}/cpm/bin80
%{_libdir}/cpm/bin80/bios.bin
%dir %{_libdir}/cpm/lib80
%dir %{_libdir}/cpm/include80

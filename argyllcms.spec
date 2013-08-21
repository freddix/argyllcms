Summary:	ICC compatible color management system
Name:		argyllcms
Version:	1.6.0
Release:	1
License:	AGPL v3, MIT, GPL v2+, LGPL v2.1+, FDL v1.3
Group:		X11/Applications/Graphics
Source0:	http://people.freedesktop.org/~hughsient/releases/h%{name}-%{version}.tar.xz
# Source0-md5:	03d9d07e6551a72e4b5023df3821a663
URL:		http://www.argyllcms.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libusbx-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXxf86vm-devel
Suggests:	colord
Suggests:	shared-color-profiles
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Argyll color management system supports accurate ICC profile
creation for acquisition devices, CMYK printers, film recorders and
calibration and profiling of displays.

%prep
%setup -qn h%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/color/argyll/ref/Makefile.am
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.{so,la}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/argyll

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Readme.txt
%doc doc/*.html doc/*.jpg doc/*.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libargyll.so.?
%attr(755,root,root) %ghost %{_libdir}/libargyllicc.so.?
%attr(755,root,root) %{_libdir}/libargyll.so.*.*.*
%attr(755,root,root) %{_libdir}/libargyllicc.so.*.*.*
%dir %{_datadir}/color/argyll
%{_datadir}/color/argyll/ref


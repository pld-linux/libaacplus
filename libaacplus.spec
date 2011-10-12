Summary:	High Efficiency Advanced Audio Codec v2 (HE-AAC+)
Summary(pl.UTF-8):	Kodek dźwięku HE-AAC+ (High Efficiency Advanced Audio Codec v2)
Name:		libaacplus
Version:	2.0.2
Release:	1
License:	commercial (3GPP code), LGPL (wrapper code)
Group:		Libraries
Source0:	http://217.20.164.161/~tipok/aacplus/%{name}-%{version}.tar.gz
# Source0-md5:	3fc15d5aa91d0e8b8f94acb6555103da
Source1:	http://www.3gpp.org/ftp/Specs/archive/26_series/26.410/26410-800.zip
# NoSource1-md5:	2346a0f709d42cee88b784c513744e98
NoSource:	1
URL:		http://tipok.org.ua/node/17
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	fftw3-devel >= 3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High Efficiency Advanced Audio Codec v2 (he-aac+) encoder library
based on 3GPP source code (3GPP TS 26.410 V8.0.0) from:

http://www.3gpp.org/ftp/Specs/html-info/26410.htm

%description -l pl.UTF-8
Biblioteka kodująca kodekiem HE-AAC+ (High Efficiency Advanced Audio
Codec v2), oparta na kodzie źródłowym 3GPP (3GPP TS 26.410 V8.0.0) z:

http://www.3gpp.org/ftp/Specs/html-info/26410.htm

%package devel
Summary:	Header files for aacplus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki aacplus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for aacplus library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki aacplus.

%package static
Summary:	Static aacplus library
Summary(pl.UTF-8):	Statyczna biblioteka aacplus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static aacplus library.

%description static -l pl.UTF-8
Statyczna biblioteka aacplus.

%prep
%setup -q

ln -sf %{SOURCE1} src/26410-800.zip

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
# 3GPP source unpacking is not parallel-ready
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/aacplusenc
%attr(755,root,root) %{_libdir}/libaacplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaacplus.so.2
%{_mandir}/man1/aacplusenc.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaacplus.so
%{_includedir}/aacplus.h
%{_pkgconfigdir}/aacplus.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libaacplus.a

#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	Fuzzy string compare library
Name:		fstrcmp
Version:	0.7.D001
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/fstrcmp/%{name}-%{version}.tar.gz
# Source0-md5:	9c440bbdfcad9fd22e38f2388715b0cc
URL:		http://fstrcmp.sourceforge.net/
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fstrcmp package provides a library which may be used to make fuzzy
comparisons of strings and byte arrays. It also provides simple
commands for use in shell scripts.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
%{__make}

%if %{with tests}
# make t0001a ... t0010a
%{__make} $(seq -f "t%04ga" 1 10)
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -delete

# Fix permissions
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*

# Remove useless compilation instructions
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/building.pdf
# Remove API documentation in main subpackage
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/reference.pdf
# Remove duplicate README in PDF
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/readme.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/fstrcmp
%attr(755,root,root) %{_libdir}/libfstrcmp.so.*.*.*
%ghost %{_libdir}/libfstrcmp.so.0
%{_mandir}/man1/fstrcmp.1*
%{_mandir}/man1/fstrcmp_license.1*

%files devel
%defattr(644,root,root,755)
%doc etc/reference.pdf
%{_includedir}/fstrcmp.h
%attr(755,root,root) %{_libdir}/libfstrcmp.so
%{_pkgconfigdir}/fstrcmp.pc
%{_mandir}/man3/fmemcmp.3*
%{_mandir}/man3/fmemcmpi.3*
%{_mandir}/man3/fstrcasecmp.3*
%{_mandir}/man3/fstrcasecmpi.3*
%{_mandir}/man3/fstrcmp.3*
%{_mandir}/man3/fstrcmpi.3*
%{_mandir}/man3/fstrcoll.3*
%{_mandir}/man3/fstrcolli.3*
%{_mandir}/man3/fwcscmp.3*
%{_mandir}/man3/fwcscmpi.3*

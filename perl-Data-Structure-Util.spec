#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Structure-Util
Summary:	Data::Structure::Util - Change nature of data within a structure
Summary(pl.UTF-8):	Data::Structure::Util - Zmiana natury danych wewnątrz struktury
Name:		perl-%{pdir}-%{pnam}
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1af2a4149ba81f42d11dbfaecbaf5973
URL:		http://search.cpan.org/dist/Data-Structure-Util/
%if %{with tests}
BuildRequires:	perl-Clone
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Test-Pod
%endif
BuildRequires:	perl-Module-Build >= 0.02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Structure::Util is a toolbox to manipulate data inside a data
structure. It can parse an entire tree and perform the operation
requested on each appropriate element. It can transform to UTF-8 any
string within a data structure. I can attempt to transform any UTF-8
string back to default encoding either. It can remove the blessing on
any reference. It can collect all the objects or detect if there is a
circular reference.

It is written in C for decent speed.

%description -l pl.UTF-8
Data::Structure::Util to zestaw narzędzi do obróbki danych wewnątrz
struktur danych. Może analizować całe drzewo i wykonywać żądane
operacje na każdym właściwym elemencie. Może przekształcać na UTF-8
dowolny łańcuch wewnątrz struktury danych, a także próbować
przekształcić dowolny łańcuch z UTF-8 z powrotem do domyślnego
kodowania. Może usuwać błogosławieństwo z dowolnej referencji. Może
zbierać wszystkie obiekty lub wykrywać czy są zapętlone referencje.

Jest napisany w C w celu zapewnienia przyzwoitej szybkości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Data/Structure/Util/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%dir %{perl_vendorarch}/Data/Structure
%{perl_vendorarch}/Data/Structure/Util.pm
%dir %{perl_vendorarch}/auto/Data/Structure
%dir %{perl_vendorarch}/auto/Data/Structure/Util
%{perl_vendorarch}/auto/Data/Structure/Util/Util.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Data/Structure/Util/Util.so
%{_mandir}/man3/*

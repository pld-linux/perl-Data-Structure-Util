#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Structure-Util
Summary:	Data::Structure::Util - Change nature of data within a structure
Summary(pl):	Data::Structure::Util - Zmiana natury danych wewn±trz struktury
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3cbec998cd7c55b1244b3f782569b552
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
requested on each appropriate element. It can transform to utf8 any
string within a data structure. I can attempts to transform any utf8
string back to default encoding either. It can remove the blessing on
any reference. It can collect all the objects or detect if there is a
circular reference.

It is written in C for decent speed.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorarch}/Data/Structure/Util.pm
%{_mandir}/man3/*

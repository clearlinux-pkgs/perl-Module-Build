#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Build
Version  : 0.4231
Release  : 41
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4231.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4231.tar.gz
Summary  : 'Build and install Perl modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Build-bin = %{version}-%{release}
Requires: perl-Module-Build-man = %{version}-%{release}
Requires: perl-Module-Build-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Module::Build - Build and install Perl modules
SYNOPSIS
Standard process for building & installing modules:

%package bin
Summary: bin components for the perl-Module-Build package.
Group: Binaries

%description bin
bin components for the perl-Module-Build package.


%package dev
Summary: dev components for the perl-Module-Build package.
Group: Development
Requires: perl-Module-Build-bin = %{version}-%{release}
Provides: perl-Module-Build-devel = %{version}-%{release}
Requires: perl-Module-Build = %{version}-%{release}

%description dev
dev components for the perl-Module-Build package.


%package man
Summary: man components for the perl-Module-Build package.
Group: Default

%description man
man components for the perl-Module-Build package.


%package perl
Summary: perl components for the perl-Module-Build package.
Group: Default
Requires: perl-Module-Build = %{version}-%{release}

%description perl
perl components for the perl-Module-Build package.


%prep
%setup -q -n Module-Build-0.4231
cd %{_builddir}/Module-Build-0.4231

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/config_data

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Build.3
/usr/share/man/man3/Module::Build::API.3
/usr/share/man/man3/Module::Build::Authoring.3
/usr/share/man/man3/Module::Build::Base.3
/usr/share/man/man3/Module::Build::Bundling.3
/usr/share/man/man3/Module::Build::Compat.3
/usr/share/man/man3/Module::Build::ConfigData.3
/usr/share/man/man3/Module::Build::Cookbook.3
/usr/share/man/man3/Module::Build::Notes.3
/usr/share/man/man3/Module::Build::PPMMaker.3
/usr/share/man/man3/Module::Build::Platform::Default.3
/usr/share/man/man3/Module::Build::Platform::MacOS.3
/usr/share/man/man3/Module::Build::Platform::Unix.3
/usr/share/man/man3/Module::Build::Platform::VMS.3
/usr/share/man/man3/Module::Build::Platform::VOS.3
/usr/share/man/man3/Module::Build::Platform::Windows.3
/usr/share/man/man3/Module::Build::Platform::aix.3
/usr/share/man/man3/Module::Build::Platform::cygwin.3
/usr/share/man/man3/Module::Build::Platform::darwin.3
/usr/share/man/man3/Module::Build::Platform::os2.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/config_data.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

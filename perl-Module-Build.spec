#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Build
Version  : 0.4224
Release  : 16
URL      : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/Module-Build-0.4224.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/Module-Build-0.4224.tar.gz
Summary  : 'Build and install Perl modules'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Build-bin
Requires: perl-Module-Build-doc

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


%package doc
Summary: doc components for the perl-Module-Build package.
Group: Documentation

%description doc
doc components for the perl-Module-Build package.


%prep
%setup -q -n Module-Build-0.4224

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Module/Build.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/API.pod
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Authoring.pod
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Base.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Bundling.pod
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Compat.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Config.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/ConfigData.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Cookbook.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Dumper.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Notes.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/PPMMaker.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/Default.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/MacOS.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/Unix.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/VMS.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/VOS.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/Windows.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/aix.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/cygwin.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/darwin.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/Platform/os2.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Build/PodParser.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/config_data

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

Name:		fio
Version:	1.18
Release:	1%{?dist}
Summary:	Multithreaded IO generation tool

Group:		Applications/System
License:	GPLv2
URL:		http://git.kernel.dk/?p=fio.git;a=summary
Source:		http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	libaio-devel

%description
fio is an I/O tool that will spawn a number of threads or processes doing
a particular type of io action as specified by the user.  fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install prefix=%{_prefix} mandir=%{_mandir} DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README REPORTING-BUGS COPYING HOWTO examples
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Feb 13 2008 Eric Sandeen <sandeen@redhat.com> 1.18-1
- Initial build

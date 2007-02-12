Summary:	A FAM (File Alteration Monitor) client
Summary(pl.UTF-8):   Klient FAM (monitora zmian plików)
Name:		fileschanged
Version:	0.6.4
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/fileschanged/%{name}-%{version}.tar.gz
# Source0-md5:	c8e6d9829a2ecb2363835787f578415d
URL:		http://fileschanged.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	help2man
Requires:	fam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fileschanged utility is a FAM (File Alteration Monitor) client.
From the command-line it monitors sets of files and shows you when
they change. You can use fileschanged in shell scripts to take action
when monitored files become altered.

%description -l pl.UTF-8
Fileschanged to klient FAM (monitora zmian plików). Pozwala
monitorować podany mu zestaw plików i informować, jeśli któryś z nich
się zmieni. Można używać fileschanged w skryptach powłoki, by zrobić
coś gdy zmienią się określone pliki.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# only useless files (docs and fileschanged.lsm)
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*

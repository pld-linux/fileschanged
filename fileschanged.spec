Summary:	A FAM (File Alteration Monitor) client
Summary(pl):	Klient FAM (monitora zmian plików)
Name:		fileschanged
Version:	0.6.1
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/fileschanged/%{name}-%{version}.tar.gz
# Source0-md5:	d7f6b4030d2d46ba94da781bef61095a
URL:		http://fileschanged.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	help2man
Requires:	fam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fileschanged utility is a FAM (File Alteration Monitor) client.
From the command-line it monitors sets of files and shows you when
they change. You can use fileschanged in shell scripts to take action
when monitored files become altered.

%description -l pl
Fileschanged to klient FAM (monitora zmian plików). Pozwala
monitorowaæ podany mu zestaw plików i informowaæ, je¶li który¶ z nich
siê zmieni. Mo¿na u¿ywaæ fileschanged w skryptach pow³oki, by zrobiæ
co¶ gdy zmieni± siê okre¶lone pliki.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*

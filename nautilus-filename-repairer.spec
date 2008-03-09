Summary:	Reencode filenames in Nautilus
Summary(pl.UTF-8):	Zakoduj nazwy plików w Nautilus
Name:		nautilus-filename-repairer
Version:	0.0.2
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://kldp.net/frs/download.php/4443/%{name}-%{version}.tar.bz2
# Source0-md5:	b3b73deeb3a8745a90e57bc6287efba0
URL:		http://repairer.kldp.net/
BuildRequires:	intltool
BuildRequires:  gettext-devel
BuildRequires:  gtk+2-devel >= 2.2.18
BuildRequires:  gnome-vfs2-devel >= 2.20.1
BuildRequires:  nautilus-devel >= 2.20.0
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus Filename Repairer is a nautilus extension which provides
context menu to change the selected filename to correct encoding if
the file has invalid encoding. You can easily rename a file by
selecting a context menu item.

%description -l pl.UTF-8
Nautilus Filename Repairer jest rozszerzeniem nautilusa dostarczającym
menu kontekstowe do zmiany zaznaczonego nazwy pliku na poprawne
kodowanie, jeżeli plik jest poprawnie zakodowany. Możesz łatwo zmienić
nazwę pliku przez wybranie odpowiedniej opcji w menu kontekstowym.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/nautilus/extensions-1.0/*.so

Summary:	Reencode filenames in Nautilus
Summary(pl.UTF-8):	Zakoduj nazwy plików w Nautilus
Name:		nautilus-filename-repairer
Version:	0.0.6
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://repairer.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	680bb6ab46687541bd6ff4fe5a16e185
URL:		http://code.google.com/p/repairer/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:  gettext-devel
BuildRequires:  gtk+2-devel >= 2.2.18
BuildRequires:  gnome-vfs2-devel >= 2.20.1
BuildRequires:	libtool
BuildRequires:  nautilus-devel >= 2.20.0
BuildRequires:	pkgconfig
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
%{__libtoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/nautilus/extensions-2.0/*.so

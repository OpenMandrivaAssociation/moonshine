%define name moonshine
%define version 0.2
%define release %mkrel 1

Summary: Windows Media player based on Moonlight
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://abock.org/moonshine/releases/%{name}-%{version}.tar.bz2
License: MIT
Group: Video
Url: http://abock.org/moonshine/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xulrunner-devel-unstable
BuildRequires: glib2-devel
Requires: moon >= 1.0

%description
Moonshine leverages the Windows Media capabilities from Silverlight,
provided by the Moonlight browser plugin on Linux, and the Firefox web
browser framework to enable the playback of embedded Windows Media
content on the web and local files on a user's desktop.

%package player
Summary: Standalone Windows Media player
Group: Video
Requires: xulrunner
Requires: %name = %version-%release

%description player
Moonshine leverages the Windows Media capabilities from Silverlight,
provided by the Moonlight browser plugin on Linux, and the Firefox web
browser framework to enable the playback of embedded Windows Media
content on the web and local files on a user's desktop.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %buildroot%_libdir/mozilla/plugins
mv %buildroot%_libdir/browser-plugins/* %buildroot%_libdir/mozilla/plugins/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS
%_libdir/mozilla/plugins/libmoonshine-plugin.so
%_libdir/mozilla/plugins/libmoonshine-plugin.la
%_datadir/%name

%files player
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/*/*

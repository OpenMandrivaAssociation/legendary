Name:           legendary
Version:        0.20.13
Release:        1
Summary:        Free and open-source replacement for the Epic Games Launcher
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/derrod/legendary
Source0:        https://github.com/derrod/legendary/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(requests)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(wheel)

Requires: python-requests
Requires: python-wheel

%description
Legendary is an open-source game launcher that can download and install games
from the Epic Games Store on Linux and Windows. It's name as a tongue-in-cheek
play on tiers of item rarity in many MMORPGs.


%prep
%autosetup -p1

# E: non-executable-script
for lib in %{name}/{*.py,downloader/*.py,lfs/*.py,models/*.py}; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python_sitelib}/%{name}*.egg-info/
%{python_sitelib}/%{name}/

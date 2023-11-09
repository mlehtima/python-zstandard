%global desc This project provides Python bindings for interfacing with the Zstandard\
compression library. A C extension and CFFI interface are provided.

Name: python-zstandard
Version: 0.22.0
Release: 1
Summary: Zstandard bindings for Python
License: (BSD-3-Clause OR GPL-2.0-only) AND MIT
URL: https://github.com/indygreg/python-zstandard
Source0: %{name}-%{version}.tar.bz2

%define sonamever %(echo %{version} | cut -d '+' -f 1)

%description
%{desc}

%package -n python3-zstandard
Summary: %{summary}
BuildRequires: gcc
BuildRequires: libzstd-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-cffi
# https://github.com/indygreg/python-zstandard/issues/48
Provides: bundled(zstd) = 1.5.5

%description -n python3-zstandard
%{desc}

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%py3_build

%install
%py3_install

%files -n python3-zstandard
%license LICENSE zstd/COPYING
%doc README.rst
%{python3_sitearch}/zstandard-%{sonamever}-py%{python3_version}.egg-info
%{python3_sitearch}/zstandard


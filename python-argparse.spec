# NOTE
# - The argparse module (v1.1) is now part of the Python standard library since 2.7, 3.2
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	doc	# Sphinx documentation [fails as of 1.4.0]
%bcond_without	tests	# test run

%define		module	argparse
Summary:	Optparse inspired command line parser for Python 2
Summary(pl.UTF-8):	Analizator linii poleceń dla Pythona 2 zainspirowany przez optparse
Name:		python-argparse
Version:	1.4.0
Release:	1
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/pypi/argparse
Source0:	https://pypi.python.org/packages/source/a/argparse/%{module}-%{version}.tar.gz
# Source0-md5:	08062d2ceb6596fcbc5a7e725b53746f
URL:		https://github.com/ThomasWaldmann/argparse/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.3
BuildRequires:	python-setuptools
%endif
%if %{with python2}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The argparse module is an optparse-inspired command line parser that
improves on optparse by:
 - handling both optional and positional arguments
 - supporting parsers that dispatch to sub-parsers
 - producing more informative usage messages
 - supporting actions that consume any number of command-line args
 - allowing types and actions to be specified with simple callables
   instead of hacking class attributes like STORE_ACTIONS or
   CHECK_METHODS

as well as including a number of other more minor improvements on the
optparse API.

%description -l pl.UTF-8
Moduł argparse to analizator linii poleceń zainspirowany przez
optparse zawierający następujące ulepszenia w stosunku do optparse:
 - obsługa argumentów zarówno opcjonalnych, jak i pozycyjnych
 - obsługa analizatorów przekazujących do podanalizatorów
 - bardziej informacyjne komunikaty o sposobie użycia polecenia
 - obsługa akcji pochłaniających dowolną liczbę argumentów linii
   poleceń
 - możliwość podania typów i akcji poprzez proste wywołania zamiast
   grzebania w atrybutach klas, takich jak STORE_ACTIONS czy
   CHECK_METHODS

a także wiele innych, pomniejszych ulepszeń w stosunku do API
optparse.

%package -n python3-%{module}
Summary:	Optparse inspired command line parser for Python 3
Summary(pl.UTF-8):	Analizator linii poleceń dla Pythona 3 zainspirowany przez optparse
Group:		Development/Languages/Python

%description -n python3-%{module}
The argparse module is an optparse-inspired command line parser that
improves on optparse by:
 - handling both optional and positional arguments
 - supporting parsers that dispatch to sub-parsers
 - producing more informative usage messages
 - supporting actions that consume any number of command-line args
 - allowing types and actions to be specified with simple callables
   instead of hacking class attributes like STORE_ACTIONS or
   CHECK_METHODS

as well as including a number of other more minor improvements on the
optparse API.

%description -n python3-%{module} -l pl.UTF-8
Moduł argparse to analizator linii poleceń zainspirowany przez
optparse zawierający następujące ulepszenia w stosunku do optparse:
 - obsługa argumentów zarówno opcjonalnych, jak i pozycyjnych
 - obsługa analizatorów przekazujących do podanalizatorów
 - bardziej informacyjne komunikaty o sposobie użycia polecenia
 - obsługa akcji pochłaniających dowolną liczbę argumentów linii
   poleceń
 - możliwość podania typów i akcji poprzez proste wywołania zamiast
   grzebania w atrybutach klas, takich jak STORE_ACTIONS czy
   CHECK_METHODS

a także wiele innych, pomniejszych ulepszeń w stosunku do API
optparse.

%prep
%setup -q -n %{module}-%{version}
%undos README.txt
%{__rm} -r doc/source

%build
%if %{with python2}
%py_build

%if %{with tests}
cd test
PYTHONPATH=../ %{__python} test_argparse.py
cd ..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
cd test
PYTHONPATH=../ %{__python3} test_argparse.py
cd ..
%endif
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.txt README.txt %{?with_doc:doc/html}
%{py_sitescriptdir}/argparse.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.txt README.txt %{?with_doc:doc/html}
%{py3_sitescriptdir}/argparse.py
%{py3_sitescriptdir}/__pycache__/argparse.cpython-*.py[co]
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

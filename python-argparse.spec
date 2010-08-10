#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	argparse
Summary:	Optparse inspired command line parser for Python
Name:		python-argparse
Version:	1.1
Release:	1
License:	ASL 2.0
Group:		Development/Languages
URL:		http://code.google.com/p/argparse/
Source0:	http://argparse.googlecode.com/files/%{module}-%{version}.zip
# Source0-md5:	e62565cde81a8deb61f90dcb5e8861a4
BuildRequires:	python-distribute
BuildRequires:	rpmbuild(macros) >= 1.553
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

%prep
%setup -q -n %{module}-%{version}
%undos README.txt doc/_static/pygments.css
%{__rm} -rf doc/source

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%if %{with tests}
cd test
PYTHONPATH=../ %{__python} test_%{module}.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%{py_sitescriptdir}/%{module}.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
%endif

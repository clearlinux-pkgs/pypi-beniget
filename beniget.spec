#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7B24DA8C9551659F (sguelton@redhat.com)
#
Name     : beniget
Version  : 0.4.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/14/e7/50cbac38f77eca8efd39516be6651fdb9f3c4c0fab8cf2cf05f612578737/beniget-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/e7/50cbac38f77eca8efd39516be6651fdb9f3c4c0fab8cf2cf05f612578737/beniget-0.4.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/14/e7/50cbac38f77eca8efd39516be6651fdb9f3c4c0fab8cf2cf05f612578737/beniget-0.4.1.tar.gz.asc
Summary  : Extract semantic information about static Python code
Group    : Development/Tools
License  : BSD-3-Clause
Requires: beniget-license = %{version}-%{release}
Requires: beniget-python = %{version}-%{release}
Requires: beniget-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : gast-python
BuildRequires : pip

%description
A static analyzer for Python2 and Python3 code.
        
        Beniget provides a static over-approximation of the global and
        local definitions inside Python Module/Class/Function.
        It can also compute def-use chains from each definition.

%package license
Summary: license components for the beniget package.
Group: Default

%description license
license components for the beniget package.


%package python
Summary: python components for the beniget package.
Group: Default
Requires: beniget-python3 = %{version}-%{release}

%description python
python components for the beniget package.


%package python3
Summary: python3 components for the beniget package.
Group: Default
Requires: python3-core
Provides: pypi(beniget)
Requires: pypi(gast)

%description python3
python3 components for the beniget package.


%prep
%setup -q -n beniget-0.4.1
cd %{_builddir}/beniget-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635706689
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/beniget
cp %{_builddir}/beniget-0.4.1/LICENSE %{buildroot}/usr/share/package-licenses/beniget/f76d03572a96c45c7c1fd8212bce69dbe34fa924
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/beniget/f76d03572a96c45c7c1fd8212bce69dbe34fa924

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

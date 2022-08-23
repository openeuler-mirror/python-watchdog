%global _empty_manifest_terminate_build 0
Name:		python-watchdog
Version:	2.1.9
Release:	1
Summary:	Filesystem events monitoring
License:	Apache-2.0
URL:		https://github.com/gorakhargosh/watchdog
Source0:	https://files.pythonhosted.org/packages/42/f7/da8e889f8626786eac9454e8d2718fc79359ed517be20cdd50c647167d39/watchdog-2.1.9.tar.gz

Requires:	python3-PyYAML
Requires:	python3-argh

%description
Python API and shell utilities to monitor file system events.
Works on 3.6+.

%package -n python3-watchdog
Summary:	Filesystem events monitoring
Provides:	python-watchdog
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-cffi
BuildRequires:	gcc
BuildRequires:	gdb
%description -n python3-watchdog
Python API and shell utilities to monitor file system events.
Works on 3.6+.

%package help
Summary:	Development documents and examples for watchdog
Provides:	python3-watchdog-doc
%description help
Python API and shell utilities to monitor file system events.
Works on 3.6+.

%prep
%autosetup -n watchdog-2.1.9

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-watchdog -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Aug 23 2022 hkgy <kaguyahatu@outlook.com> - 2.1.9-1
- Update to 2.1.9

* Fri May 20 2022 liukuo <liukuo@kylinos.cn> - 2.1.3-2
- License compliance rectification

* Thu Jul 22 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated

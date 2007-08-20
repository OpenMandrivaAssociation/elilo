%define name	elilo
%define version	3.3a
%define release	%mkrel 1
%define bootdir	/boot/efi/mandrake

Summary:	An ia64 LILO-like kernel loader
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		ftp://ftp.hpl.hp.com/pub/linux-ia64/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		elilo-3.3a-makefile.patch
Patch1:		elilo-3.3a-devscheme.patch
Patch2:		elilo-3.3a-localfs.patch
License:	GPL
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	gnu-efi >= 3.0
ExclusiveArch:	ia64

%description
ELILO is a linux boot loader for EFI-based systems, such as IA-64.

%prep
%setup -q
%patch0 -p1 -b .makefile
%patch1 -p1 -b .devscheme
%patch2 -p1 -b .localfs

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{bootdir}
install -m755 elilo.efi $RPM_BUILD_ROOT%{bootdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n elilo
%defattr(-,root,root)
%doc README.* LIMITATIONS TODO ChangeLog
%doc docs/elilo.txt
%{bootdir}/elilo.efi


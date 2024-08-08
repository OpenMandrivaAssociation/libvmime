%define	major	1
%define	libname	%mklibname vmime
%define	devname	%mklibname vmime -d

%define gitdate 20240808

Summary:	A powerful C++ class library for working with MIME/Internet messages
Name:		libvmime
Version:	0.9.3
# As of 2024/08/08, upstream "highly recommends" not using their releases and
# instead using git master.
Release:	%{?gitdate:0.%{gitdate}.}1
License:	GPLv2+
Group:		System/Libraries
URL:		https://vmime.org/
Source0:	https://github.com/kisli/vmime/archive/refs/heads/master.tar.gz#/libvmime-%{gitdate}.tar.gz
BuildSystem:	cmake
BuildOption:	-DVMIME_BUILD_STATIC_LIBRARY:BOOL=OFF
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libgsasl)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	doxygen
# Just so configuration can figure out it's %{_bindir}/sendmail
BuildRequires:	postfix

%description
VMime is a powerful C++ class library for parsing, generating or
editing Internet RFC-[2]822 and MIME messages. VMime is designed
to provide a fast and an easy way to manipulate Internet mail
messages.

It also includes support for using messaging protocols (POP3, IMAP,
SMTP and maildir) with a lot of features supported: listing folders,
downloading and adding messages to folders, extracting parts from
message, getting and setting message flags and a lot more.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%package -n	%{libname}
Summary:	Library associated with ncpfs
Group:		System/Libraries
Obsoletes:	%{mklibname vmime07 _0}

%description -n	%{libname}
VMime is a powerful C++ class library for parsing, generating or
editing Internet RFC-[2]822 and MIME messages. VMime is designed
to provide a fast and an easy way to manipulate Internet mail
messages.

It also includes support for using messaging protocols (POP3, IMAP,
SMTP and maildir) with a lot of features supported: listing folders,
downloading and adding messages to folders, extracting parts from
message, getting and setting message flags and a lot more.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%package -n	%{devname}
Summary:	Development files for the libvmime library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{mklibname vmime07 -d}

%description -n	%{devname}
The libvmime package includes header files and libraries necessary
for developing programs which use the libvmime C++ class library.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%files -n %{libname}
%doc AUTHORS COPYING
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_includedir}/vmime/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/vmime

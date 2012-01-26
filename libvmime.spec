%define	major	0
%define	libname	%mklibname vmime %{major}
%define	devname	%mklibname vmime -d


Summary:	A powerful C++ class library for working with MIME/Internet messages
Name:		libvmime
Version:	0.9.2
%define	svnrev	581
Release:	%{?svnrev:0.svn%{svnrev}}.1
License:	GPLv2+
Group:		System/Libraries
URL:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/
Source0:	http://downloads.sourceforge.net/project/vmime/vmime/0.9/%{name}-%{version}%{?svnrev:+svn%{svnrev}}.tar.bz2
Patch0:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-attachfnamelen.diff
Patch1:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-charset-catch.diff
Patch2:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-header-value-on-next-line.diff
Patch3:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-unicode-1-1-utf-7-charset.diff
Patch4:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.9.0-undisclosed-recipients.diff
Patch5:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.9.2-infinite-loop.diff
Patch6:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-flush-iconv.diff
Patch7:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-fullname-without-email-address.diff
Patch8:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-highchar-filename.diff
Patch9:		http://download.zarafa.com/community/final/7.0/7.0.4-31235/sourcecode/vmime-patches/vmime-empty-bodypart.diff
Patch10:	http://download.zarafa.com/community/final/7.0/7.0.4-31235/sourcecode/vmime-patches/vmime-mixed-qp-in-parameter.diff
Patch11:	libvmime-0.9.2-add-missing-gcrypt-linkage.patch
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	libgsasl-devel
BuildRequires:	gnutls-devel
BuildRequires:	zlib-devel

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch10 -p1
%patch11 -p1 -b .libgcrypt~

# Needed to apply branding patch
#libtoolize --force
#autoreconf --force --install
sh ./bootstrap

%build
export EXTRA_CFLAGS="%{optflags}"
export SENDMAIL=%{_sbindir}/sendmail

%configure2_5x
%make

%install
%makeinstall_std

# Remove the static library and libtool .la file
rm -f %{buildroot}%{_libdir}/%{name}.a

# Remove the documentation dir, as %doc will pick it up
rm -rf %{buildroot}%{_datadir}/doc

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_includedir}/vmime/
%{_libdir}/pkgconfig/*.pc

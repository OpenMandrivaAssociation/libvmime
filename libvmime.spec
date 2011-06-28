%define	major 0
%define	libname %mklibname vmime %{major}
%define develname %mklibname vmime -d

%if %mandriva_branch == Cooker
# Cooker
%define release %mkrel 1
%else
# Old distros
%define subrel 1
%define release %mkrel 0
%endif

Summary:	A powerful C++ class library for working with MIME/Internet messages
Name:		libvmime
Version:	0.9.1
Release:	%release
License:	GPLv2+
Group:		System/Libraries
URL:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/
Source0:	http://downloads.sourceforge.net/project/vmime/vmime/0.9/libvmime-%{version}.tar.bz2
Patch0:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-attachfnamelen.diff
Patch1:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-charset-catch.diff
Patch2:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-header-value-on-next-line.diff
Patch3:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.8.1-unicode-1-1-utf-7-charset.diff
Patch4:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.9.0-undisclosed-recipients.diff
Patch5:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-0.9.2-infinite-loop.diff
Patch6:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-flush-iconv.diff
Patch7:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-fullname-without-email-address.diff
Patch8:		http://download.zarafa.com/community/final/7.0/7.0.0-27791/sourcecode/vmime-patches/vmime-highchar-filename.diff
BuildRequires:	libgsasl-devel
BuildRequires:	gnutls-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Development files for the libvmime library
Group:		Development/C++
Requires:	%{libname} >= %{version}-%{release}
Requires:	pkgconfig
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname vmime07 -d}

%description -n	%{develname}
The libvmime package includes header files and libraries necessary
for developing programs which use the libvmime C++ class library.

This package contains an old and deprecated version of libvmime.
You need it only if the software you are using hasn't been updated
to work with the newer version and the newer API.

%prep

%setup -q -n libvmime-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p0

%build
# Needed to apply branding patch
#libtoolize --force
#autoreconf --force --install
sh ./bootstrap

export EXTRA_CFLAGS="%{optflags}"
export SENDMAIL=%{_sbindir}/sendmail

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# Complete the libvmime07 renaming at some places
mkdir -p %{buildroot}%{_includedir}/%{name}/
mv -f %{buildroot}%{_includedir}/{vmime,%{name}}/
#mv -f %{buildroot}%{_libdir}/pkgconfig/vmime{,07}.pc 

# Remove the static library and libtool .la file
rm -f %{buildroot}%{_libdir}/%{name}.{a,la}

# Remove the documentation dir, as %doc will pick it up
rm -rf %{buildroot}%{_datadir}/doc

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*.pc


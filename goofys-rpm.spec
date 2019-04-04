%global _prefix /usr/local

Name:    goofys
Version: 0.19.0
Release: 2
Summary: A high-performance, POSIX-ish Amazon S3 file system written in Go
Group:   Development Tools
License: ASL 2.0
Source0: https://github.com/kahing/goofys/releases/download/v%{version}/goofys
Requires: fuse

%description
Goofys allows you to mount an S3 bucket as a filey system.
It's a Filey System instead of a File System because goofys strives for performance first and POSIX second. 
Particularly things that are difficult to support on S3 or would translate into more than one round-trip
would either fail (random writes) or faked (no per-file permission).
Goofys does not have an on disk data cache (checkout catfs), and consistency model is close-to-open.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%global GIT_TAG 57eb4fdd4dfe364fd7d1171c6b66d1b5e4ff6b0f
%global GIT_SHORTTAG 57eb4fdd
%global GIT_DATE 20240215
%global debug_package %{nil}

Name:           hccl_ofi_wrapper
Version:        0.0.1.%{GIT_DATE}git%{GIT_SHORTTAG}
Release:        1%{?dist}
Summary:        HCCL OFI Wrapper

License:        BSD
URL:            https://github.com/HabanaAI/hccl_ofi_wrapper
Source0:        https://github.com/HabanaAI/hccl_ofi_wrapper/archive/%{GIT_TAG}.tar.gz

BuildRequires:  g++
BuildRequires:  make
BuildRequires:  libfabric-devel >= 1.20
Requires:       libfabric >= 1.20
Requires:       habanalabs-graph

%description
HCCL (Habana Collective Communication Library) supports inter-node communication based on OFI libfabric.
HCCL OFI wrapper introduced to act as a thin layer connecting between HCCL and libfabric APIs.


%prep
%autosetup -n hccl_ofi_wrapper-%{GIT_TAG}


%build
make make LIBFABRIC_ROOT=%{_prefix}


%install
install -D -p -m 0755 libhccl_ofi_wrapper.so %{buildroot}/usr/lib/habanalabs/libhccl_ofi_wrapper.so


%files
%license license.txt
%doc README.md
/usr/lib/habanalabs/libhccl_ofi_wrapper.so


%changelog
* Wed Jun 19 2024 Christian Heimes <cheimes@redhat.com> - 0.0.1.20240215git57eb4fdd-1
- Initial release of hccl_ofi_wrapper

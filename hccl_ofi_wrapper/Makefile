SPEC = hccl_ofi_wrapper.spec

.PHONY: srpm rpm getsources
srpm:
	rpmbuild --define "_sourcedir $(CURDIR)" --define "_srcrpmdir $(CURDIR)" -bs $(SPEC)

rpm:
	rpmbuild --define "_sourcedir $(CURDIR)" -bb $(SPEC)

getsources:
	spectool -g $(SPEC)
	sha512sum --tag *.tar.gz > sources


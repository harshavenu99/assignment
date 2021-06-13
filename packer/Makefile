webserver_image_name = webserver


build-webserver-image:

	@echo "Building ${webserver_image_name}"
	@packer build \
		-var-file=params/${webserver_image_name}.json ${webserver_image_name}.json


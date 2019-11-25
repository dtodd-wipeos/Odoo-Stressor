# Create a nice minimal container, living on the edge
# Base install is 5.6MB
FROM alpine:edge

# Install python3 without keeping a cache in the image
# Increases image size to 60.5MB
RUN apk add --no-cache python3

# Include our application
ADD . /opt/stressor/

# Run the stress test
ENTRYPOINT ["/usr/bin/python3"]
CMD ["/opt/stressor/stressor.py"]

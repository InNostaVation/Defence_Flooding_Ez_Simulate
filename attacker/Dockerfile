# Use a basic Linux image as the base image
FROM alpine

RUN apk add apache2-utils
RUN apk add vim
RUN apk add --no-cache bash
# Copy the attack.sh script to the container
COPY attack.sh /

# Make the script executable
RUN chmod +x /attack.sh


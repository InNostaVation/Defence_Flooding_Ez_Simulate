# Use the official NGINX image as the base image
FROM nginx:alpine


# COPY requirements.txt /
# RUN apk add py3-pip
# UN pip3 install --no-cache -r requirements.txt
# Install iptables
RUN apk add --no-cache iptables ip6tables
# RUN apk add --no-cache python3
RUN apk add --no-cache bash

# Copy the custom index.html file to the NGINX document root
COPY index.html /usr/share/nginx/html/index.html

# COPY iptb.py /
# COPY monitor.py /
#COPY --from=builder /usr/local/lib/python3.8/dist-packages /usr/local/lib/python3.8/dist-packages

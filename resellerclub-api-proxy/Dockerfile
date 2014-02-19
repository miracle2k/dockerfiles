FROM dhrp/nginx-proxy

# Add nginx config file
RUN rm /etc/nginx/sites-enabled/readthedocs.conf
ADD httpapi_proxy.conf /etc/nginx/sites-available/httpapi_proxy.conf.template

# Make sure nginx runs in daemon  mode
RUN echo "daemon off;" >> /etc/nginx/nginx.conf 

# This supports the env variable
ADD /run_nginx /run_nginx

EXPOSE 80
EXPOSE 443
CMD /run_nginx

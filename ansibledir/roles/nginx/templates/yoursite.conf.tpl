#jinja2: lstrip_blocks: True
server {
    server_name {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
    access_log /var/log/nginx/{{ user.project_name }}_access.log;
    error_log /var/log/nginx/{{ user.project_name }}_error.log warn;
    location / {
        proxy_set_header                Host  {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
        proxy_set_header                HTTP_Country-Code $geoip_country_code;
        proxy_pass_request_headers      on;
        {% if varnish.enable==true %}
        proxy_pass http://localhost:{{ varnish.ports }};
        {% else %}  
        proxy_pass http://localhost:{{ nginx_php.ports }};
        {% endif %}
        proxy_read_timeout 1800;
        proxy_connect_timeout 1800;

    }
}







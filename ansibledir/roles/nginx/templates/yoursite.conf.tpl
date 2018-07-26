server {
    server_name {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
    access_log /var/log/nginx/{{ user.project_name }}/access.log;
    error_log /var/log/nginx/{{ user.project_name }}/error.log warn;
    location / {
        proxy_set_header                Host  {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
        proxy_set_header                HTTP_Country-Code $geoip_country_code;
        proxy_pass_request_headers      on;  
        proxy_pass http://localhost:{{ nginx_php.ports }};
        proxy_read_timeout 1800;
        proxy_connect_timeout 1800;

    }
}







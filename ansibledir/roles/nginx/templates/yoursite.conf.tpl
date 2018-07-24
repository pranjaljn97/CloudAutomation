server {
    server_name {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
    location / {
        proxy_set_header                Host  {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
        proxy_set_header                HTTP_Country-Code $geoip_country_code;
        proxy_pass_request_headers      on;  
        proxy_pass http://localhost:{{ nginx_php.ports }};
        proxy_read_timeout 1800;
        proxy_connect_timeout 1800;

    }
}







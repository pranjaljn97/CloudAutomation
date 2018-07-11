server {
    server_name {{ user.project_name }}-{{ user.application_name }}.tothenew.tk;
    location / {
        proxy_pass http://localhost:{{ nginx_php.ports }};
    }
}

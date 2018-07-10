server {
    listen 80;
    server_name {{ user.project_name }}_{{ user.application_name }}.tothenew.tk;
    location / {
        proxy_pass http://127.0.0.1:{{ nginx_php.ports }};
    }
}
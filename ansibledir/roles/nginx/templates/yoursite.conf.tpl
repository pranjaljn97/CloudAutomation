server {
    listen 80;
    server_name {{ user.project_name }}_{{ user.application_name }}.tothenew.tk;
    access_log /home/{{ user.project_name }}/logs/access.log;
    error_log /home/{{ user.project_name }}/logs/error.log;
    location / {
        proxy_pass http://127.0.0.1:{{ nginx_php.ports }};
    }
}
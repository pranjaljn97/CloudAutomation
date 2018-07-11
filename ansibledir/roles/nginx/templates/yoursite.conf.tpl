server {
    server_name {{ user.project_name }}_{{ user.application_name }}.tothenew.tk;
    access_log /home/{{ user.project_name }}/logs/access.log;
    error_log /home/{{ user.project_name }}/logs/error.log;
    location / {
        proxy_pass localhost:{{ nginx_php.ports }};
    }
}

vcl 4.0;

backend default {
   .host = "nginx_php";
   .port = "80";
}

sub vcl_recv {
}

sub vcl_backend_response {
}

sub vcl_deliver {
}
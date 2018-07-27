user www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
  worker_connections 768;
  # multi_accept on;
}

http {
  # Prevent flood
  limit_conn_zone $binary_remote_addr zone=conn_limit_per_ip:10m;
  limit_req_zone $binary_remote_addr zone=req_limit_per_ip:10m rate=5r/s;
  # Format log
  log_format timed_combined '$remote_addr - $remote_user [$time_local] '
    '"$request" $status $body_bytes_sent '
    '"$http_referer" "$http_user_agent" '
    '$request_time $upstream_response_time $pipe';
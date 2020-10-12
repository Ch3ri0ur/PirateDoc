# Getting Started

Not all steps are transferable so it is assumed that a domain is available and Let's Encrypt or a certificate is available.

## Get Caddy

Download it either via:

https://caddyserver.com/download

https://caddyserver.com/docs/download

or directly from Github via:

```
curl -OL https://github.com/caddyserver/caddy/releases/download/v2.2.0/caddy_2.2.0_linux_armv7.tar.gz
```

Unzip the directory with for instance:

```
tag -xz caddy_2.2.0_linux_armv7.tar.gz
```

and move / rename the caddy executable to a suitable location. 

## Configure Caddy

There create a file called "caddyfile" without an extension and fill it with the following content:

```
{    
admin :34567 # expose admin port
}
theuseddomain.ending  # ! INSERT correct domain under which to serve

reverse_proxy /* localhost:3000  # Website
reverse_proxy /getconfig raspberrypi:9876 # Pirate-Bridge
reverse_proxy /ctrl raspberrypi:9876 # Pirate-Bridge
reverse_proxy /janus* raspberrypi:8088 # Pirate-Spyglass
reverse_proxy /stream { # Pirate-Bridge
	flush_interval -1
	to raspberrypi:9876
	}

# if specific certs are used otherwise delete the tls line and ensure that the ports 80 and 443 are forwarded to the caddy server so that it can enable HTTPS/TLS via Let's Encrypt 
tls "<path_to_cert>.crt" "<path_to_public_key>.key"  # enable tls 

```

## Start Caddy

If the Caddy executable is in the same folder as the caddy file it can now be started with:

```
caddy run
```

it might be necessary to specify further

```
./caddy run -f ./caddyfile
```

If you want to run caddy detached replace "run" with "start".

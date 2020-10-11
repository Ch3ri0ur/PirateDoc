# Chart Implementation

This is currently a small component, because only one project is supported and the project is not yet integrated in the targeted network. 

In its current form only a reverse proxy under a temporary domain is set up, enabling HTTPS. Because it is used on a residential connection Dynamic DNS is set up on the Router.

## Domain

The domain is currently bought from [namecheap](https://www.namecheap.com/). 

## Dyn-DNS

The Dynamic DNS is provided by a "Fritz Box" router set up to communicate with the namecheap service. It periodically updates the current IP-Adress of the residential connection.

## Certificates

Even tough namecheap provides certificates it is easier to use the automatic certification via [Let's Encrypt](https://letsencrypt.org/). 

## Reverse Proxy

The used reverse proxy is a [caddy](https://caddyserver.com/) server. It enables automatic certificates via Let's Encrypt. It is written in the programming language Go. This has the benefit, that Go programs are mostly compiled to a single executable, making the deployment very easy. The caddy server also uses a single configuration file. The configuration used for the reverse proxies can be viewed in the [setup section](10-chart-getting-started.md)

The reverse proxy supports the following routes.

A reverse proxy is used to create a unified front and as a TLS boundary.

| URL        | Use                                  | Target        | Port |
| ---------- | ------------------------------------ | ------------- | ---- |
| /          | Website                              | Webserver     | 3000 |
| /getconfig | Arduino Config from Node             | Pirate-Bridge | 9876 |
| /ctrl      | POST Control of Arduino through Node | Pirate-Bridge | 9876 |
| /stream    | SSE-Stream from Node                 | Pirate-Bridge | 9876 |
| /janusopt  | Janus WebRTC Stream                  | Janus-Gateway | 8088 |

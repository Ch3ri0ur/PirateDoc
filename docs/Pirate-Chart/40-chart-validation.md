# Chart Validation and Future Steps

In this section the initial requirements are measured against the current implementation.

## Functional Requirements

The functional requirements are not matched by the current implementation.

### Create an Unified Endpoint

The client should be able to access all functionality over HTTPS. This includes:

* Get Bridge endpoints
* Get videostream from the Spyglass

This requirement is partially fulfilled. With one project on a temporary domain it is possible to access the project as intended. But it is not yet integrated in the target network.

### Enable routing to different Projects 

The routing solution should be able to support multiple projects which can be visited independently from each other.

This requirement is not met. A solution is designed, but the feasibility in a corporate environment has not been investigated.

A temporary solution can be created by using another reverse proxy in front of the individual pirate modules. This proxy would strip a /projectX/ suffix from the URL and forward the requests to the standardized endpoints of the modules.

### Advertise different Project in a summary Site

The available Projects should be aggregated in a single source.

This requirement is not met. As there is not yet a way to target multiple projects, no such site / aggregation is implemented.

## Non-Functional Requirements

* The solution needs to be robust and run for at least 3 hours und continuous load.
    * A reverse proxy is a very established technology and ran 72 hours without interruption.
* The solution needs to enable 24/7 availability.
    * A reverse proxy is a very established technology and ran 72 hours without interruption.
* The latency should not be significantly increased by the routing.
    * A reverse proxy is a very established technology and latency is minimal.
* A single project must be implemented.
    * The current implementation points directly to the single project. This requirement is fulfilled.

## Future Steps

The original goal of integration this solution into a more complex network and enabling access to multiple projects needs to be implemented. 




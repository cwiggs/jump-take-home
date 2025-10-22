# Jump-take-home
This repo contains a minimal Python Flask application.  The application is very simple,
it returns text at the root path on port 5000.

There is a basic Dockerfile that builds the application and uses the Flask dev web server.

## CI
There is a Github Action workflow that builds the container image and pushes it to Github 
Container Registry (GHCR).

## CD
Deployment is done via kubectl manually.  The deployment manifest is in the `k8s` directory.

Thanks to the reconsiliation loop in Kubernetes, any new image pushed to GHCR with the same tag
will automatically be deployed.

## Requirements:
1. [x] Create a minimal server and Dockerfile.
2. [x] Run locally once to verify 'Hello world'
3. [x] Push to the repo; show CI building/pushing/deploying to your chosen cloud.
4. [x] Commit the text change to "Hello World. I was updated with CI!"
5. [x] Push; show CI logs and successful redeploy
6. [x] Verify the cloud endpoint shows the updated response.

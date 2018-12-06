## Usage:

*nix: sh run.sh; curl localhost:5000/trends/mysearchterm/mylimit

## notes:

as indicated by: 
https://stackoverflow.com/questions/30525330/how-to-get-list-of-trending-github-repositories-by-github-api
there is still no access to the trending repo data directly (neither via graphql...)

error handling is quite simple: if either param is not given, return an error.

i could not find a max limit for per_page in the github docs

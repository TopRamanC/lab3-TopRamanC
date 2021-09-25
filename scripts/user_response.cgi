#!/bin/bash

# Variables for username
USERNAME=${QUERY_STRING#*Username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

# Emit the HTTP response header
echo "X-function: Emitting a hereis document"
echo "Content-type: text/html"

# Emit a blank line to separate the HTTP response header from the HTTP response body
echo ""

# Emit the HTTP response body
cat <<EOF
<html>
  <head>
     <title>Response Page</title>
  </head>
  <body>
    <h3>Here is the username you entered: </h3>
  <h4>You entered:  $USERNAME<h4>
  </body>
</html>
EOF

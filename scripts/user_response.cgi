#!/bin/bash

USERNAME=${QUERY_STRING#*Username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

echo "X-function: Emitting a hereis document"
echo "Content-type: text/html"

echo ""

cat <<EOF
<!-- Start of the Body -->
<html>
  <head>
     <title>Response Page</title>
  </head>
  <body>
    <h3>Here is the username you entered: </h3>
  <h4>You entered:  $USERNAME<h4>
  </body>
</html>
<!-- End of the Body -->
EOF

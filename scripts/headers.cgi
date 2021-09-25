#!/bin/bash

# Emit the HTTP response header
echo "X-function: Emitting a hereis document"
echo "X-cit-384-student: $USER"
echo "Date: $(date)"
echo "Accept-Language: en-US"
echo "Content-type: text/html"


# Emit a blank line to separate the HTTP response header from the HTTP response body 
echo ""


# Emit the HTTP response body
cat <<EOF
<!-- Start of the Body -->
<html>
  <head>
     <title>Hello!</title>
  </head>
  <body>
    <h1>A Simple HTML Document</h1>
    "Hello!"
  </body>
</html>
<!-- End of the Body -->
EOF

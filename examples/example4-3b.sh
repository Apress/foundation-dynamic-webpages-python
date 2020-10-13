#!/usr/bin/sh

echo "Content-type:text/html"
echo ""
echo "<!DOCTYPE html>"
echo "<head>"
echo "   <meta http-equiv=""Content-Type"" content=""text/html; charset=iso-8859-1"" />"
echo "</head>"
echo "<html>"
echo "<body>"
echo "<p>This is output from a shell script. "
echo "The current date is $(date).</p>"
echo "</body>"
echo "</html>"


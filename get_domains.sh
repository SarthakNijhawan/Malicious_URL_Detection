#!/bin/bash - 
#===============================================================================
#
#          FILE: get_domains.sh
# 
#         USAGE: ./get_domains.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Vikrant (Vikrant), vikrant@cse.iitb.ac.in
#  ORGANIZATION: 
#       CREATED: Friday 31 March 2017 17:01
#      REVISION:  ---
#===============================================================================

    
while read p;
do
    ip=`nslookup "$p" | grep "Address: "| head -n1 | cut -d' ' -f2`;
    echo "$p $ip"
done < "domains_http.txt";

    



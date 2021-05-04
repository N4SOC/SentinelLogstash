if [[ $1 != False ]]; then

    sed -i "s/# additional_output/$syslogconfig/g"  /usr/share/logstash/pipeline/logstash.conf
else
    echo "not A"
fi
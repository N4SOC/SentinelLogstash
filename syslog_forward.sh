set +o allexport
source .env
echo "$syslog_forward"

if [ "$syslog_forward" == "True" ]; then
    echo "Doing"
    syslog_config=$(cat <<-END
        syslog {
            host => "127.0.0.1"
            port => 514
            protocol => "tcp"
    }
END
)
echo "Injecting Config..."
grep -c "# additional_output"  ./*/logstash.conf

sed -i "s/# additional_output/$syslog_config/g"  ./*/logstash.conf
fi
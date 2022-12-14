
def deployids(interface, table):
    volumes = ['zeeklogs']
    yml = yaml.dump({"volumes": volumes})
    args["table"] = collector["table"]
    zeek = {"build": {
        "context": "./zeek",
        "args": args
    },
        "image": "zeek_sentinel",
        "volumes": []
    }
    zeek_ids = []
    services['zeek'] = zeek
    services['zeek_ids'] = zeek_ids

    """
      zeek:
    build:
      context: ./zeek
      args:
        environment_name: ${environment_name}
        workspaceID: ${workspaceID}
        workspaceKey: ${workspaceKey}
    image: zeek_sentinel
    volumes:
      - type: volume
        source: zeeklogs
        target: /logs/
    profiles:
      - ids

  zeek_ids:
    build:
      context: ./zeek_ids
      args:
        span_interface: ${span_interface}
    image: zeek_ids
    volumes:
      - type: volume
        source: zeeklogs
        target: /opt/zeek/spool/zeek
    network_mode: host
    cap_add:
      - sys_nice
      - net_admin
    stdin_open: true # docker run -i
    tty: true # docker run -t
    profiles:
      - ids
      """
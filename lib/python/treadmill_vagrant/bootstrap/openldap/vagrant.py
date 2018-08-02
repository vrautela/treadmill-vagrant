"""Treadmill AWS Zookeeper bootstrap.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import vagrant_aliases as aliases


_DEFAULT_HOST_TICKET = 'treadmill/spool/tickets/krb5cc_host'

DEFAULTS = {
    'treadmill_host_ticket': _DEFAULT_HOST_TICKET,
    'data_dir': '/treadmill/zookeeper/data',
    'tick_time': 20,
    'init_limit': 5,
    'sync_limit': 2,
    'max_client_cnxns': 0,
    'jaas_login_renew': 3600000,
    'max_sessions_timeout': 360000,
    'restart_interval': 300,
    'restart_limit': 5,
    'zk_distro': '/opt/zookeeper',
    'keytab': '/treadmill/zookeeper/zookeeper.keytab',
    'zkroot': '/treadmill/zookeeper',
}

ALIASES = aliases.ALIASES

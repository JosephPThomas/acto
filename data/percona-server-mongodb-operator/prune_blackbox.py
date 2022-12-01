import sys

sys.path.append('../..')
import input

custom_fields = [
    input.CopiedOverField(['spec', 'backup', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'backup', 'resources']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'arbiter', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'arbiter', 'resources']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'arbiter', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'arbiter', 'tolerations']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'resources']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'tolerations']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'resources']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'tolerations']),
    input.CopiedOverField(['spec', 'replsets', 'ITEM', 'volumeSpec', 'persistentVolumeClaim']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'resources']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'arbiter', 'tolerations']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'resources']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'tolerations']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'nonvoting', 'volumeSpec', 'persistentVolumeClaim']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'resources']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'tolerations']),
    input.CopiedOverField(['spec', 'sharding', 'configsvrReplSet', 'volumeSpec', 'persistentVolumeClaim']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'affinity', 'advanced']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'containerSecurityContext']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'podSecurityContext']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'resources']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'sidecarPVCs', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'sidecarVolumes', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'sidecars', 'ITEM']),
    input.CopiedOverField(['spec', 'sharding', 'mongos', 'tolerations']),

    input.ProblematicField(['spec', 'pmm']),  # ignore external dependency
    input.ProblematicField(['spec', 'crVersion'], string=True),  # ignore external dependency
    input.ProblematicField(['spec', 'mongod', 'setParameter']),  # ignore external dependency
    input.ProblematicField(['spec', 'mongod', 'security']),
    input.ProblematicField(['spec', 'mongod', 'replication']),
    input.ProblematicField(['spec', 'mongod', 'operationProfiling']),
]
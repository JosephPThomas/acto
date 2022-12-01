import input
import schema

custom_fields = [
    input.CopiedOverField(['spec', 'configBuilderResources']),
    input.CopiedOverField(['spec', 'podTemplateSpec']),
    input.CopiedOverField(['spec', 'resources']),
    input.CopiedOverField(['spec', 'storageConfig', 'additionalVolumes', 'INDEX', 'pvcSpec']),
    input.CopiedOverField(['spec', 'storageConfig', 'cassandraDataVolumeClaimSpec']),
    input.CopiedOverField(['spec', 'systemLoggerResources']),
    input.OverSpecifiedField(['spec', 'managementApiAuth', 'manual']),
    input.CopiedOverField(['spec', 'tolerations'], True),
]
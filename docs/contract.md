# Genomic variant normalization contract

Sequence-data engineers provide one bounded uppercase ACGT reference and 1-based variants with nonempty reference and alternate alleles. Every reference allele must match the supplied sequence exactly. The service removes redundant shared suffix and prefix context while retaining at least one base in each allele, then left-aligns indels through identical repeated trailing bases.

Each result retains its source identity and canonical key. Source variants that normalize to the same position/ref/alt form an explicit equivalence group. The baseline does not parse VCF, handle symbolic alleles, phase genotypes, annotate genes or make medical interpretations.

The result is a reference-aware normalization data product, not a patient system or generic text tool. Future call-set comparison can consume canonical keys while preserving source caller identity.

#!/usr/bin/python3
import iptc

# Example: Creating a rule
rule = iptc.Rule()
rule.src = "192.168.1.0/24"
rule.target = iptc.Target(rule, "ACCEPT")

# Add the rule to the INPUT chain
chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
chain.insert_rule(rule)

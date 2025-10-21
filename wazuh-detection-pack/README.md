#  Detection Pack

Production-grade Wazuh custom rules ready for use in enterprise environments. Rules focus on high-signal detections for Windows, Linux, and SSH, with MITRE ATT&CK mapping and sensible safeguards.

## Contents
- `rules/custom_rules.xml` – Ready-to-deploy rules.
- `tools/validate_rules.py` – Simple XML validator and ID uniqueness check.
- `.github/workflows/xml-lint.yml` – CI to validate XML on pull requests.
- `LICENSE` – MIT License.

## Quick start

1. Copy `rules/custom_rules.xml` to your Manager:
   - **Wazuh 4.x** (recommended): `/var/ossec/etc/rules/local_rules.xml` *or* `/var/ossec/etc/rules.d/custom_rules.xml`
2. Validate and restart/reload the manager:
   ```bash
   sudo /var/ossec/bin/wazuh-logtest -U /var/ossec/etc/rules/local_rules.xml
   sudo systemctl restart manager
   ```
3. (Optional) Keep it as a dedicated rules file:
   ```bash
   sudo cp rules/custom_rules.xml /var/ossec/etc/rules.d/1100-custom-detections.xml
   sudo systemctl restart manager
   ```

## Data sources expected
- **Windows Security** logs (Event IDs: 1102, 4698, 4720, 4728, 4732).
- **Sysmon** Event ID 1 (Process Create) via Windows agent (group: `sysmon_event1`).
- **Syscheck (FIM)** for Linux critical paths (group: `syscheck`).
- **sshd** authentication logs on Linux (program name `sshd`).

## Rules Overview (MITRE ATT&CK)
- Suspicious PowerShell execution — T1059.001, T1105, T1055
- Privileged group membership add — T1098, T1069, T1078
- Linux critical auth file change — T1098, T1547, T1068
- Windows Security log cleared — T1070.001
- New local user created — T1136.001
- Scheduled task created — T1053.005
- LOLBIN abuse (signed binary proxy) — T1218, T1105
- SSH brute-force followed by success — T1110, T1078

## Contributing
- Open a PR; CI will lint the XML.
- Keep rule IDs in the **110000–119999** range to avoid collisions with vendor rules.
- Include `<decoded_as>`, `<group>`, `<if_group>`, and meaningful `<description>` for each rule.
- Add MITRE IDs in `<mitre>` blocks when applicable.

## License
MIT – see `LICENSE`.





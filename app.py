import streamlit as st
import pandas as pd

st.set_page_config(page_title="شهادات الشبكات", layout="wide")

# --- بيانات المحاور والعناصر ---
domains = [
    "Networking Fundamentals",
    "Infrastructure",
    "Network Operations",
    "Network Security",
    "Network Troubleshooting"
    
]

topics_dict = {
    "Networking Fundamentals": [
        "Network Topologies and Types",
        "Network Architecture (Three-tier, Collapsed Core, Spine/Leaf)",
        "IP Addressing and Subnetting (IPv4, IPv6, APIPA, CIDR, VLSM)",
        "Ports and Protocols (HTTP, HTTPS, FTP, DNS, NTP, SNMP, LDAP, RDP, SIP, SMTP, SMB, Syslog)",
        "Traffic Flow and Communication Types (Unicast, Multicast, Anycast, Broadcast, North/South, East/West)",
        "Network Media and Devices (Cables, Fiber, Transceivers, Connectors)",
        "WAN Technologies (SD-WAN, VPN, Data Center Interconnect)",
        "Network Automation and Management (IaC, Zero-touch provisioning, Playbooks, Version Control)"
    ],
    "Infrastructure": [
        "Common Networking Devices (Switches, Routers, Firewalls, Access Points, Hubs)",
        "Cabling and Physical Media (Twisted Pair, Coaxial, Fiber, DAC, Twinax)",
        "Wireless Technologies (802.11 Standards, Frequency Bands, Wi-Fi Security)",
        "Cloud and Virtualization Concepts (VMs, Hypervisors, Virtual Networks)",
        "Network Storage Solutions (SAN, NAS, Fibre Channel)",
        "WAN Technologies (MPLS, Satellite, Cellular, Leased Lines)"
    ],
    "Network Operations": [
        "Network Monitoring and Management Tools (SNMP, Syslog, Flow Analysis)",
        "Configuration Management (Backups, Automation, Templates)",
        "High Availability Concepts (Redundancy, Failover, Load Balancing)",
        "Disaster Recovery and Business Continuity",
        "Performance Optimization (QoS, Traffic Shaping, Latency Analysis)",
        "Documentation and Diagrams (Network Maps, VLAN Documentation)"
    ],
    "Network Security": [
        "Network Security Concepts (Confidentiality, Integrity, Availability)",
        "Authentication and Access Control (AAA, MFA, Policy-based Authentication)",
        "Network Security Devices (Firewalls, IDS/IPS, VPNs, NAC)",
        "Secure Network Architectures (Zero Trust, SASE, SD-WAN Security)",
        "Encryption and Protocol Security (IPSec, SSL/TLS, HTTPS, SNMPv3)",
        "Security Policies and Best Practices (Least Privilege, Patch Management, User Awareness)"
    ],
    "Network Troubleshooting": [
        "Troubleshooting Methodologies (Identify, Analyze, Implement, Verify)",
        "Common Network Issues (Connectivity, Latency, DNS, DHCP, IP Conflicts)",
        "Network Diagnostic Tools (Ping, Traceroute, ipconfig/ifconfig, nslookup, netstat)",
        "Performance and Traffic Analysis Tools (Wireshark, SNMP Monitors, Flow Analyzers)",
        "Cable and Hardware Testing Tools (Cable Testers, TDR, OTDR, Multimeter)"
    ]
}

# --- قائمة لتخزين البيانات في الجلسة ---
if "certifications" not in st.session_state:
    st.session_state.certifications = []

# --- نموذج إضافة شهادة ---
st.header("إضافة شهادة جديدة")
with st.form("cert_form"):
    certificate_name = st.text_input("اسم الشهادة")
    domain = st.selectbox("اختر المحور", domains)

    st.markdown("**اختر العنصر:**")
    topic = st.radio("", topics_dict[domain], )

    submitted = st.form_submit_button("إضافة")

    if submitted:
        if certificate_name.strip() == "":
            st.warning("يرجى إدخال اسم الشهادة قبل الإضافة.")
        elif not topic:
            st.warning("يرجى اختيار عنصر من المحور.")
        else:
            st.session_state.certifications.append({
                "الشهادة": certificate_name,
                "المحور": domain,
                "العنصر": topic
            })
            st.success(f"تمت إضافة: {certificate_name} → {domain} → {topic}")

# --- عرض البيانات ---
st.header("البيانات المخزنة")
df = pd.DataFrame(st.session_state.certifications)
st.dataframe(df, use_container_width=True)

# --- زر لتحميل الملف ---
if not df.empty:
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ تحميل كملف CSV",
        data=csv,
        file_name="certifications.csv",
        mime="text/csv"
    )






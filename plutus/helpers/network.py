import psutil
import pyshark


class MonitorNetwork(object):
    def __init__(self):
        self.__description__ = "This is a monitoring class"

    # this performs a quick scan output of established connection from the server with remote devices.
    @staticmethod
    def mnt_in_out():
        connections = psutil.net_connections()
        saved_conns = []
        for connection in connections:
            if connection.status == 'ESTABLISHED':
                data = f"[LOCAL ADDRESS][{connection.laddr.ip}:{connection.laddr.port}] [ESTABLISHED CONNECTION TO] -> [REMOTE ADDRESS][{connection.raddr.ip}:{connection.raddr.port}]"
                saved_conns.append(data)

        return saved_conns

    # monitor a single IP
    @staticmethod
    def single_mnt_in_out(ip: str):
        connections = psutil.net_connections()
        logs = []
        for conn in connections:
            remote_ip = conn.raddr.ip
            local_ip = conn.laddr.ip

            if remote_ip == ip or local_ip == ip:
                data = f"[LOCAL ADDRESS][{local_ip}:{conn.laddr.port}] [{conn.status}] -> [REMOTE ADDRESS][{remote_ip}:{conn.raddr.port}]"
                logs.append(data)

        return logs

    # from a list of suspicious IP that you want to keep an eye on as well as asserted with the IPs from threat intel platform
    @staticmethod
    def flag_suspicious_ip(ip_file: str):
        suspicious_ips = []
        logs = []
        with open(ip_file, 'r') as file:
            for line in file:
                ip = line.strip()
                suspicious_ips.append(ip)

        connections = psutil.net_connections()
        for conn in connections:
            remote_ip = conn.raddr.ip
            local_ip = conn.laddr.ip
            if local_ip in suspicious_ips or remote_ip in suspicious_ips:
                data = f"[LOCAL ADDRESS][{local_ip}:{conn.laddr.port}] [{conn.status}] -> [REMOTE ADDRESS][{remote_ip}:{conn.raddr.port}]"
                logs.append(data)

        return logs

    # captures packets continuously and hunt for malicious packets
    @staticmethod
    def malicious_monitoring(iface: str):
        capture = pyshark.LiveCapture(interface=iface)
        packets = []
        for packet in capture.sniff_continuously():
            if "malicious_pattern" in packet:
                # print("[!] [SUSPICIOUS ACTIVITY DETECTED ON THE NETWORK] [!]")
                packets.append(packet)

        return packets
